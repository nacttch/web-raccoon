import socket
def run(target, opts):
    open_ports=[]
    for port in [21,22,25,53,80,443,8080]:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((target,port))
            open_ports.append({"port":port,"open":True})
            s.close()
        except:
            pass
    return open_ports
