import socket
import time

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.settimeout(2.0)

cliente.connect((host, porta))

enviados = 0
recebidos = 0

for i in range(10000):
    start_time = time.time()
    mensagem = f'Ping {i} {start_time}'.encode()
    cliente.send(mensagem)
    enviados += 1

    try: 
        dados, endereco = cliente.recvfrom(1024)
        end_time = time.time()
        latencia = (end_time - start_time) * 1000
        print(f"Ping {i}: Latência de {latencia:.2f} ms")
        recebidos += 1
    except socket.timeout:
        print(f"Ping {i}: Tempo resposta excedido")

print(f"\nPacotes enviados: {enviados}")
print(f"Pacotes recebidos: {recebidos}")
print(f"Perda de pacotes: {(1 - recebidos / enviados) * 100:.2f}%")

cliente.close()