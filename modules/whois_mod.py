from utils import do_whois
def run(target, opts):
    return {"whois": do_whois(target)}
