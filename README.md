# scriptsMB03T
## Timer
### Instalación de dependencias
Para poder usarlo hay que instalar python 3, normalmente la última versión suele funcionar. Se puede descargar [aquí](https://www.python.org/downloads/windows/) para windows.
Aparte de python3 también hay que instalar las librerías que el timer usa: tkinter, colorama y bcolors. Para instalar estas librerías se usa "pip", gestor de paquetes de python que debería venir con la instalación de python 3.
Abre una terminal (varias opciones: puedes abrir el menú de windows y ejecutar símbolo del sistema o bien pulsar a la vez "Win+R" y ejecutar cmd.exe) escribe este comando y pulsa enter:
  pip install tk bcolors colorama
  
### Uso
Doble click en el archivo para abrir, se abren dos ventanas, una consola y una ventana gris. Hay que hacer click en la ventana gris para usar el programa. **El programa no va a funcionar si no has hecho click en la ventana gris y cada vez que hagas click en otro sitio va a dejar de registrar inputs nuevos aunque seguirá contando** 
### Teclas
Las que vienen de serie son "W", "A", "S", y "D" para empezar/pausar los timers, "0" para poner todos los valores a 0 y barra espaciadora para sacar en pantalla los tiempos y frecuencia.
Si se quieren cambiar es tan fácil como editar el archivo con el bloc de notas y sustituir las instrucciones del final "frame.bind ("w", teclaw)" cambiando la tecla entre comillas por cualquier tecla.
