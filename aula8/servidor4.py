import socket


host = "127.0.0.1"
porta = 1060

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((host, porta))

print('Servidor de chat iniciado na porta', porta)

clientes = []

while True:

    dados, endereco = servidor.recvfrom(1024)

    if endereco not in clientes:
            clientes.append(endereco)  
            print(f"Novo cliente conectado: {endereco}")

    for cliente in clientes:
        if cliente != endereco:
            servidor.sendto(dados, endereco)
        else:
            servidor.sendto('Mensagem enviada'.encode(), endereco)
    