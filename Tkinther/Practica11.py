from tkinter import *

#Generar ventana
ventana = Tk()
ventana.title("Ejemplo 3 Frames")
ventana.geometry("600x400")

#Agregar frames
seccion1=Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="gray")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="purple")
seccion3.pack(expand=True,fill='both')

#Agregamos botones
botonAzul=Button(seccion1,text="Boton azul",bg="cyan",fg="black")
botonAzul.place(x=60,y=60,height=30,width=100)

botonNegro=Button(seccion2,text="Boton Negro",bg="black",fg="white")
botonNegro.grid(row=0,column=0)
botonAmarillo=Button(seccion2,text="Boton amarillo",bg="yellow",fg="red")
botonAmarillo.grid(row=1,column=1)

botonVerde=Button(seccion3,text="Boton verde",bg="lightgreen",fg="black")
botonVerde.pack()
#Metodo para la ejecucion
ventana.mainloop()
