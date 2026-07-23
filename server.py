import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✅ Server running at http://localhost:{PORT}")
    print(f"🌐 Open your browser and go to the URL above")
    print(f"⏹️  Press Ctrl+C to stop")
    httpd.serve_forever()
