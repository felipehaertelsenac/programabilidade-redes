import socket

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        mensagem = input("Digite sua mensagem ou 'fim' para sair: ")
        if mensagem.lower() == 'fim':
            break

        cliente.sendto(mensagem.encode(), (host, porta))

        dados, endereco = cliente.recvfrom(1024)
        print(f"Mensagem: {dados.decode()}")

finally:
    cliente.close()