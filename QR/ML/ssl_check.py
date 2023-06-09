import ssl
import socket
import pandas as pd

def STL(path = 'url_t.csv'):
    url = pd.read_csv(path)
    url = url['url'].to_string()
    hostname = url.split("//")[-1].split("/")[0]
    port = 443  # HTTPS port

    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            certificate = ssock.getpeercert()
            # print(certificate)

    import datetime

    not_before_str = certificate["notBefore"]
    not_after_str = certificate["notAfter"]
    not_before = datetime.datetime.strptime(not_before_str, "%b %d %H:%M:%S %Y %Z")
    not_after = datetime.datetime.strptime(not_after_str, "%b %d %H:%M:%S %Y %Z")
    current_time = datetime.datetime.now()

    if not_before < current_time < not_after:
        # print("Certificate is valid")
        return 1
    else:
        # print("Certificate is invalid")
        return 0
