import socket
from datetime import datetime
import random

host = "127.0.0.1"
porta = 1060

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((host, porta))

print('Servidor de descoberta iniciado na porta', porta)

while True:

    dados, endereco = servidor.recvfrom(1024)

    request = dados.decode().lower()

    if request == "hora":
        response = datetime.now().strftime("%H:%M:%S")
    elif request == "data":
        response = datetime.now().strftime("%d/%m/%Y")
    elif request == "randomico":
        response = str(random.randint(1,10))
    else: 
        response = "Serviço desconhecido!"
    
    servidor.sendto(response.encode(), endereco)
       