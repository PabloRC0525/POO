from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#5 agregar funcion de mensaje
def mostrarmensaje():
    messagebox.showinfo("Informacion","Te informo que aqui todo esta peor que al igual que ella mi voluntad tambien murio")
    messagebox.showerror("Error","Te he fallado Anakin, te he fallado!!!")
    print(messagebox.askokcancel("Pregunta","¿Seguro que quieres guardar?"))
    
#6 funcion agrear botones
def agregarboton():
        botonVerde.config(text="+",bg="lightgreen",fg="black")
        botonNuevo=Button(seccion3, text="Boton nuevo",bg="black",fg="white")
        botonNuevo.pack()
    
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
botonAzul=Button(seccion1,text="Boton azul",bg="cyan",fg="black",command=mostrarmensaje)
botonAzul.place(x=60,y=60,height=30,width=100)

botonNegro=Button(seccion2,text="Boton Negro",bg="black",fg="white")
botonNegro.grid(row=0,column=0)
botonAmarillo=Button(seccion2,text="Boton amarillo",bg="yellow",fg="red")
botonAmarillo.grid(row=1,column=1)

botonVerde=Button(seccion3,text="Boton verde",bg="#255748",fg="white",command=agregarboton)
botonVerde.pack()
#Metodo para la ejecucion
ventana.mainloop()

entry = ttk.Entry()
entry.place(x=300, y=300)