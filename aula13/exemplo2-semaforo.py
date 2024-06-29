import threading
import time

semaforo = threading.Semaphore(3)

def imprimir_numeros():
    global contador
    for _ in range(10):
        with semaforo:
            print(threading.current_thread().name)

threads = []
for _ in range(10):
    thread = threading.Thread(target=imprimir_numeros)
    threads.append(thread)
    thread.start()

for tread in threads:
    thread.join()
