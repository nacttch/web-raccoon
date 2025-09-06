
from modules import dns_mod, subdomains_mod, whois_mod, ports_mod, tls_mod
from utils import color, utc_now
import json, os

BANNER = r"""
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·   ▄▄▄   ▄▄▄·  ▄▄·  ▄▄·              ▐ ▄ 
██· █▌▐█▀▄.▀·▐█ ▀█▪  ▀▄ █·▐█ ▀█ ▐█ ▌▪▐█ ▌▪ ▄█▀▄  ▄█▀▄ •█▌▐█
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄  ▐▀▀▄ ▄█▀▀█ ██ ▄▄██ ▄▄▐█▌.▐▌▐█▌.▐▌▐█▐▐▌
▐█▌██▐█▌▐█▄▄▌██▄▪▐█  ▐█•█▌▐█▪ ▐▌▐███▌▐███▌▐█▌.▐▌▐█▌.▐▌██▐█▌
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀   .▀  ▀ ▀  ▀ ·▀▀▀ ·▀▀▀  ▀█▄▀▪ ▀█▄▀▪▀▀ █▪

                         by nactch
"""

def interactive():
    print(BANNER)
    target = input("Target (e.g. https://example.com or example.com): ").strip()
    while True:
        print("[1] DNS Lookup")
        print("[2] Subdomain Enumeration")
        print("[3] WHOIS Info")
        print("[4] Port Scan")
        print("[5] TLS Certificate Info")
        print("[6] Run All Checks")
        print("[0] Exit")
        choice = input("Select option: ").strip()
        report = {"target": target, "timestamp": utc_now(), "findings":[]}
        if choice=="1":
            report["dns"] = dns_mod.run(target, {})
        elif choice=="2":
            report["subdomains"] = subdomains_mod.run(target, {})
        elif choice=="3":
            report["whois"] = whois_mod.run(target, {})
        elif choice=="4":
            report["open_ports"] = ports_mod.run(target, {})
        elif choice=="5":
            report["tls"] = tls_mod.run(target, {})
        elif choice=="6":
            report["dns"] = dns_mod.run(target, {})
            report["subdomains"] = subdomains_mod.run(target, {})
            report["whois"] = whois_mod.run(target, {})
            report["open_ports"] = ports_mod.run(target, {})
            report["tls"] = tls_mod.run(target, {})
        elif choice=="0":
            break
        else:
            print("Invalid choice")
            continue
        fn = "report.json"
        with open(fn,"w") as f: json.dump(report,f,indent=2)
        print("Saved report to",fn)

if __name__=="__main__":
    interactive()
