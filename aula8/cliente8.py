import socket

host = "127.0.0.1"
porta = 1060

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def titulo(texto, simbolo='-', quant=40):
    print()
    print(texto)
    print(simbolo*quant)

while True:
    titulo('Cadastro de Usuários')
    print('1. Incluir Usuário')
    print('2. Listar Usuário')
    print('3. Finalizar')
    opcao = int(input('Opção: '))
    if opcao == 1:
        titulo('Inclusão de Usuários')
        login = input('Login: ')
        senha = input('Senha: ')
        mensagem = f"incluir;{login};{senha}"
    elif opcao == 2:
        mensagem = "listar"
    elif opcao == 3:
        break
    else:
        print('Código invalido')
        continue

    cliente.sendto(mensagem.encode(), (host, porta))
    dados, endereco = cliente.recvfrom(4096)
    print(dados.decode())

cliente.close()
