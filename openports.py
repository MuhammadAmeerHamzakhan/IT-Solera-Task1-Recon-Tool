import socket
from urllib.parse import urlparse

def get_openport(url):
    ports = {
        'http': 80,
        'https': 443,
        'ftp': 21,
        'ftps': 990,
        'ssh': 22,
        'smtp': 25,
        'pop3': 110,
        'imap': 143,
        'dns': 53,
        'mysql': 3306,
        'postgresql': 5432,
        'rdp': 3389,
        'mongodb': 27017
    }

    def ip_addresses(url):
        try:
            ais = socket.getaddrinfo(url, 0, 0, 0, 0)
            ip_addresses = list(set(result[-1][0] for result in ais))
            return ip_addresses
        except socket.error as e:
            print(f'[!] Error resolving domain: {e}')
            return []

    def port_scanner(ip, scheme):
        open_ports = set()
        default_port = ports.get(scheme)
        if default_port:
            open_ports.add(str(default_port))

        for port in ports.values():
            try:
                sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sck.settimeout(1)
                result = sck.connect_ex((ip, port))
                if result == 0:
                    open_ports.add(str(port))
                sck.close()
            except:
                continue

        return sorted(open_ports, key=int)

    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc or parsed_url.path  # Handle both full and raw domains
    scheme = parsed_url.scheme or 'http'

    ip_list = ip_addresses(domain_name)
    if not ip_list:
        return []

    return port_scanner(ip_list[0], scheme)
