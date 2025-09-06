import ssl, socket
def run(target, opts):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((target, 443), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()
                return {"subject": cert.get("subject"), "issuer": cert.get("issuer"), "valid":True}
    except Exception as e:
        return {"error": str(e)}
