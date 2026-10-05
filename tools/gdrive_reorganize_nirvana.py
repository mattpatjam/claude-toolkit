#!/usr/bin/env python3
"""
gdrive_reorganize_nirvana.py — Reorganize the Nirvana folder on the ScaleRise Shared Drive.

New structure:
  OLC-Method/Clients/Nirvana/
  ├── project.tracker.md
  ├── training-structure.md
  ├── Strategy/
  ├── Admin/
  ├── Marketing/
  ├── Session-0-Audit/
  ├── Session-1-Offer/
  ├── Session-2-Discovery/
  └── Session-3-Closing/
"""

import json, os, mimetypes, uuid, sys
import requests

CREDENTIALS_FILE  = "/Users/matt/.claude/gdrive-scalrize-credentials.json"
TOKEN_FILE        = "/Users/matt/.claude/gdrive-scalrize-token.json"
SHARED_DRIVE_NAME = "Scale-Rise & OLC Method"
LOCAL_BASE        = "/Users/matt/Desktop/Claude/olc-method/clients/nirvana"

def refresh_token():
    with open(CREDENTIALS_FILE) as f: creds = json.load(f)["installed"]
    with open(TOKEN_FILE) as f: tok = json.load(f)
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": creds["client_id"], "client_secret": creds["client_secret"],
        "refresh_token": tok["refresh_token"], "grant_type": "refresh_token",
    })
    r.raise_for_status()
    return r.json()["access_token"]

def find_shared_drive(token):
    r = requests.get("https://www.googleapis.com/drive/v3/drives",
        headers={"Authorization": f"Bearer {token}"}, params={"pageSize": 100})
    r.raise_for_status()
    for d in r.json().get("drives", []):
        if d["name"] == SHARED_DRIVE_NAME:
            return d["id"]
    raise ValueError(f"Shared Drive '{SHARED_DRIVE_NAME}' not found")

def list_folder(token, folder_id, drive_id):
    results, page_token = [], None
    while True:
        params = {
            "q": f"'{folder_id}' in parents and trashed=false",
            "corpora": "drive", "driveId": drive_id,
            "includeItemsFromAllDrives": "true", "supportsAllDrives": "true",
            "fields": "nextPageToken,files(id,name,mimeType)",
            "pageSize": 100,
        }
        if page_token: params["pageToken"] = page_token
        r = requests.get("https://www.googleapis.com/drive/v3/files",
            headers={"Authorization": f"Bearer {token}"}, params=params)
        r.raise_for_status()
        data = r.json()
        results.extend(data.get("files", []))
        page_token = data.get("nextPageToken")
        if not page_token: break
    return results

def find_folder(token, name, parent_id, drive_id):
    safe = name.replace("'", "\\'")
    r = requests.get("https://www.googleapis.com/drive/v3/files",
        headers={"Authorization": f"Bearer {token}"},
        params={
            "q": f"name='{safe}' and '{parent_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false",
            "corpora": "drive", "driveId": drive_id,
            "includeItemsFromAllDrives": "true", "supportsAllDrives": "true",
            "fields": "files(id,name)",
        })
    r.raise_for_status()
    files = r.json().get("files", [])
    return files[0]["id"] if files else None

def get_or_create_folder(token, name, parent_id, drive_id):
    fid = find_folder(token, name, parent_id, drive_id)
    if fid:
        return fid
    r = requests.post("https://www.googleapis.com/drive/v3/files",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        params={"supportsAllDrives": "true"},
        json={"name": name, "mimeType": "application/vnd.google-apps.folder", "parents": [parent_id]})
    r.raise_for_status()
    print(f"  + Created folder: {name}")
    return r.json()["id"]

def rename_folder(token, folder_id, new_name):
    r = requests.patch(f"https://www.googleapis.com/drive/v3/files/{folder_id}",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        params={"supportsAllDrives": "true"},
        json={"name": new_name})
    r.raise_for_status()
    print(f"  ~ Renamed to: {new_name}")

def move_file(token, file_id, old_parent_id, new_parent_id):
    r = requests.patch(f"https://www.googleapis.com/drive/v3/files/{file_id}",
        headers={"Authorization": f"Bearer {token}"},
        params={"addParents": new_parent_id, "removeParents": old_parent_id, "supportsAllDrives": "true", "fields": "id,name"})
    r.raise_for_status()

def upload_file(token, local_path, folder_id, drive_id):
    filename = os.path.basename(local_path)
    mime_type, _ = mimetypes.guess_type(local_path)
    if not mime_type: mime_type = "application/octet-stream"
    with open(local_path, "rb") as f: content = f.read()
    # check existing
    safe = filename.replace("'", "\\'")
    r = requests.get("https://www.googleapis.com/drive/v3/files",
        headers={"Authorization": f"Bearer {token}"},
        params={
            "q": f"name='{safe}' and '{folder_id}' in parents and trashed=false",
            "corpora": "drive", "driveId": drive_id,
            "includeItemsFromAllDrives": "true", "supportsAllDrives": "true",
            "fields": "files(id)",
        })
    r.raise_for_status()
    existing = r.json().get("files", [])
    boundary = uuid.uuid4().hex
    metadata = {"name": filename}
    if not existing: metadata["parents"] = [folder_id]
    body = (f"--{boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n"
            f"{json.dumps(metadata)}\r\n--{boundary}\r\nContent-Type: {mime_type}\r\n\r\n"
            ).encode() + content + f"\r\n--{boundary}--".encode()
    if existing:
        url, method = f"https://www.googleapis.com/upload/drive/v3/files/{existing[0]['id']}", "PATCH"
    else:
        url, method = "https://www.googleapis.com/upload/drive/v3/files", "POST"
    r = requests.request(method, url,
        headers={"Authorization": f"Bearer {token}", "Content-Type": f"multipart/related; boundary={boundary}"},
        params={"uploadType": "multipart", "supportsAllDrives": "true", "fields": "id,name"},
        data=body)
    r.raise_for_status()
    action = "Updated" if existing else "Uploaded"
    print(f"  {action}: {filename} ({len(content)//1024}KB)")

def resolve_path(token, path, drive_id):
    parts = [p for p in path.strip("/").split("/") if p]
    current = drive_id
    for part in parts:
        current = get_or_create_folder(token, part, current, drive_id)
    return current

def main():
    print("Refreshing token...")
    token = refresh_token()
    print("Finding Shared Drive...")
    drive_id = find_shared_drive(token)
    nirvana_id = resolve_path(token, "OLC-Method/Clients/Nirvana", drive_id)

    print("\n--- Auditing current Drive structure ---")
    items = list_folder(token, nirvana_id, drive_id)
    folders = {i["name"]: i["id"] for i in items if i["mimeType"] == "application/vnd.google-apps.folder"}
    files   = {i["name"]: i["id"] for i in items if i["mimeType"] != "application/vnd.google-apps.folder"}
    print(f"  Folders: {sorted(folders.keys())}")
    print(f"  Files:   {sorted(files.keys())}")

    print("\n--- Creating new top-level folders ---")
    strategy_id  = get_or_create_folder(token, "Strategy",  nirvana_id, drive_id)
    admin_id     = get_or_create_folder(token, "Admin",     nirvana_id, drive_id)
    marketing_id = get_or_create_folder(token, "Marketing", nirvana_id, drive_id)

    print("\n--- Renaming Session folders ---")
    renames = {
        "Session-0": "Session-0-Audit",
        "Session-1": "Session-1-Offer",
        "Session-2": "Session-2-Discovery",
        "Session-3": "Session-3-Closing",
    }
    for old, new in renames.items():
        if old in folders:
            if new not in folders:
                rename_folder(token, folders[old], new)
                folders[new] = folders.pop(old)
            else:
                print(f"  Already named: {new}")
        else:
            print(f"  Not found on Drive: {old} (may already be renamed or missing)")
    # Refresh folder listing after renames
    items = list_folder(token, nirvana_id, drive_id)
    folders = {i["name"]: i["id"] for i in items if i["mimeType"] == "application/vnd.google-apps.folder"}
    files   = {i["name"]: i["id"] for i in items if i["mimeType"] != "application/vnd.google-apps.folder"}

    print("\n--- Moving loose files to correct folders ---")
    # Marketing files
    marketing_files = ["marketing-brief.pdf", "meeting-notes-marketing.pdf", "meeting-prep-marketing.md",
                       "marketing-brief.html", "meeting-notes-marketing.html"]
    for name in marketing_files:
        if name in files:
            move_file(token, files[name], nirvana_id, marketing_id)
            print(f"  Moved to Marketing/: {name}")

    # Admin files
    admin_files = ["toby-proposal.pdf", "toby-proposal.html"]
    for name in admin_files:
        if name in files:
            move_file(token, files[name], nirvana_id, admin_id)
            print(f"  Moved to Admin/: {name}")

    print("\n--- Uploading missing files ---")
    # Strategy folder
    print("  Strategy/")
    for fname in ["brand-foundation.md", "offer.md", "pitch.md", "project-reference.md"]:
        local = os.path.join(LOCAL_BASE, "Strategy", fname)
        if os.path.exists(local):
            upload_file(token, local, strategy_id, drive_id)

    # Admin folder — emails, invoice, proposal
    print("  Admin/")
    admin_local_files = [
        "proposal-nirvana-v2.md", "invoice-nirvana-002.html",
        "email-toby-confirmed.md", "email-toby-session2-prep.md", "email-natasha-session2-prep.md",
        "toby-proposal.html",
    ]
    for fname in admin_local_files:
        local = os.path.join(LOCAL_BASE, "Admin", fname)
        if os.path.exists(local):
            upload_file(token, local, admin_id, drive_id)

    # Session-0-Audit
    print("  Session-0-Audit/")
    s0_id = get_or_create_folder(token, "Session-0-Audit", nirvana_id, drive_id)
    for fname in os.listdir(os.path.join(LOCAL_BASE, "Session-0-Audit")):
        local = os.path.join(LOCAL_BASE, "Session-0-Audit", fname)
        if os.path.isfile(local):
            upload_file(token, local, s0_id, drive_id)

    # Session-1-Offer
    print("  Session-1-Offer/")
    s1_id = get_or_create_folder(token, "Session-1-Offer", nirvana_id, drive_id)
    for fname in os.listdir(os.path.join(LOCAL_BASE, "Session-1-Offer")):
        local = os.path.join(LOCAL_BASE, "Session-1-Offer", fname)
        if os.path.isfile(local):
            upload_file(token, local, s1_id, drive_id)

    # Session-2-Discovery (already exists, make sure all files are there)
    print("  Session-2-Discovery/")
    s2_id = get_or_create_folder(token, "Session-2-Discovery", nirvana_id, drive_id)
    for fname in os.listdir(os.path.join(LOCAL_BASE, "Session-2-Discovery")):
        local = os.path.join(LOCAL_BASE, "Session-2-Discovery", fname)
        if os.path.isfile(local):
            upload_file(token, local, s2_id, drive_id)

    # Session-3-Closing
    print("  Session-3-Closing/")
    s3_id = get_or_create_folder(token, "Session-3-Closing", nirvana_id, drive_id)
    for fname in os.listdir(os.path.join(LOCAL_BASE, "Session-3-Closing")):
        local = os.path.join(LOCAL_BASE, "Session-3-Closing", fname)
        if os.path.isfile(local):
            upload_file(token, local, s3_id, drive_id)

    # Root files
    print("  Root/")
    for fname in ["project.tracker.md", "training-structure.md"]:
        local = os.path.join(LOCAL_BASE, fname)
        if os.path.exists(local):
            upload_file(token, local, nirvana_id, drive_id)

    print("\nDone. Nirvana folder is now reorganized on Drive.")

if __name__ == "__main__":
    main()
