import threading
import time

contador = 0
lock = threading.Lock()

def imprimir_numeros():
    global contador
    for _ in range(1000):
        with lock:
            contador += 1
            print(contador)

threads = []
for _ in range(10):
    thread = threading.Thread(target=imprimir_numeros)
    threads.append(thread)
    thread.start()

for tread in threads:
    thread.join()

print(f"Contador: {contador}")