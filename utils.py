
import socket
import ssl
from datetime import datetime, timezone

def do_whois(domain):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect(("whois.iana.org", 43))
        s.send((domain + "\r\n").encode())
        response = b""
        while True:
            d = s.recv(4096)
            if not d:
                break
            response += d
        s.close()
        data = response.decode(errors="ignore")
        ref = None
        for line in data.splitlines():
            if line.lower().startswith("refer:"):
                ref = line.split(":")[1].strip()
                break
        if ref:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((ref, 43))
            s.send((domain + "\r\n").encode())
            response = b""
            while True:
                d = s.recv(4096)
                if not d:
                    break
                response += d
            s.close()
            data = response.decode(errors="ignore")
        return {"raw": data}
    except Exception as e:
        return {"error": str(e)}

def color(text, col="cyan"):
    return text

def utc_now():
    return datetime.now(timezone.utc).isoformat()
