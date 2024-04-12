import os


def titulo(texto, simbolo='-', quant=40):
    print()
    print(texto)
    print(simbolo*quant)


def incluir():
    titulo('Inclusão de Usuários')

    login = input('Login: ')
    senha = input('Senha: ')
    
    # open: nome do arquivo e modo de abertura
    arq = open('usuarios.txt', 'a')
    arq.write(f'{login};{senha}\n')
    arq.close()

    print('Ok! Usuário cadastrado com sucesso!')


def listar():
    titulo('Listagem de Usuarios')

    # se o arquivo não existe
    if not os.path.isfile('usuarios.txt'):
        print('Não há usuarios cadastrados...')
        return

    arq = open('usuarios.txt')          # abre o arquivo para leitura
    linha = arq.readline()
    
    while linha != "":
        partes = linha.split(";")
        print(f"{partes[0]} : {partes[1][:-1]}")

        linha = arq.readline()

    arq.close()

while True:
    titulo('Cadastro de Usuários')
    print('1. Incluir Usuário')
    print('2. Listar Usuário')
    print('3. Finalizar')
    opcao = int(input('Opção: '))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    else:
        break
