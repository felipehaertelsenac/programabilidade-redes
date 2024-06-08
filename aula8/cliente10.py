import socket

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem = input("Digite sua mensagem (digite 'fim' para sair): ")
    if mensagem.lower() == 'sair':
        break

    cliente.sendto(mensagem.encode(), (host, porta))
    dados, endereco = cliente.recvfrom(1024)

    print(dados.decode())

   
cliente.close()
        