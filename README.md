# Web Raccoon - NACTCH Recon Toolkit

![Web Raccoon](web-raccoon.png)

## Overview

Web Raccoon is a professional and intuitive command-line reconnaissance toolkit designed for gathering information about any domain. It provides DNS lookups, subdomain enumeration, WHOIS information, open ports detection, and TLS certificate details, and outputs results in both JSON and HTML formats.

**Disclaimer:** Use this toolkit only on domains and networks for which you have explicit written permission. Unauthorized scanning or probing of systems you do not own is illegal.

## Features

* **DNS Lookup:** Resolve A, AAAA, MX, NS, and TXT records.
* **Subdomain Enumeration:** Passive scanning to discover subdomains.
* **WHOIS Information:** Retrieve domain registration details.
* **Open Ports Detection:** Checks common ports (FTP, HTTP, HTTPS, SMTP).
* **TLS Certificate Details:** Issuer, common name, SAN, validity.
* **Professional CLI:** Colorful output, live logs.
* **Reports:** Generates JSON and HTML reports for easy viewing and sharing.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nacttch/web-raccoon.git
cd web-raccoon
```

2. (Optional) Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

1. Enter the target domain (e.g., `example.com`).
2. Choose the type of checks to run or select `0` for all checks.
3. Wait for the toolkit to complete the reconnaissance.
4. View reports in the `report/` directory (`report.json` and `report.html`).

### CLI Example

```

▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·   ▄▄▄   ▄▄▄·  ▄▄·  ▄▄·              ▐ ▄ 
██· █▌▐█▀▄.▀·▐█ ▀█▪  ▀▄ █·▐█ ▀█ ▐█ ▌▪▐█ ▌▪ ▄█▀▄  ▄█▀▄ •█▌▐█
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄  ▐▀▀▄ ▄█▀▀█ ██ ▄▄██ ▄▄▐█▌.▐▌▐█▌.▐▌▐█▐▐▌
▐█▌██▐█▌▐█▄▄▌██▄▪▐█  ▐█•█▌▐█▪ ▐▌▐███▌▐███▌▐█▌.▐▌▐█▌.▐▌██▐█▌
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀   .▀  ▀ ▀  ▀ ·▀▀▀ ·▀▀▀  ▀█▄▀▪ ▀█▄▀▪▀▀ █▪

                         by nacttch

--------------------------------------------------
Enter target URL: https://example.com
Choose test:
0 - Run ALL checks
1 - DNS Lookup
2 - Subdomain Enumeration
3 - WHOIS
4 - Open Ports
5 - TLS Certificate
Choice: 0
```

## Report Output

Reports are saved in the `report/` folder:

* `report.json` — machine-readable JSON report.
* `report.html` — visually formatted HTML report.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
