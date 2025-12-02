allowed_rules = {
    "192.168.1.10": [22, 80, 443],
    "10.0.0.5": [8080, 3306],
    "172.16.0.7": [53, 443]
}

def check_connection(ip, port):
    if ip not in allowed_rules:
        return f"[ALERT] Suspicious IP detected: {ip} is NOT registered!"
        
    if port not in allowed_rules[ip]:
        return f"[BLOCKED] {ip}:{port} is NOT permitted!"
        
    return f"[ALLOWED] {ip}:{port} connection approved."

