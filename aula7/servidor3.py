# importa a biblioteca socket
import socket

# define host e porta
host = "127.0.0.1"
porta = 1060

# define as configurações (IPV4, tipo protocolo UDP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'Iniciando a escuta no servidor {host}...')

# inicia escuta no servidor
servidor.bind((host, porta))

# variavel flag, para verificar se existe uma conexão ativa
flag = False

while True:
    #recebe os dados enviados pelo cliente
    dados, endereco = servidor.recvfrom(2048)

    # verifica se não havia conexão e altera a flag
    if not flag:
        print(f'Conectado por {endereco}')
        flag = True

    # exibe os dados recebidos
    # .decode para decodificar os bytes recebidos
    print(f'Dados recebidos: {dados.decode()}')

    # verifica se foi digitado 5, para interromper a conexão do cliente, sem encerrar o servidor
    if dados.decode() == '5':
        print(f'Desconectado do endereço {endereco}')
        flag = False

    # verifica se foi digitado FIM, para encerrar o cliente e o servidor
    if dados.decode().upper() == 'FIM':
        break

# fecha a conexão
servidor.close()