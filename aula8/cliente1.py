import socket

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cliente.connect((host, porta))

mensagem = "Testando o servidor!"

cliente.send(mensagem.encode())

dados, endereco = cliente.recvfrom(1024)

print("Resposta do servidor:", dados.decode())

cliente.close()