import socket

host = "127.0.0.1"
porta = 1060

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, porta))
servidor.listen(5)

print("Servidor iniciado na porta: ", porta)

while True:
    cliente, endereco = servidor.accept()
    print(f"Conectado com {endereco}")
    dados = cliente.recv(1024).decode()
    print(f"Recebido: {dados}")
    cliente.send("mensagem recebida".encode())
    cliente.close()