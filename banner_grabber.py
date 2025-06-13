import socket
import ssl
import argparse
from datetime import datetime


def banner_grab(ip, port):
    try:
        # Create a TCP connection
        s = socket.create_connection((ip, port), timeout=3)

        # Wrap in SSL if it's HTTPS (port 443)
        if port == 443:
            context = ssl._create_unverified_context()

            s = context.wrap_socket(s, server_hostname=ip)

        # Send minimal HTTP request
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")

        # Receive and decode banner
        banner = s.recv(4096).decode(errors="ignore")
        s.close()

        return f"[+] Banner for {ip}:{port}\n{banner}"

    except socket.timeout:
        return f"[-] Timeout on {ip}:{port}"
    except Exception as e:
        return f"[-] Error on {ip}:{port}: {e}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom Banner Grabbing Tool (Supports HTTP/HTTPS)")
    parser.add_argument("--banner", action="store_true", help="Enable banner grabbing")
    parser.add_argument("--ip", type=str, help="Target IP address")
    parser.add_argument("--ports", nargs="+", type=int, help="List of ports to scan (e.g., 80 443 21)")

    args = parser.parse_args()

    if args.banner:
        if not args.ip or not args.ports:
            print("[-] Please provide both --ip and --ports with --banner flag")
        else:
            print(f"\n--- Performing Banner Grabbing on {args.ip} ---\n")
            for port in args.ports:
                print(f"Scanning {args.ip}:{port}...")
                result = banner_grab(args.ip, port)
                print("[Result]:\n" + result)

                # Save to report
                with open("banner_report.txt", "a") as report:
                    report.write(f"--- {datetime.now()} ---\n")
                    report.write(result + "\n\n")
            print("\n[+] All banners saved to banner_report.txt")
    else:
        print("[-] Please use --banner flag to enable banner grabbing.")
