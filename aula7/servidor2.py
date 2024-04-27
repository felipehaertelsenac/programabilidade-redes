# importa a biblioteca socket
import socket

# define as configurações (IPV4, tipo protocolo UDP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Iniciando escuta no servidor!')

# inicia escuta no servidor
servidor.bind(('127.0.0.1', 1060))

# recebe os dados enviados pelo cliente
dados, endereco = servidor.recvfrom(2048)

print(f'Conectado por {endereco}')

# exibe os dados recebidos
# .decode para decodificar os bytes recebidos
print(f'Dados recebidos: {dados.decode()}')

msg = f'A mensagem "{dados.decode()}" foi recebida corretamente!'

# envia dados para o programa cliente
servidor.sendto(msg.encode(), endereco)

# fecha a conexão
servidor.close()