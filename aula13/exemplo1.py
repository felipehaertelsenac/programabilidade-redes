import threading

def ler_arquivo(arquivo):
    with open(arquivo, 'r') as arq:
        dados = arq.read()
    print(f"Lido o arquivo {dados}")

def escrever_arquivo(arquivo, dados):
    with open(arquivo, 'w') as arq:
        arq.write(dados)
    print(f"Arquivo escrito {arquivo}")

thread1 = threading.Thread(target=ler_arquivo, args=('arquivo.txt',))

thread2 = threading.Thread(target=escrever_arquivo, args=('arquivo2.txt', 'Teste com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2este com Threads 2'))


thread1.start()
thread2.start()
thread1.join()


print('Fim do programa')


thread2.join()



