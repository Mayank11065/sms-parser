#!/usr/bin/env python
"""Simple HTTP server"""

from http.server import BaseHTTPRequestHandler

# HTTPRequestHandler class

class TestHTTPServerRequestHandler(BaseHTTPRequestHandler):
    """HTTP server Class"""
    def do_GET(self):
        """GET Function"""
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
