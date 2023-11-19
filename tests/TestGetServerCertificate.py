#This test checks if the retrieval of certificates is working which has impact on first getting the server certificates
#and after that comparing it to the certificate in the communication. (certificate pinning)

import ssl
from urllib.parse import urlparse  # Import urlparse for parsing URLs.

url = "https://tesselaarbv.nl"

# Server address, and convert to ssl readable domain.

parsed_url = urlparse(url)
domain = parsed_url.netloc

serverHost = domain
serverPort = "443"
serverAddress = (serverHost, serverPort)

 

# Retrieve the server certificate in PEM format.

cert = ssl.get_server_certificate(serverAddress)

print(f"This printed certificate comes from: {domain}.")
print(cert)