def scan_ports(host, ports):
    for ports in ports:
        print(f"Escaneando porta {ports} em {host}")

scan_ports("192.168.1.1", [22, 80, 443])