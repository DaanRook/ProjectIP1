#This piece of code is used to simulate an earlier retrieved server certificate.

import ssl

def get_server_certificate(server_host, server_port):
    server_address = (server_host, server_port)

    try:
        # Retrieve the server certificate in PEM format
        cert = ssl.get_server_certificate(server_address)
        return cert
    except ssl.SSLError as e:
        return f"Error: {e}"

def write_certificate_to_file(cert, filename):
    try:
        with open(filename, 'w') as file: # Write your specified URL servercertificate to pem file.
            file.write(cert)
        return f"Certificate written to {filename} successfully."
    except Exception as e:
        return f"Error writing to file: {e}"

if __name__ == "__main__":
    server_host = "tesselaarbv.nl" # Specify your domain here. (not URL )
    server_port = 443  # Specify server port so ssl can understand.

    server_certificate = get_server_certificate(server_host, server_port)

    if "Error" in server_certificate:
        print(f"Failed to retrieve server certificate: {server_certificate}")
    else:
        # Write the server certificate to a file
        result = write_certificate_to_file(server_certificate, "server_certificate.pem")
        print(result)