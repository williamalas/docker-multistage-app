from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok"}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))

if __name__ == "__main__":
    port = 8081
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"listening on {port}")
    server.serve_forever()
