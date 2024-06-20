import socket

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, porta))

cliente.send("Teste de envio TCP!".encode())
dados = cliente.recv(1024).decode()
print(f"Recebido resposta do servidor: {dados}")

cliente.close()