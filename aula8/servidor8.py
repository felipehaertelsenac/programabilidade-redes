import socket
import os

host = "127.0.0.1"
porta = 1060

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((host, porta))

print('Servidor de cadastro iniciado na porta', porta)

def incluir(request):
    login, senha = request[1], request[2]

    with open('usuarios.txt', 'a') as arq:
        arq.write(f'{login};{senha}\n')
    
    return 'Ok! Usuário cadastrado com sucesso!'

def listar():
    if not os.path.isfile('usuarios.txt'):
        return 'Não há usuarios cadastrados...'

    with open('usuarios.txt') as arq:
        usuarios = arq.readlines()
        listagem = "\nListagem de Usuários\n" + "".join([f"{usuario.split(';')[0]} - {usuario.split(';')[1]}" for usuario in usuarios])
        return listagem
    
while True:

    dados, endereco = servidor.recvfrom(1024)
    request = dados.decode().split(";")
    opcao = request[0]
    if opcao == "incluir":
        response = incluir(request)
    elif opcao == "listar":
        response = listar()
    else:
        print('Código inválido')
    
    servidor.sendto(response.encode(), endereco)
       