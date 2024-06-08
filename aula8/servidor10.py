import socket

host = "127.0.0.1"
porta = 1060

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((host, porta))
print("Servidor mensagem iniciado na porta", porta)

while True:
    dados, endereco = servidor.recvfrom(1024)
    
    with open("mensagens.txt", "r") as arq:
        num = int(arq.readline())

    num += 1

    response = f"Mensagem de número: {num} recebida."

    servidor.sendto(response.encode(), endereco)
    
    with open("mensagens.txt", "w") as arq:
        arq.write(str(num))