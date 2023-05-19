from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from glob import glob
import cv2 
from PIL import Image, ImageTk
import numpy as np


pantalla1=Tk()
pantalla2=Toplevel()

pantalla2.withdraw() #cerrar la pantalla 2 cuando se inicialice 

#funciones para capturar el valor 
'''def actualizar_valor(valor):
    contraste.config(text="Contraste al: " + str(valor))

def actualizar_valor2(valor):
    umbralizacion.config(text="Umbralizacion al: " + str(valor))'''

#FUNCIONES PARA ABRIR Y CERRAR LAS VENTANAS
def abrirVentana1():
    pantalla2.withdraw() #cerrar la pantalla2
    pantalla1.deiconify() #abrir la pantalla1

def abrirVentana2():
    pantalla1.withdraw() #cerrar la pantalla1
    pantalla2.deiconify() #abrir la pantalla2

#---------------------------------------------------------------------------------------------------------------
#CONFIGURACIONES DE LA PANTALLA 1 
pantalla1.title("fingerprint") #titulo del proyecto
pantalla1.resizable(False, False) #para que no se mueva la pantalla
#pantalla1.iconbitmap("Fingerprint-2-icon.ico") icono de la app
pantalla1.geometry("800x550") #dimenciones
pantalla1.config(bg="#EEDEEB") #color fondo de pantalla

# CONFIGURACIONES DEL FRAME 1
miFrame=Frame(pantalla1, width="750", height="500" )
#miFrame.pack(side="left", anchor="n") #ubicacion del frame, expand="true"´para que ocupe toda la pantalla
miFrame.place(relx=0.5, rely=0.5, anchor="center")
miFrame.config(bg="#E4C6DE") #color de fondo del frame
miFrame.config(bd=10) #tamaño del borde
miFrame.config(relief="groove") #borde 
miFrame.config(cursor="heart") 

#LABEL O TEXTO EN EL FRAME
Label1=Label(miFrame, text=" Bienvenido a fingerprint", fg="#6C4581", font=("Comic Sans MS", 18)).place(x=200, y=6) #TEXTO BIENVENIDO

# IMAGEN EN EL FRAME
miImagen=PhotoImage(file="huella.gif") #cargar una imagen
Label(miFrame, image=miImagen).place(x=160, y=50)

#CONFIGURACIONES DEL BOTON DE LA PANTALLA1
boton=tk.Button(pantalla1, text="Empezar", height=1, width=10, fg="black", font=("Comic Sans MS", 18), command=abrirVentana2) #BOTON DE COMENZAR
boton.place(x=300, y=450)
boton.config(bg="#8D65A3") #color de fondo del frame

#------------------------------------------------------------------------------------------------------------------------------

#CONFIGURACIONES DE LA PANTALLA 2
pantalla2.title("cargar archivo") #titulo del proyecto
pantalla2.geometry("990x600") #dimenciones
pantalla2.config(bg="#EEDEEB") #color fondo de 
    
#NOMBRES DE LAS FUNCIONES EN PANTALLA 2
nitidez=Label(pantalla2, text=" Nitidez", fg="#6C4581", font=("Comic Sans MS", 13)).place(x=200, y=440)
umbralizacion=Label(pantalla2, text=" Umbralizacion", fg="#6C4581", font=("Comic Sans MS", 13)).place(x=350, y=440)
brillo=Label(pantalla2, text=" Brillo", fg="#6C4581", font=("Comic Sans MS", 13)).place(x=550, y=440)
rotacion=Label(pantalla2, text=" Rotacion", fg="#6C4581", font=("Comic Sans MS", 13)).place(x=700, y=440)


# CONFIGURACIONES DEL FRAME 2
miFrame2=Frame(pantalla2, width="375", height="390" )
#miFrame.pack(side="left", anchor="n") #ubicacion del frame, expand="true"´para que ocupe toda la pantalla
miFrame2.place(relx=0.15, rely=0.365, anchor=W)
miFrame2.config(bg="#E4C6DE") #color de fondo del frame
miFrame2.config(bd=10) #tamaño del borde
miFrame2.config(relief="groove") #borde 
miFrame2.config(cursor="heart")

# CONFIGURACIONES DEL FRAME 2
miFrame3=Frame(pantalla2, width="375", height="390" )
#miFrame.pack(side="left", anchor="n") #ubicacion del frame, expand="true"´para que ocupe toda la pantalla
miFrame3.place(relx=0.95, rely=0.365, anchor=E)
miFrame3.config(bg="#E4C6DE") #color de fondo del frame
miFrame3.config(bd=10) #tamaño del borde
miFrame3.config(relief="groove") #borde 
miFrame3.config(cursor="heart")

#BARRAS HORIZONTALES EN PANTALLA 2
#definicion de rangos para funcion de contraste de 0-100
#definición de rangos para la funcion de umbralizacion 0-200
BarraUmbralizacion = Scale(pantalla2, from_= 0, to=200,orient=HORIZONTAL) 
BarraUmbralizacion.place(x=350, y=480)

#BarraNitidez = Scale(pantalla2, orient=HORIZONTAL) #no se usa rangos en la nitidez
#BarraNitidez.place(x=185, y=480) #no se usa rangos en la nitidez

#definicion de rangos para la funcion de brillo de -200 a 200
BarraBrillo = Scale(pantalla2, from_= -200, to=200, orient=HORIZONTAL)
BarraBrillo.place(x=550, y=480)

BarraRotacion = Scale(pantalla2, from_= 0, to=360, orient=HORIZONTAL)
BarraRotacion.place(x=700, y=480)

#FUNCIONES PARA EL MENU EN PANTALLA 2
def salirApp():
    valor=messagebox.askokcancel("salir","estas seguro?")
    if valor==True:
        pantalla1.destroy() #finalizar programa
        pantalla2.destroy() #finalizar programa

 #CARGAR UN ARCHIVO
imagenFrame2 = Label(miFrame2, width="352", height="367") # Crear el Label para mostrar las imagenes de la base de datos
imagenFrame2.place(relx=0.5, rely=0.50, anchor="center")
imagenFrame2.config(bg="white") #color fondo 

imagenFrame3 = Label(miFrame3, width="352", height="367") # Crear el Label para mostrar las imagenes de la base de datos
imagenFrame3.place(relx=0.5, rely=0.50, anchor="center")
imagenFrame3.config(bg="white") #color fondo 

#CARGAR LA BASE DE DATOS
def abrirArchivo():
    global pos, nombre_imagenes
    directorio = (filedialog.askdirectory())  # Seleccionar una carpeta en el explorador de archivos
    nombre_imagenes = glob(  #sacar lista de archivos en el directorio
        directorio + "/*/*.jpg"  
    )  # Retorna una lista con los nombres de archivos
    # en formato png
    #print(nombre_imagenes)
    n_imgs=len(nombre_imagenes)
    pos=0
    miImagen2 = ImageTk.PhotoImage(Image.open(nombre_imagenes[pos]).resize((320,320)))

        #file=nombre_imagenes[0], height=256, width=256
      # Cargar la primera imagen en la carpeta
    imagenFrame2.configure(image=miImagen2)  # Mostrar la imagen
    imagenFrame2.image = miImagen2

def ImgSiguiente():
    global pos, nombre_imagenes
    pos+=1
    miImagen2 = ImageTk.PhotoImage(Image.open(nombre_imagenes[pos]).resize((320,320)))
    #file=nombre_imagenes[0], height=256, width=256 # Cargar la primera imagen en la carpeta
    imagenFrame2.configure(image=miImagen2)  # Mostrar la imagen
    imagenFrame2.image = miImagen2

def ImgAnterior():
    global pos, nombre_imagenes
    pos-=1
    miImagen2 = ImageTk.PhotoImage(Image.open(nombre_imagenes[pos]).resize((320,320)))
        #file=nombre_imagenes[0], height=256, width=256
      # Cargar la primera imagen en la carpeta
    imagenFrame2.configure(image=miImagen2)  # Mostrar la imagen
    imagenFrame2.image = miImagen2


#leer la imagen de la flecha derecha
image = Image.open("flechaDerecha.png")
 
#redimensionar la imagen
resize_image = image.resize((30, 50))

#nueva imagen con nuevas dimensiones 
img = ImageTk.PhotoImage(resize_image)

#BOTON PARA AVANZAR CON IMAGEN
Bsiguiente=tk.Button(pantalla2, height=30, width=50, image=img ,justify="right", fg="black",command=ImgSiguiente)
Bsiguiente.place(x=80, y=80)

#leer la imagen de la flecha izquierda
image2 = Image.open("flechaIzquierda.png")
 
#redimensionar la imagen
resize_image2 = image2.resize((30, 50))
 
#nueva imagen con nuevas dimensiones 
img2 = ImageTk.PhotoImage(resize_image2)

#BOTON PARA DEVOLVERSE CON IMAGEN
Banterior=tk.Button(pantalla2, height=30, width=50, image=img2 ,justify="right", fg="black",command=ImgAnterior)
Banterior.place(x=80, y=150)

#-------------------------------------------------------------------------------------------------------s
def nitidez():
    global new_img, pos, nombre_imagenes
    coeficientes = np.array([[0, 1, 0],
                         [1, -5, 1],
                         [0, 1, 0]])*-1
    img=cv2.imread(nombre_imagenes[pos],cv2.IMREAD_GRAYSCALE)
    #img=cv2.imread(nombre_imagenes[pos],cv2.IMREAD_GRAYSCALE)
    new_img = cv2.filter2D(img, 0, coeficientes)
    imagen = ImageTk.PhotoImage(Image.fromarray(new_img).resize((320,320)))
    imagenFrame3.configure(image=imagen)
    imagenFrame3.image=imagen
    return new_img

bNitidez=tk.Button(pantalla2, text="nitidez", height=1, width=8, fg="black", font=("Comic Sans MS", 12),command=nitidez)
bNitidez.place(x=200, y=480)

def umbralizacion():
    global new_img, pos, nombre_imagenes
    img=nitidez()
    #img=cv2.imread(nombre_imagenes[pos],cv2.IMREAD_GRAYSCALE)
    ret,new_img = cv2.threshold(img,BarraUmbralizacion.get(),255,cv2.THRESH_BINARY)
    imagen = ImageTk.PhotoImage(Image.fromarray(new_img).resize((320,320)))
    imagenFrame3.configure(image=imagen)
    imagenFrame3.image=imagen
    return new_img

bUmbralizacion=tk.Button(pantalla2, text="umbralizacion", height=1, width=10, fg="black", font=("Comic Sans MS", 12),command=umbralizacion)
bUmbralizacion.place(x=350, y=530)


def brillo():
    global new_img, pos, nombre_imagenes
    adjustment3 = BarraBrillo.get()
    img=umbralizacion()
    #img=cv2.imread(nombre_imagenes[pos],cv2.IMREAD_GRAYSCALE)
    new_img = np.uint8(np.clip(adjustment3 + img.astype(np.int16), 0, 255))
    imagen3 = ImageTk.PhotoImage(Image.fromarray(new_img).resize((320,320)))
    imagenFrame3.configure(image=imagen3)
    imagenFrame3.image=imagen3
    return new_img 

bBrillo=tk.Button(pantalla2, text="brillo", height=1, width=8, fg="black", font=("Comic Sans MS", 12),command=brillo)
bBrillo.place(x=550, y=530)

def rotacion():
    global new_img, pos, nombre_imagenes
    #img=cv2.imread(nombre_imagenes[pos],cv2.IMREAD_GRAYSCALE)
    img=brillo()
    ancho, alto = img.shape
    center = (ancho/2, alto/2)
    grados= BarraRotacion.get()
    theta = np.deg2rad(grados)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=grados, scale=1)
    new_img = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(ancho, alto))
    imagen = ImageTk.PhotoImage(Image.fromarray(new_img).resize((320,320)))
    imagenFrame3.configure(image=imagen)
    imagenFrame3.image=imagen
    return new_img

bRotacion=tk.Button(pantalla2, text="rotacion", height=1, width=8, fg="black", font=("Comic Sans MS", 12),command=rotacion)
bRotacion.place(x=700, y=530)

#---------------------------------------------------------------------------------------------------------------------------
#BOTON PARA GUARDAR LA IMAGEN
def guardar():
    global new_img, pos, nombre_imagenes
    #imagen = ImageTk.PhotoImage(Image.fromarray(new_img).resize((320,320)))
    imagen=rotacion()
    cv2.imwrite("resultado.png",imagen)

bGuardar=tk.Button(pantalla2, text="Guardar", height=1, width=8, fg="black", font=("Comic Sans MS", 14),command=guardar)
bGuardar.place(x=850, y=450)
bGuardar.config(bg="#8D65A3") #color de fondo del frame

#---------------------------------------------------------------------------------------------------------------------------
#MENU DE LA PANTALLA 2
barraMenu=Menu(pantalla2)
pantalla2.config(menu=barraMenu, width=600, height=600)

archivoM=Menu(barraMenu, tearoff=0)
archivoM.add_command(label="abrir", command=abrirArchivo)
archivoM.add_separator()
archivoM.add_command(label="salir", command=salirApp) #ventana emergente

barraMenu.add_cascade(label="archivo", menu=archivoM)

#CONFIGURACION BOTON DE ATRAS PANTALLA 2
'''# Carga la imagen
imagen = tk.PhotoImage(file="devolver.gif")

# Crea el botón y establece la imagen
boton = tk.Button(pantalla1, image=imagen).place(x=160, y=50)

# Empaqueta el botón en la ventana
boton.pack()'''

botonAtras=tk.Button(pantalla2, text="Atras", height=1, width=4, fg="black", font=("Comic Sans MS", 12), command=abrirVentana1)
botonAtras.place(x=20, y=40)
botonAtras.config(bg="#8D65A3") #color de fondo del 

#-----------------------------------------------------------------------------------------------------------

pantalla1.mainloop()