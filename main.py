import argparse
import ip
import whoislookup
import openports
import subdomain
import banner_grabber
import tech_detect
import dns_enum  


def main():
    parser = argparse.ArgumentParser(description="IT SOLERA Task 1 - Recon Tool")
    parser.add_argument("--ip", type=str, help="Target domain or IP")
    parser.add_argument("--whois", action="store_true", help="Perform WHOIS lookup")
    parser.add_argument("--ports", nargs="+", type=int, help="Scan open ports (e.g., 80 443)")
    parser.add_argument("--subdomains", action="store_true", help="Find subdomains")
    parser.add_argument("--banner", action="store_true", help="Perform banner grabbing")
    parser.add_argument("--detectech", action="store_true", help="Detect technologies using WhatWeb via WSL")
    parser.add_argument("--dnsenum", action="store_true", help="Enumerate DNS records")  # ← NEW FLAG

    args = parser.parse_args()

    if not args.ip:
        print("[-] Please provide a target using --ip")
        return

    target_ip = ip.get_target_ip(args.ip)
    print(f"Target IP: {target_ip}\n")

    if args.whois:
        print("[+] Performing WHOIS lookup...")
        print(whoislookup.target_whois(args.ip))

    if args.ports and not args.banner:
        print("[+] Performing port scan...")
        open_ports_result = openports.get_openport(args.ip)
        if open_ports_result:
            print("Open Ports:", ", ".join(open_ports_result))
        else:
            print("No open ports found.")

    if args.subdomains:
        print("[+] Finding subdomains...")
        subdomains = subdomain.getSubdomains(args.ip)
        if subdomains:
            for dom in subdomains:
                print(f"* {dom}")
        else:
            print("No subdomains found.")

    if args.banner:
        ports_to_scan = args.ports if args.ports else [80, 443]
        print(f"[+] Performing banner grabbing on {target_ip} ports {ports_to_scan}")
        for port in ports_to_scan:
            result = banner_grabber.banner_grab(target_ip, port)
            print(result)
            with open("banner_report.txt", "a") as report:
                report.write(f"\n--- {target_ip}:{port} ---\n")
                report.write(result + "\n")

    if args.detectech:
        print(f"[+] Detecting technologies for {args.ip}...")
        detect_result = tech_detect.scan_website(f"https://{args.ip}")
        if detect_result.returncode == 0:
            print(detect_result.stdout)
        else:
            print(detect_result.stderr)

    if args.dnsenum:
        print(f"[+] Enumerating DNS records for {args.ip}...")
        dns_enum.get_dns_records(args.ip)


if __name__ == "__main__":
    main()
