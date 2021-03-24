import threading
from time import sleep


def espera():
    print("Inicio Espera")
    sleep(2)
    print("Fim Espera")

th = threading.Thread(target=espera, name="Espera")
th.start()

print(threading.enumerate()[1].name)
print(threading.enumerate()[1].is_alive())