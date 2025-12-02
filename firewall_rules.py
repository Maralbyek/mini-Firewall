# Pre-registered allowed IPs and their allowed ports
allowed_rules = {
    "192.168.1.10": [22, 80, 443],
    "10.0.0.5": [8080, 3306],
    "172.16.0.7": [53, 443]
}

def check_connection(ip, port):
    # Check if IP exists
    if ip not in allowed_rules:
        return f"[ALERT] Suspicious IP detected: {ip} is NOT registered!"

    # Check if port is allowed for that IP
    if port not in allowed_rules[ip]:
        return f"[BLOCKED] {ip}:{port} is NOT permitted!"

    # Valid IP and port
    return f"[ALLOWED] {ip}:{port} connection approved."
