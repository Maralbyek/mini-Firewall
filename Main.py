from firewall_rules import check_connection

def main():
    print("=== MINI FIREWALL SECURITY CHECK ===")

    ip = input("Enter IP address: ").strip()
    port = int(input("Enter Port number: ").strip())

    result = check_connection(ip, port)
    print(result)

if __name__ == "__main__":
    main()
