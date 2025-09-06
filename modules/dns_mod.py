import socket
def run(target, opts):
    try:
        ip = socket.gethostbyname(target)
        return {"resolved_ips":[ip], "findings":[]}
    except: return {"resolved_ips":[], "findings":["Could not resolve domain"]}
