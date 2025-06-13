# 🔍 IT SOLERA Offensive Security Internship - Task 1 Offensive Team Sigma

## 🛠️ Final Reconnaissance Tool (Flag-Based CLI)

This is a complete, modular Python-based reconnaissance tool developed by our team Offensive Team Sigma as part of **Task 1** for the **IT SOLERA Offensive Security Internship 2025**.

The tool is designed to perform independent recon scans using **command-line flags**, making it flexible, scriptable, and suitable for automation. Each module is implemented in its own file and integrated into a unified `main.py` script.

---

## 📦 Features & Modules

### ✅ WHOIS Lookup

Command: `--whois`

* Performs WHOIS record lookup for a given domain.
* Returns domain registrar, expiration, creation date, and contact info.

### ✅ Subdomain Enumeration

Command: `--subdomains`

* Enumerates subdomains for the target domain using a predefined wordlist.

### ✅ Port Scanning

Command: `--ports 80 443`

* Scans target for open TCP ports.
* Can be used independently or with banner grabbing.

### ✅ Banner Grabbing

Command: `--banner --ports 80 443`

* Retrieves service banners from specified open ports.
* Supports HTTP/HTTPS (with SSL support).
* Saves results in `banner_report.txt`

### ✅ DNS Enumeration

Command: `--dns`

* Performs basic DNS record enumeration (A, MX, TXT, NS).
* Uses `dnspython` for querying.

### ✅ Technology Detection

Command: `--tech`

* Detects backend technologies using HTTP headers and responses.
* Identifies CMS, server type, frameworks (basic fingerprinting).

---

## 🚀 Example Usage

```bash
python main.py --ip google.com --whois
python main.py --ip google.com --subdomains
python main.py --ip google.com --ports 80 443
python main.py --ip google.com --banner --ports 80 443
python main.py --ip google.com --dns
python main.py --ip google.com --tech
```

---

## 🧠 Technologies Used

* `socket`, `ssl`, `requests`, `argparse`
* `dnspython`, `python-whois`
* CLI-based architecture for modular scanning

---

## 👨‍💻 Developed By

Offensive Team Sigma

---

## 📝 Notes

* All modules are designed to be called independently.
* Easily extendable for more recon techniques or automation.
* Ideal for beginners learning real-world recon logic.

---

> ⚙️ Built with purpose. Tested with passion. Delivered with collaboration. - IT SOLERA Interns 2025 💻
