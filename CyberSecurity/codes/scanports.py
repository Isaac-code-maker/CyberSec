import socket
import threading

# Função para escanear uma porta específica
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Porta {port} está aberta")
        sock.close()
    except Exception as e:
        print(f"Erro ao escanear a porta {port}: {e}")

# Função para escanear um intervalo de portas
def scan_ports(ip, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    alvo = input("Digite o endereço IP ou domínio do alvo: ")
    porta_inicial = int(input("Digite a porta inicial do intervalo: "))
    porta_final = int(input("Digite a porta final do intervalo: "))

    print(f"Escaneando {alvo} de {porta_inicial} até {porta_final}...")
    scan_ports(alvo, porta_inicial, porta_final)
    print("Scan completo.")
