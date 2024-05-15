from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the HTML content with CSS styles
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello, world!</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f7f7f7;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    h1, h2 {
      color: #333;
      font-size: 36px;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>Hello, world!</h1>
  <h2>This is a subheading 1</h2>
  <h2>This is a subheading 2</h2>
</body>
</html>
"""

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_CONTENT.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on {addr}:{port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run(addr="0.0.0.0", port=8000)
