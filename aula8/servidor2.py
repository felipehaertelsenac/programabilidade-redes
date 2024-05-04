import socket
import os

host = "127.0.0.1"
porta = 1060

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((host, porta))

print('Iniciando escuta no servidor...')

with open('dados_recebidos.txt', 'wb') as arq:
    try:
        while True:

            dados, endereco = servidor.recvfrom(1024)

            if not dados:
                break

            arq.write(dados)
            if len(dados) < 1024:
                break
    finally:
        print("Transferencia concluída")
        servidor.close()