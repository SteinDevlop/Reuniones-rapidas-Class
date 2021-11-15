from tkinter import *
import os
import tkinter as tk

#interfaz grafica simple

#P1 Main

   #Opciones: [clases insertadas] - configuracion - agragar clases

#P2 [clases insertadas]

   #descripcion de la clase a iniciar
   #Boton: Iniciar clase
   #Boton: Salir
   #Boton: Editar
#P3 Agregar clase
   #Caja de texto Nombre
   #Caja de texto Link
   #Caja de texto Descripcion
#P4 Configuracion
   #Boton Imagen de fondo
      #Boton-imagen (x10)
      #Boton Personalizada
      #Boton Salir
   #Boton Eliminar todo
   #Ayuda
   # Acerca de
      #[Informacion de desarollador] 

P1 = Tk()
#Comandos de Main
def New_Class():
   P3 = Tk()
   #Funcion para cerrar la ventana
   def Exit_P3():
      P3.destroy()
   #Funcion para crear la clase - Error crea un espacio innecesario - arregar para poner obligatorio un link y nombre
   def Create_P3():
      os.makedirs('txt_clss', exist_ok=True)
      path = "txt_clss/"
      name = Text_PutName.get()
      link = Text_PutLink.get()
      description = Text_PutDescription.get()
      file = open(path+ name + ".txt", "w")
      file.write(link + os.linesep)
      file.write(description)
      file.close()
      P3.destroy()
   P3.title("Agregado de clase")
   P3.geometry('600x300')
   #Label para la descripcion
   label_PutName = Label(P3, text="Nombre:")
   label_PutName.grid(column=0, row=0)
   label_PutLink = Label(P3, text="Link:")
   label_PutLink.grid(column=0, row=1)
   label_PutDescription = Label(P3, text="Descripcion:")
   label_PutDescription.grid(column=0, row=2)
   #Entradas de texto
   Text_PutName = Entry(P3,width=10)
   Text_PutName.grid(column=1, row=0)
   Text_PutLink = Entry(P3,width=10)
   Text_PutLink.grid(column=1, row=1)
   Text_PutDescription = Entry(P3,width=20)
   Text_PutDescription.grid(column=1, row=2)
   #Botones de salida
   Button_Exit = Button(P3, text="Cancelar", command= Exit_P3)
   Button_Exit.grid(column=3, row=0)
   Button_Create = Button(P3, text="Crear", command= Create_P3)
   Button_Create.grid(column=3, row=1)
P1.title("Main")
P1.geometry('1000x600')
Button_New_Class = Button(P1, text="Agregar nueva clase", command=New_Class)
Button_Config = Button(P1, text="Configuracion")
#Aqui van las supuestas clases por entrar - acordar con una base de datos
#-----------------------------
#-----------------------------
Button_New_Class.grid(column=0, row=0)
Button_Config.grid(column=0, row=1)
P1.mainloop()