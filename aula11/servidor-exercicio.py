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

while True:
    dados = conexao.recv(2048).decode()

    if dados == '':
        break

    print(f'dados recebidos: {dados}')

    partes = dados.split(';')

    if partes[0] == '1':
        incluirLog(partes[1], partes[2])

conexao.close()