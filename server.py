"""
🥽 STEAM FRAME VR VIDEO BROWSER LOCAL SERVER
Hosts the WebXR VR Video Browser POC on http://localhost:8080
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8080
DIRECTORY = Path(r"C:\Users\Vivian\Desktop\DreamLLM\steam_frame_vr_browser")

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

def run_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print("[STEAM FRAME VR BROWSER SERVER ONLINE]")
        print(f"[*] Local WebXR URL: http://localhost:{PORT}")
        print(f"[*] Serving files from: {DIRECTORY}\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Server stopped.")

if __name__ == "__main__":
    run_server()
