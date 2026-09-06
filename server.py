import os
import sys
import json
import base64
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

import main as core

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_HTML_PATH = os.path.join(BASE_DIR, "index.html")
INPUT_DIR = os.path.join(BASE_DIR, "ss")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

CURRENT_DOCX = os.path.join(OUTPUT_DIR, core.OUTPUT_DOCX_NAME)
CURRENT_PDF = os.path.join(OUTPUT_DIR, core.OUTPUT_PDF_NAME)


class ScreenshotServerHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # Clean minimalist console logs
        sys.stdout.write(f"[Server] {self.command} {self.path} -> {args[1]}\n")
        sys.stdout.flush()

    def send_json(self, status_code: int, data: dict):
        response_bytes = json.dumps(data).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(response_bytes)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path in ('/', '/index.html'):
            if os.path.exists(INDEX_HTML_PATH):
                with open(INDEX_HTML_PATH, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404, "index.html not found")

        elif path == '/logo.png':
            logo_path = os.path.join(BASE_DIR, "logo.png")
            if os.path.exists(logo_path):
                with open(logo_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'image/png')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
        elif path in ('/favicon.png', '/favicon.ico'):
            fav_name = "favicon.png" if path == '/favicon.png' else "favicon.ico"
            fav_path = os.path.join(BASE_DIR, fav_name)
            if os.path.exists(fav_path):
                with open(fav_path, 'rb') as f:
                    content = f.read()
                content_type = 'image/png' if fav_name.endswith('.png') else 'image/x-icon'
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404, "favicon not found")

        elif path == '/api/download/pdf':
            global CURRENT_PDF
            if os.path.exists(CURRENT_PDF):
                with open(CURRENT_PDF, 'rb') as f:
                    content = f.read()
                filename = os.path.basename(CURRENT_PDF)
                self.send_response(200)
                self.send_header('Content-Type', 'application/pdf')
                self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404, "PDF output not found")

        elif path == '/api/download/docx':
            global CURRENT_DOCX
            if os.path.exists(CURRENT_DOCX):
                with open(CURRENT_DOCX, 'rb') as f:
                    content = f.read()
                filename = os.path.basename(CURRENT_DOCX)
                self.send_response(200)
                self.send_header('Content-Type', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404, "DOCX output not found")

        elif path == '/api/status':
            ss_count = len(core.get_sorted_images(INPUT_DIR)) if os.path.exists(INPUT_DIR) else 0
            self.send_json(200, {
                "status": "ok",
                "ss_count": ss_count,
                "has_pdf": os.path.exists(CURRENT_PDF),
                "has_docx": os.path.exists(CURRENT_DOCX)
            })

        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/api/generate':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                if content_length == 0:
                    self.send_json(400, {"error": "Empty payload"})
                    return

                body = self.rfile.read(content_length)
                payload = json.loads(body.decode('utf-8'))

                images_data = payload.get('images', [])
                doc_name = payload.get('docName', 'arranged_screenshots').strip() or 'arranged_screenshots'
                show_captions = payload.get('showCaptions', True)
                page_format = payload.get('pageFormat', 'letter')

                if not images_data:
                    self.send_json(400, {"error": "No images provided"})
                    return

                os.makedirs(INPUT_DIR, exist_ok=True)
                os.makedirs(OUTPUT_DIR, exist_ok=True)

                # Clear old screenshot files from ss folder
                for f in os.listdir(INPUT_DIR):
                    if not f.startswith('.'):
                        try:
                            os.remove(os.path.join(INPUT_DIR, f))
                        except Exception:
                            pass

                saved_image_paths = []

                # Save incoming images to ss/ folder in designated order
                for idx, img_info in enumerate(images_data, 1):
                    raw_name = img_info.get('name', f'screenshot_{idx}.png')
                    # Sanitize filename
                    safe_name = "".join(c for c in raw_name if c.isalnum() or c in "._- ")
                    base_root, ext = os.path.splitext(safe_name)
                    if not ext:
                        ext = '.png'

                    # Ensure unique ordered filename
                    filename = f"{idx:02d}_{base_root}{ext}"
                    file_path = os.path.join(INPUT_DIR, filename)

                    data_url = img_info.get('dataUrl', '')
                    if ',' in data_url:
                        encoded = data_url.split(',', 1)[1]
                    else:
                        encoded = data_url

                    img_bytes = base64.b64decode(encoded)
                    with open(file_path, 'wb') as f:
                        f.write(img_bytes)

                    saved_image_paths.append(file_path)

                # Destination output paths
                global CURRENT_DOCX, CURRENT_PDF
                docx_filename = f"{doc_name}.docx"
                pdf_filename = f"{doc_name}.pdf"
                CURRENT_DOCX = os.path.join(OUTPUT_DIR, docx_filename)
                CURRENT_PDF = os.path.join(OUTPUT_DIR, pdf_filename)

                # Generate Word DOCX
                core.create_docx(saved_image_paths, CURRENT_DOCX, show_captions=show_captions)

                # Generate PDF
                core.create_pdf(saved_image_paths, CURRENT_PDF, show_captions=show_captions, page_format=page_format)

                self.send_json(200, {
                    "success": True,
                    "count": len(saved_image_paths),
                    "docx_name": docx_filename,
                    "pdf_name": pdf_filename,
                    "pdf_url": "/api/download/pdf",
                    "docx_url": "/api/download/docx",
                    "ss_folder": "ss/",
                    "output_folder": "output/"
                })

            except Exception as e:
                self.send_json(500, {"error": str(e)})

        elif path == '/api/clear':
            try:
                # Clear images in ss/
                if os.path.exists(INPUT_DIR):
                    for f in os.listdir(INPUT_DIR):
                        if not f.startswith('.'):
                            try:
                                os.remove(os.path.join(INPUT_DIR, f))
                            except Exception:
                                pass

                # Clear compiled files in output/
                if os.path.exists(OUTPUT_DIR):
                    for f in os.listdir(OUTPUT_DIR):
                        if not f.startswith('.'):
                            try:
                                os.remove(os.path.join(OUTPUT_DIR, f))
                            except Exception:
                                pass

                self.send_json(200, {"success": True, "message": "Workspace cleared"})
            except Exception as e:
                self.send_json(500, {"error": str(e)})

        else:
            self.send_error(404, "Endpoint not found")


def run_server(port: int = 5050, open_browser: bool = True):
    server_address = ('', port)
    try:
        httpd = HTTPServer(server_address, ScreenshotServerHandler)
    except OSError:
        # Fallback to next available port if 5050 is occupied
        port = 5051
        server_address = ('', port)
        httpd = HTTPServer(server_address, ScreenshotServerHandler)

    url = f"http://localhost:{port}"
    print("\n" + "=" * 50)
    print(" SnapStitch — Minimalist Document Compiler")
    print("=" * 50)
    print(f" • Running at:    {url}")
    print(f" • Screenshot dir: {INPUT_DIR}")
    print(f" • Output dir:     {OUTPUT_DIR}")
    print(" • Press Ctrl+C to stop the server.")
    print("=" * 50 + "\n")

    if open_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down.")
        httpd.server_close()


if __name__ == "__main__":
    run_server()
