import socket

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servico = input("Informe o servico desejado: ")
        
cliente.sendto(servico.encode(), (host, porta))

dados, endereco = cliente.recvfrom(1024)
print(f"Resposta do servidor: {dados.decode()}")
