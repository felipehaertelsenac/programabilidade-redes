import socket

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Controle de Acessos")

tentativas = 0

while tentativas < 3:
    login = input("Login: ")
    senha = input("Senha: ")

    cliente.sendto(f"{login};{senha}".encode(), (host, porta))
    dados, endereco = cliente.recvfrom(1024)

    if dados.decode() == "liberado":
        print("Acesso Liberado!")
        break
    elif dados.decode() == "arquivonaoencontrado":
        print("Arquivo não encontrado.")
        break
    else:
        tentativas += 1
        print(f"Erro... inválido - {tentativas}ª tentativa.")
        if tentativas == 3:
            print("Limite de tentativas esgotado")

cliente.close()
        