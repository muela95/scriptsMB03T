from pynput.keyboard import Key, Listener, KeyCode
from colorama import Fore, init, Style
import time
import numpy as np
import colorama
import pyperclip

init(autoreset=True)

print("Programa iniciado\nMantén pulsado W/A/S/D para contar tiempo/frecuencia\n
        Pulsa espacio para copiar los tiempos y frecuencias (formato t1, f1, t2, f2...)\n
        Pulsa 0 para resetear todo a 0")


tiemposInicio = [0,0,0,0]
tiemposFin = [0,0,0,0]
tiemposTotal = [0,0,0,0]
contadores = [0,0,0,0]
frecuenciasTotal = [0,0,0,0]
rojo = Fore.RED
normal = Fore.RESET
colores = [normal, normal, normal, normal]
import contextlib

print("Timer iniciado")
print("Deja pulsado W, A, S o D para iniciar cada uno de los 4 timers diferentes, levanta el dedo para parar de contar")
print("Pulsa espacio para sacar el tiempo que llevas en cada uno de los 4")
print("Pulsa 0 (el número) para poner todos los timers y contadores a 0.")

def on_press(key):
    global tiemposTotal
    global tiemposFin
    global tiemposInicio
    global contadores
    global colores
    global frecuenciasTotal
    if key == KeyCode.from_char('w'):
        if contadores[0] == 0:
            tiemposInicio[0] = time.time()
            colores[0] = rojo
            print(f"{colores[0]}\r\tW\t\t{colores[1]}A\t\t{colores[2]}S\t\t{colores[3]}D", end='')
            contadores[0] = contadores[0] + 1
            frecuenciasTotal[0] = frecuenciasTotal[0] + 1
    if key == KeyCode.from_char('a'):
        if contadores[1] == 0:
            tiemposInicio[1] = time.time()
            colores[1] = rojo
            print(f"{colores[0]}\r\tW\t\t{colores[1]}A\t\t{colores[2]}S\t\t{colores[3]}D", end='')
            contadores[1] = contadores[1] + 1
            frecuenciasTotal[1] = frecuenciasTotal[1] + 1
    if key == KeyCode.from_char('s'):
        if contadores[2] == 0:
            tiemposInicio[2] = time.time()
            colores[2] = rojo
            print(f"{colores[0]}\r\tW\t\t{colores[1]}A\t\t{colores[2]}S\t\t{colores[3]}D", end='')
            contadores[2] = contadores[2] + 1
            frecuenciasTotal[2] = frecuenciasTotal[2] + 1
    if key == KeyCode.from_char('d'):
        if contadores[3] == 0:
            tiemposInicio[3] = time.time()
            colores[3] = rojo
            print(f"{colores[0]}\r\tW\t\t{colores[1]}A\t\t{colores[2]}S\t\t{colores[3]}D", end='')
            contadores[3] = contadores[3] + 1
            frecuenciasTotal[3] = frecuenciasTotal[3] + 1





def on_release(key):
    global tiemposTotal
    global tiemposFin
    global tiemposInicio
    global contadores
    global colores
    global frecuenciasTotal
    #print('{0} release'.format(
    #key))
    if key == KeyCode.from_char('w'):
        tiemposFin[0] = time.time()
        tiemposTotal[0] = tiemposTotal[0] + round(tiemposFin[0]-tiemposInicio[0], 3)
        contadores[0] = 0
        colores[0] = normal
        print(f"{colores[0]}\r\tW\t\t{colores[1]}A\t\t{colores[2]}S\t\t{colores[3]}D", end='')

    if key == KeyCode.from_char('a'):
        tiemposFin[1] = time.time()
        tiemposTotal[1] = tiemposTotal[1] + round(tiemposFin[1]-tiemposInicio[1], 3)
        contadores[1] = 0
        colores[1] = normal
        print(f"{colores[0]}\r\tW\t\t{colores[1]}A\t\t{colores[2]}S\t\t{colores[3]}D", end='')
        # Stop listener
        # return False
    if key == KeyCode.from_char('s'):
        tiemposFin[2] = time.time()
        tiemposTotal[2] = tiemposTotal[2] + round(tiemposFin[2]-tiemposInicio[2], 3)
        contadores[2] = 0
        colores[2] = normal
        print(f"{colores[0]}\r\tW\t\t{colores[1]}A\t\t{colores[2]}S\t\t{colores[3]}D", end='')
    if key == KeyCode.from_char('d'):
        tiemposFin[3] = time.time()
        tiemposTotal[3] = tiemposTotal[3] + round(tiemposFin[3]-tiemposInicio[3], 3)
        contadores[3] = 0
        colores[3] = normal
        print(f"{colores[0]}\r\tW\t\t{colores[1]}A\t\t{colores[2]}S\t\t{colores[3]}D", end='')
    if key == Key.space:
        print("\n\nTiempo en W ", np.round(tiemposTotal[0], 3),
              "\nTiempo en A ", np.round(tiemposTotal[1], 3),
              "\nTiempo en S ", np.round(tiemposTotal[2], 3),
              "\nTiempo en D ", np.round(tiemposTotal[3], 3),
              "\n\nLa frecuencia en W ", frecuenciasTotal[0],
              "\nFrecuencia en A ", frecuenciasTotal[1],
              "\nFrecuencia en S ", frecuenciasTotal[2],
              "\nFrecuencia en D ", frecuenciasTotal[3],

              )
        pyperclip.copy(str(tiemposTotal[0]) + "\t" + str(frecuenciasTotal[0]) + "\t" +
                       str(tiemposTotal[1]) + "\t" + str(frecuenciasTotal[1]) + "\t" +
                       str(tiemposTotal[2]) + "\t" + str(frecuenciasTotal[2]) + "\t" +
                       str(tiemposTotal[3]) + "\t" + str(frecuenciasTotal[3]))
    if key == KeyCode.from_char('0'):
        print("\n\nPongo todo a 0 (confirma, lo que llevabas hasta ahora era: )\n",
              "Tiempos (wasd)", np.round(tiemposTotal, 3), "\n",
              "Frecuencias (wasd)", frecuenciasTotal)
        tiemposTotal = [0,0,0,0]
        frecuenciasTotal = [0,0,0,0]

# Collect events until released
with Listener(
    on_press=on_press, suppress=True,
    on_release=on_release) as listener:
    listener.join()
