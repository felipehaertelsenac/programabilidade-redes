import socket

host = "127.0.0.1"
porta = 1060

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((host, porta))
print("Servidor de login iniciado na porta", porta)

def verifica_dados(login, senha):
    try:
        with open('usuarios.txt', 'r') as arq:
            linha = arq.readline()
            
            while linha != "":
                partes = linha.split(";")
                
                if login == partes[0] and senha == partes[1][:-1]:
                    return "liberado"

                linha = arq.readline()
    except FileNotFoundError:
        return "arquivonaoencontrado"
    return "negado"

while True:
    dados, endereco = servidor.recvfrom(1024)
    login, senha = dados.decode().split(";")
    response = verifica_dados(login, senha)
    servidor.sendto(response.encode(), endereco)