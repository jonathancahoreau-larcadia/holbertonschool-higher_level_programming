#!/usr/bin/python3

"""Simple HTTP server example using Python's built-in http.server.

This module defines a minimal API server with several GET endpoints:

- /       : plain text greeting
- /data   : example JSON payload
- /status : plain text health check
- /info   : JSON metadata about the server

Run the script with:
    python3 task_03_http_server.py

The server listens on port 8000 by default.
"""

import http.server
import json


class Serveur(http.server.BaseHTTPRequestHandler):
    """HTTP request handler for the example REST API."""
    def do_GET(self):
        """Handle GET requests for the example API endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            data_json = json.dumps(data)
            self.wfile.write(data_json.encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            status_message = "OK".encode()
            self.wfile.write(status_message)
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_message = {
                "version": "1.0", "description":
                "A simple API built with http.server"}
            info = json.dumps(info_message).encode()
            self.wfile.write(info)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, Serveur)
    httpd.serve_forever()
