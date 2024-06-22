import socket
from datetime import datetime

host = "127.0.0.1"
porta = 1061

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, porta))
servidor.listen(1)

print('Aguardando conexões na porta:', porta)

conexao, endereco = servidor.accept()

print(f'conectado por: {endereco}')

def incluirLog(ip, site):
    try:
        with open("internet.txt", "a") as arq:
            agora = datetime.now()
            data = agora.strftime('%d/%m/%Y')
            hora = agora.strftime('%H:%M:%S')
            arq.write(f'{ip};{site};{data};{hora}\n')
        
        conexao.send('1'.encode())
    except:
        conexao.send('0'.encode())

def pesquisarIP(ip):
    try:
        lista = ''
        with open('internet.txt', 'r') as arq:
            linhas = arq.readlines()

        for linha in linhas:
            partes = linha.split(';')

            if partes[0] == ip:
                lista += partes[1]+';'+partes[2]+';'+partes[3]+'#'

        if lista == '':
            conexao.send('0'.encode())
        else:
            conexao.send(lista[:-1].encode())

    except:
        conexao.send('0'.encode())

def pesquisaAcessos(site):
    try:
        numeroAcessos = 0
        with open('internet.txt', 'r') as arq:
            linha = arq.readline()
            while linha != '':
                partes = linha.split(';')
                if partes[1] == site:
                    numeroAcessos += 1
                linha = arq.readline()
        conexao.send((str(numeroAcessos)).encode())
    except:
        conexao.send('0'.encode())
    
def excluir(data):
    try:
        with open('internet.txt', 'r') as arq:
            linhas = arq.readlines()
        
        while True:
            existe = 0
            tamanho = len(linhas)
            numLinha = -1

            for i in range(0, tamanho):
                partes = linhas[i].split(';')
                numLinha += 1
                if partes[2] == data:
                    linhas.pop(numLinha)
                    existe = 1
                    break

            if existe == 0:
                break

        with open('internet.txt', 'w') as arq:
            for linha in linhas:
                arq.write(linha)

        if existe == 0:
            conexao.send('0'.encode())
        else:
            conexao.send('1'.encode())

    except:
        conexao.send('0'.encode())
    

while True:
    dados = conexao.recv(2048).decode()

    if dados == '':
        break

    print(f'dados recebidos: {dados}')

    partes = dados.split(';')

    if partes[0] == '1':
        incluirLog(partes[1], partes[2])
    elif partes[0] == '2':
        pesquisarIP(partes[1])
    elif partes[0] == '3':
        pesquisaAcessos(partes[1])
    elif partes[0] == '4':
        excluir(partes[1])


conexao.close()