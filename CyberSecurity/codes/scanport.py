import socket

# Função para escanear uma porta
def scan_port(ip, port):
    try:
        # Cria um socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Tempo máximo de resposta
        s.connect((ip, port))
        print(f"[+] Porta {port} aberta!")
        s.close()
    except:
        print(f"[-] Porta {port} fechada.")

# Scanner básico para as 100 primeiras portas
ip_alvo = input("Digite o IP alvo: ")
for porta in range(1, 101):
    scan_port(ip_alvo, porta)
