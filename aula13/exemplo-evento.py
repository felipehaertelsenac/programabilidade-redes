import threading
import time

evento = threading.Event()

def aguardando():
    print("Aguardando evento")
    evento.wait()
    print("Evento ocorreu")

def funcao_evento():
    time.sleep(3)
    print("definindo o evento")
    evento.set()

thread1 = threading.Thread(target=aguardando)
thread2 = threading.Thread(target=funcao_evento)

thread1.start()
thread2.start()

thread1.join()
thread2.join()