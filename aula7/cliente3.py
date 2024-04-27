# importa a biblioteca socket
import socket

# define host e porta
host  = '127.0.0.1'
porta = 1060

# define as configurações (IPV4, tipo protocolo UDP)
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# tenta conectar ao servidor que esta na escuta (host, porta)
cliente.connect((host, porta))

print('Digite as mensagens ou "Fim" para sair')

while True:
    msg = input('Mensagem: ')

    # envia a mensagem
    cliente.send(msg.encode())
    
    if msg.upper() == 'FIM':
        # encerra o cliente e o servidor
        break
    elif msg == '5':
        # encerra apenas o cliente
        break
    else:
        print('Mensagem enviada!')

# fecha a conexão
cliente.close()