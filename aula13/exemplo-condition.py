import threading
import time

condition = threading.Condition()
itens = []

def produtor():
    global itens
    with condition:
        for i in range(10):
            itens.append(i)
            print(f"Produzido {i}")
            condition.notify()
        time.sleep(1)
        condition.notify_all()

def consumidor():
    global itens
    while True:
        with condition:
            while len(itens) == 0:
                condition.wait()
            print(f"Consumido o item {itens.pop(0)}")


thread1 = threading.Thread(target=produtor)
thread2 = threading.Thread(target=consumidor)

thread1.start()
thread2.start()

thread1.join()
thread2.join()