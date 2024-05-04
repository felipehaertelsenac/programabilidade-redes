import socket


host = "127.0.0.1"
porta = 1060

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((host, porta))

print('Iniciando escuta no servidor...')

while True:

    dados, endereco = servidor.recvfrom(1024)

    servidor.sendto(dados, endereco)
    