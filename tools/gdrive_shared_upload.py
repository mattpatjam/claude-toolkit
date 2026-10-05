#!/usr/bin/env python3
"""
gdrive_shared_upload.py — Upload a file to the ScaleRise & OLC Method Shared Drive.

Usage:
    python3 tools/gdrive_shared_upload.py <local_file_path> <drive_folder_path>

Examples:
    python3 tools/gdrive_shared_upload.py "olc-method/clients/nirvana/marketing-brief.pdf" "OLC-Method/Clients/Nirvana"
    python3 tools/gdrive_shared_upload.py "Scale-Rise/Internal/brand-foundation.md" "Scale-Rise/Internal"

Folder path is relative to the root of the 'Scale-Rise & OLC Method' Shared Drive.
Folders are created automatically if they don't exist.
Existing files with the same name are overwritten (updated in-place).
"""

import sys
import os
import json
import mimetypes
import uuid
import requests

CREDENTIALS_FILE = "/Users/matt/.claude/gdrive-scalrize-credentials.json"
TOKEN_FILE       = "/Users/matt/.claude/gdrive-scalrize-token.json"
SHARED_DRIVE_NAME = "Scale-Rise & OLC Method"


def refresh_access_token(creds, token):
    resp = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id":     creds["installed"]["client_id"],
        "client_secret": creds["installed"]["client_secret"],
        "refresh_token": token["refresh_token"],
        "grant_type":    "refresh_token",
    })
    if not resp.ok:
        raise RuntimeError(f"Token refresh failed ({resp.status_code}): {resp.text}")
    return resp.json()["access_token"]


def find_shared_drive(access_token):
    resp = requests.get(
        "https://www.googleapis.com/drive/v3/drives",
        headers={"Authorization": f"Bearer {access_token}"},
        params={"pageSize": 100},
    )
    resp.raise_for_status()
    drives = resp.json().get("drives", [])
    for drive in drives:
        if drive["name"] == SHARED_DRIVE_NAME:
            return drive["id"]
    names = [d["name"] for d in drives]
    raise ValueError(f"Shared Drive '{SHARED_DRIVE_NAME}' not found. Available: {names}")


def find_or_create_folder(access_token, name, parent_id, drive_id):
    safe_name = name.replace("'", "\\'")
    resp = requests.get(
        "https://www.googleapis.com/drive/v3/files",
        headers={"Authorization": f"Bearer {access_token}"},
        params={
            "q": f"name='{safe_name}' and '{parent_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false",
            "corpora": "drive",
            "driveId": drive_id,
            "includeItemsFromAllDrives": "true",
            "supportsAllDrives": "true",
            "fields": "files(id,name)",
        },
    )
    resp.raise_for_status()
    files = resp.json().get("files", [])
    if files:
        return files[0]["id"]

    resp = requests.post(
        "https://www.googleapis.com/drive/v3/files",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        params={"supportsAllDrives": "true"},
        json={
            "name": name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_id],
        },
    )
    resp.raise_for_status()
    folder_id = resp.json()["id"]
    print(f"  Created folder: {name}")
    return folder_id


def resolve_folder_path(access_token, folder_path, drive_id):
    parts = [p for p in folder_path.strip("/").split("/") if p]
    current_id = drive_id
    for part in parts:
        current_id = find_or_create_folder(access_token, part, current_id, drive_id)
    return current_id


def find_existing_file(access_token, filename, folder_id, drive_id):
    safe_name = filename.replace("'", "\\'")
    resp = requests.get(
        "https://www.googleapis.com/drive/v3/files",
        headers={"Authorization": f"Bearer {access_token}"},
        params={
            "q": f"name='{safe_name}' and '{folder_id}' in parents and trashed=false",
            "corpora": "drive",
            "driveId": drive_id,
            "includeItemsFromAllDrives": "true",
            "supportsAllDrives": "true",
            "fields": "files(id,name)",
        },
    )
    resp.raise_for_status()
    files = resp.json().get("files", [])
    return files[0]["id"] if files else None


def upload_file(access_token, local_path, folder_id, drive_id):
    filename  = os.path.basename(local_path)
    file_size = os.path.getsize(local_path)
    mime_type, _ = mimetypes.guess_type(local_path)
    if not mime_type:
        mime_type = "application/octet-stream"

    existing_id = find_existing_file(access_token, filename, folder_id, drive_id)

    with open(local_path, "rb") as f:
        file_content = f.read()

    metadata = {"name": filename}
    if not existing_id:
        metadata["parents"] = [folder_id]

    boundary = uuid.uuid4().hex
    body = (
        f"--{boundary}\r\n"
        f"Content-Type: application/json; charset=UTF-8\r\n\r\n"
        f"{json.dumps(metadata)}\r\n"
        f"--{boundary}\r\n"
        f"Content-Type: {mime_type}\r\n\r\n"
    ).encode() + file_content + f"\r\n--{boundary}--".encode()

    if existing_id:
        url    = f"https://www.googleapis.com/upload/drive/v3/files/{existing_id}"
        method = "PATCH"
    else:
        url    = "https://www.googleapis.com/upload/drive/v3/files"
        method = "POST"

    resp = requests.request(
        method,
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": f"multipart/related; boundary={boundary}",
        },
        params={
            "uploadType": "multipart",
            "supportsAllDrives": "true",
            "fields": "id,name,webViewLink",
        },
        data=body,
    )
    resp.raise_for_status()
    result = resp.json()
    action = "Updated" if existing_id else "Uploaded"
    print(f"  {action}: {result['name']} ({file_size // 1024}KB)")
    if "webViewLink" in result:
        print(f"  URL: {result['webViewLink']}")
    return result


def main():
    if len(sys.argv) not in (3, 4):
        print(__doc__)
        sys.exit(1)

    local_file   = sys.argv[1]
    drive_folder = sys.argv[2]

    if not os.path.exists(local_file):
        print(f"Error: file not found: {local_file}")
        sys.exit(1)

    with open(CREDENTIALS_FILE) as f:
        creds = json.load(f)
    with open(TOKEN_FILE) as f:
        token = json.load(f)

    print(f"Refreshing token...")
    access_token = refresh_access_token(creds, token)

    print(f"Locating Shared Drive '{SHARED_DRIVE_NAME}'...")
    drive_id = find_shared_drive(access_token)

    print(f"Resolving path: {drive_folder}")
    folder_id = resolve_folder_path(access_token, drive_folder, drive_id)

    print(f"Uploading: {os.path.basename(local_file)}")
    upload_file(access_token, local_file, folder_id, drive_id)
    print("Done.")


if __name__ == "__main__":
    main()
