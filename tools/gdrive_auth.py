#!/usr/bin/env python3
"""
gdrive_auth.py — One-time OAuth setup for Google Drive Shared Drive access.

Run this once per account. It opens a browser, you grant permission,
and it saves a fresh refresh token to the token file.

Usage:
    python3 tools/gdrive_auth.py scalrize    # for ScaleRise Shared Drive
    python3 tools/gdrive_auth.py personal    # for personal Drive
"""

import sys
import json
import webbrowser
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

CONFIGS = {
    "scalrize": {
        "credentials": "/Users/matt/.claude/gdrive-scalrize-credentials.json",
        "token":       "/Users/matt/.claude/gdrive-scalrize-token.json",
        "label":       "ScaleRise Shared Drive (hello@scalrize.com)",
    },
    "personal": {
        "credentials": "/Users/matt/.claude/gdrive-personal-credentials.json",
        "token":       "/Users/matt/.claude/gdrive-personal-token.json",
        "label":       "Personal Drive (matthieu.jammers@gmail.com)",
    },
}

SCOPE       = "https://www.googleapis.com/auth/drive"
REDIRECT    = "http://localhost:8765"
PORT        = 8765

auth_code   = None


class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"<html><body><h2>Auth complete. You can close this tab.</h2></body></html>")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"<html><body><h2>Error: no code received.</h2></body></html>")

    def log_message(self, format, *args):
        pass  # suppress server logs


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in CONFIGS:
        print(__doc__)
        sys.exit(1)

    cfg = CONFIGS[sys.argv[1]]
    print(f"\nAuthenticating: {cfg['label']}")

    with open(cfg["credentials"]) as f:
        creds = json.load(f)["installed"]

    auth_url = (
        "https://accounts.google.com/o/oauth2/auth?"
        + urllib.parse.urlencode({
            "client_id":     creds["client_id"],
            "redirect_uri":  REDIRECT,
            "response_type": "code",
            "scope":         SCOPE,
            "access_type":   "offline",
            "prompt":        "consent",
        })
    )

    print(f"\nOpening browser for Google sign-in...")
    print(f"Make sure to sign in as the correct account.\n")
    webbrowser.open(auth_url)

    print("Waiting for auth callback on http://localhost:8765 ...")
    server = HTTPServer(("localhost", PORT), CallbackHandler)
    server.handle_request()

    if not auth_code:
        print("Error: no auth code received.")
        sys.exit(1)

    print("Exchanging code for tokens...")
    resp = requests.post("https://oauth2.googleapis.com/token", data={
        "code":          auth_code,
        "client_id":     creds["client_id"],
        "client_secret": creds["client_secret"],
        "redirect_uri":  REDIRECT,
        "grant_type":    "authorization_code",
    })
    resp.raise_for_status()
    token_data = resp.json()

    token_file_data = {
        "access_token":  token_data.get("access_token", ""),
        "refresh_token": token_data["refresh_token"],
        "scope":         token_data.get("scope", SCOPE),
        "token_type":    token_data.get("token_type", "Bearer"),
        "expiry_date":   0,
    }

    with open(cfg["token"], "w") as f:
        json.dump(token_file_data, f, indent=2)

    print(f"\nToken saved to: {cfg['token']}")
    print("Setup complete. gdrive_shared_upload.py will now work automatically.")


if __name__ == "__main__":
    main()
