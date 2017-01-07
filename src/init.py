"""Starting point of the module"""
from http.server import HTTPServer
import service
from constants import Constants

def run():
    """Starting server"""
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = (Constants.SERVER_URL, Constants.SERVER_PORT)
    httpd = HTTPServer(server_address, service.TestHTTPServerRequestHandler)
    print('running server...')
    httpd.serve_forever()

run()
