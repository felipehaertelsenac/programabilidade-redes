import socket
import sys

def server():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    servidor.bind((host, porta))

    print('Iniciando escuta no servidor...')

    dados, endereco = servidor.recvfrom(1024)

    print("Recebido:", dados.decode(), "de", endereco)

    servidor.sendto(dados, endereco)

    servidor.close()

def client():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    cliente.connect((host, porta))

    mensagem = "Testando o servidor!"

    cliente.send(mensagem.encode())

    dados, endereco = cliente.recvfrom(1024)

    print("Resposta do servidor:", dados.decode())

    cliente.close()

if __name__ == '__main__':
    host = "127.0.0.1"
    porta = 1060
    if sys.argv[1] == 'servidor':
        server()
    elif sys.argv[1] == 'cliente':
        client()

