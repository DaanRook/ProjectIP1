import ssl
import requests
from requests.exceptions import SSLError, ConnectionError
from urllib.parse import urlparse  # Import urlparse for parsing URLs.
import socket
    
def check_ssl_handshake(URL):  # SSL version added after deadline :(
                               # Made a mistake/oversight
    # Extract the domain from the URL.
    parsed_url = urlparse(URL)
    domain = parsed_url.netloc
    port = "443"

    try:
        # Create an SSL context
        context = ssl.create_default_context()

        # Wrap the socket with SSL
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                print("SSL handshake successful")
                print("Cipher: {}".format(ssock.cipher()))
                print("SSL Version: {}".format(ssock.version()))
                return ssock  # Return the SSL socket
    except ssl.SSLError as e:
        print("SSL Handshake failed:", e)
        return None

def check_certificate_pinning(url, pinned_certificate_path):  
    ssl_socket = check_ssl_handshake(url)                     

    if ssl_socket:
        try:
            # Extract the domain from the URL.
            parsed_url = urlparse(url)
            domain = parsed_url.netloc

            serverPort = "443"
            serverHost = domain
            serverAddress = (serverHost, serverPort)

            # Obtain the server certificate
            cert = ssl.get_server_certificate(serverAddress)

            with open(pinned_certificate_path, 'r') as file:
                pinned_certificate = file.read()

            # Checks if the server certificate and the previous retrieved one are the same.
            # (principle of certificate pinning)
            if cert == pinned_certificate:
                print(f"Certificate pinning for {url} is successful.")
            else:
                print(f"Certificate pinning failed for {url}.")
        except SSLError as e:
            print(f"SSL Handshake failed for {url}. Error: {e}")
        except ConnectionError as e:
            print(f"Connection error for {url}. Error: {e}")

if __name__ == "__main__":
    url_to_check = "https://tesselaarbv.nl"  # Specify the website u want to check here. https://..
    pinned_certificate_path = "server_certificate.pem"  # Specify the correct path to pem file.

    check_certificate_pinning(url_to_check, pinned_certificate_path)