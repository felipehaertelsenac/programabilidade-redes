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
        print("Acesso cadastrado com sucesso!")
    else:
        print('Erro no cadastramento no servidor!')

def pesquisaIP():
    ip = input('Qual IP pesquisar: ')

    mensagem = f"2;{ip}"

    cliente.send(mensagem.encode())

    retorno = cliente.recv(4096).decode()

    if retorno == '0':
        print('IP não consta na lista de acessos')
    else:
        linhas = retorno.split('#')

        print('Numero: Site:.................: Data.....: Hora...:')

        numeroLinha = 0

        for linha in linhas:
            numeroLinha += 1
            partes = linha.split(';')
            print(f'{numeroLinha:7d} {partes[0]:23s} {partes[1]} {partes[2][:-1]}')

    # site;data;hora# site;data;hora# site;data;hora

def pesquisaAcessos():
    site = input('Endereço do site: ')

    mensagem = f'3;{site}'

    cliente.send(mensagem.encode())

    retorno = cliente.recv(1024).decode()

    if retorno == '0':
        print('Site não acessado')
    else:
        print(f'Site acessado {retorno} vezes')

def excluir():
    data = input('Data: ')

    mensagem = f'4;{data}'

    cliente.send(mensagem.encode())

    retorno = cliente.recv(1024).decode()

    if retorno == '0':
        print('Não foi excluído')
    else:
        print(f'Os logs do dia {data} foram excluídos')

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