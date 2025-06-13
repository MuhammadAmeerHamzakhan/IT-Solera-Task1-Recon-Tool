import socket


def get_target_ip(url):
    try:
        target_ip = socket.gethostbyname(url)
        return target_ip
    except socket.error as err:
        print(f"Error: {err}")

