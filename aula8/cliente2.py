import socket

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cliente.connect((host, porta))

try:
    with open('dados_enviados.txt', 'rb') as arq:
        while True:

            data = arq.read(1024)
            if not data:
                break

            cliente.send(data)
finally:
    print("Arquivo enviado completamente")
    cliente.close()
