import socket

host = "127.0.0.1"
porta = 1061

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((host, porta))

def titulo(texto, simbolo='-', quant=40):
    print()
    print(texto)
    print(simbolo*quant)

def inclusao():
    ip = input('Qual o IP do acesso: ')
    site = input('Qual site foi acessado: ')
    
    mensagem = '1;'+ip+';'+site

    cliente.send(mensagem.encode())

    retorno = cliente.recv(2048).decode()

    if retorno == '1':
        print("Acesso cadastro com sucesso!")
    else:
        print('Erro no cadastramento no servidor!')

def pesquisaIP():
    return True

def pesquisaAcessos():
    return True

def excluir():
    return True

while True:
    titulo('Menu Principal - Controle de Logs')
    print('1. Incluir Log')
    print('2. Pesquisar por IP')
    print('3. Pesquisar Acessos a Site')
    print('4. Excluir Logs (Data)')
    print('5. Finalizar')
    opcao = int(input('Opção: '))
    if opcao == 1:
        inclusao()
    elif opcao == 2:
        pesquisaIP()
    elif opcao == 3:
        pesquisaAcessos()
    elif opcao == 4:
        excluir()
    else:
        break

cliente.close()