import requests
from requests.exceptions import SSLError, ConnectionError

class SSLChecker:
    def check_ssl_handshake(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            print(f"SSL Handshake for {url} is successful.")
        except SSLError as e:
            print(f"SSL Handshake failed for {url}. Error: {e}")
        except ConnectionError as e:
            print(f"Connection error for {url}. Error: {e}")

class CertificatePinningChecker:
    def __init__(self, pinned_certificate_path):
        with open(pinned_certificate_path, 'r') as file:
            self.pinned_certificate = file.read()

    def check_certificate_pinning(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            server_certificate = response.connection.getpeercert(binary_form=True)
            if server_certificate == self.pinned_certificate.encode('utf-8'):
                print(f"Certificate pinning for {url} is successful.")
            else:
                print(f"Certificate pinning failed for {url}.")
        except SSLError as e:
            print(f"SSL Handshake failed for {url}. Error: {e}")
        except ConnectionError as e:
            print(f"Connection error for {url}. Error: {e}")

if __name__ == "__main__":
    url_to_check = "https://nu.nl"

    ssl_checker = SSLChecker()
    ssl_checker.check_ssl_handshake(url_to_check)

    pinned_certificate_path = "path/to/pinned_certificate.pem"
    pinning_checker = CertificatePinningChecker(pinned_certificate_path)
    pinning_checker.check_certificate_pinning(url_to_check)