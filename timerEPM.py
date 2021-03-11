from tkinter import *
import time
import bcolors



class bcolors:
    rojo = '\033[93m'
    normal = '\033[0m'

root = Tk()
totalw = 0
totala = 0
totals = 0
totald = 0
contadorw = 0
contadora = 0
contadors = 0
contadord = 0
rojo = bcolors.rojo
normal = bcolors.normal
colorw = normal
colors = normal
colora = normal
colord = normal
primerclick = 0


root.title("Cronómetro MB03T")
print("Haz click en la ventana gris para empezar el programa")

def key(event):
    print("\n", repr(event.char))


def callback(event):
    global primerclick
    frame.focus_set()
#    print ("click en", event.x, event.y)
    if primerclick == 0:
        print("Programa iniciado, presiona W, A, S y D para iniciar/parar cada uno de los 4 timers\n")
        primerclick = primerclick + 1


def teclaw(event):
    global contadorw
    global iniciow
    global totalw
    global colorw
    if contadorw%2 == 0:
        iniciow = time.time()
        contadorw = contadorw + 1
        colorw = rojo
        print(f"{colorw}\tTimer 1\t\t{colora}Timer 2\t\t{colors}Timer 3\t\t{colord}Timer 4{normal}", end = "\r")
    else:
        finw = time.time()+totalw
        totalw = finw - iniciow
        contadorw = contadorw + 1
        colorw = normal
        print(f"{colorw}\tTimer 1\t\t{colora}Timer 2\t\t{colors}Timer 3\t\t{colord}Timer 4{normal}",end = "\r")
    return(colorw)

def teclaa(event):
    global contadora
    global inicioa
    global totala
    global colora
    if contadora%2 == 0:
        inicioa = time.time()
        contadora = contadora + 1
        colora = rojo
        print(f"{colorw}\tTimer 1\t\t{colora}Timer 2\t\t{colors}Timer 3\t\t{colord}Timer 4{normal}", end = "\r")
    else:
        fina = time.time()+totala
        totala = fina - inicioa
        contadora = contadora + 1
        colora = normal
        print(f"{colorw}\tTimer 1\t\t{colora}Timer 2\t\t{colors}Timer 3\t\t{colord}Timer 4{normal}", end = "\r")

def teclas(event):
    global contadors
    global inicios
    global totals
    global colors
    if contadors%2 == 0:
        inicios = time.time()
        contadors = contadors + 1
        colors = rojo
        print(f"{colorw}\tTimer 1\t\t{colora}Timer 2\t\t{colors}Timer 3\t\t{colord}Timer 4{normal}", end = "\r")
    else:
        fins = time.time()+totals
        totals = fins - inicios
        contadors = contadors + 1
        colors = normal
        print(f"{colorw}\tTimer 1\t\t{colora}Timer 2\t\t{colors}Timer 3\t\t{colord}Timer 4{normal}", end = "\r")

def teclad(event):
    global contadord
    global iniciod
    global totald
    global colord
    if contadord%2 == 0:
        iniciod = time.time()
        contadord = contadord + 1
        colord = rojo
        print(f"{colorw}\tTimer 1\t\t{colora}Timer 2\t\t{colors}Timer 3\t\t{colord}Timer 4{normal}", end = "\r")
    else:
        find = time.time()+totald
        totald = find - iniciod
        contadord = contadord + 1
        colord = normal
        print(f"{colorw}\tTimer 1\t\t{colora}Timer 2\t\t{colors}Timer 3\t\t{colord}Timer 4{normal}", end = "\r")

def salir(event):
    print("\n\nT1 = ", round(totalw, 3), "\tf1 = ", round(int(contadorw/2)))
    print("T2 = ", round(totala, 3), "\tf2 = ", round(int(contadora/2)))
    print("T3 = ", round(totals, 3), "\tf3 = ", round(int(contadors/2)))
    print("T4 = ", round(totald, 3), "\tf4 = ", round(int(contadord/2)))

def cero(event):
    print("\n----PONGO TODO A 0-----\n")
    global totala 
    global totals
    global totald
    global totalw
    global contadora
    global contadors
    global contadord
    global contadorw
    totala = 0
    totals = 0
    totald = 0
    totalw = 0
    contadora = 0 
    contadors = 0 
    contadord = 0 
    contadorw = 0 



frame = Frame(root, width=300, height=300)
frame.bind("<Key>", key)
frame.bind("w", teclaw)
frame.bind("a", teclaa)
frame.bind("s", teclas)
frame.bind("d", teclad)
frame.bind("<space>", salir)
frame.bind("0", cero)

frame.bind("<Button-1>", callback)
frame.pack()




root.mainloop()
