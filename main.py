import threading as thr

from time import sleep
from cache_teste import cache

def fibonacci(parametro_numero):
    numero_anterior = 0
    numero_posterior = 1
    numero = 0

    for i in range(parametro_numero):
        numero_anterior = numero_posterior
        numero_posterior = numero
        numero = numero_anterior + numero_posterior

    return numero

def teste_fib(inicio, fim):
    erro = 0
    acerto = 0
    for item in range(inicio, fim):
        print(f"{inicio} - {fim}: item:{item}")
        sleep(0.5)
        if not cache[item] == fibonacci(item):
            erro += 1
        else:
            acerto += 1
    print(f"Intervalo: {inicio} - {fim} - Erros: {erro} - Acertos: {acerto}")
    return erro, acerto

def th_fib():
    # Thread 01
    th1 = thr.Thread(target=teste_fib, args=(0, 10,), name="th1")
    th1.start()

    # Thread 02
    th2 = thr.Thread(target=teste_fib, args=(10, 20,), name="th2")
    th2.start()
    
    # Thread 03
    th3 = thr.Thread(target=teste_fib, args=(20, 30,), name="th3")
    th3.start()

th_all = thr.Thread(target=th_fib, name="th_fib")
th_all.start()

print(f"\nTH {thr.enumerate()[0].name} - {thr.enumerate()[0].is_alive()}")
