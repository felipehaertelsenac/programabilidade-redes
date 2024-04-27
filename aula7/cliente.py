# importa a biblioteca socket
import socket

# define as configurações (IPV4, tipo protocolo UDP)
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# tenta conectar ao servidor que esta na escuta (host, porta)
cliente.connect(('localhost', 1060))

# envia uma mensagem
# .encode para codificar os dados enviados
cliente.send('Testando o envio de mensagem'.encode())

print('Mensagem enviada!')

# fecha a conexão
cliente.close()