import socket
import time

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.settimeout(1)

start_time = time.time()
mensagem = f"ping"
cliente.sendto(mensagem.encode(), (host, porta))

try:
    dados, endereco = cliente.recvfrom(1024)
    end_time = time.time()
    tempo = (end_time - start_time) * 1000
    print(f"{dados.decode()} {tempo:.2f} ms")
except socket.timeout:
    print("Tempo esgotado")

cliente.close()

