from tkinter import *
from tkinter import ttk
from Clase12 import *
ventana = Tk()
ventana.title("Iniciar sesion")
ventana.geometry("600x400")

seccion1=Frame(ventana,bg="green")
seccion1.pack(expand=True,fill='both')

ic = Label(ventana, text="Ingrese su correo:", bg="green")
ic.place(x=50,y=50)

corr = ttk.Entry(width= 30)
corr.place(x=200,y=50)

ip = Label(ventana, text="Ingrese su contraseña:", bg="green")
ip.place(x=50,y=80)

passw = ttk.Entry(width= 30,show="*")
passw.place(x=200,y=80)

word1 = "121038827@upq.edu.mx"
word2 = "upq1234"


validacion = Validacion(corr,passw,word1,word2)
BotonValidar=Button(seccion1,text="Validar",bg="#255748",fg="white",command=validacion.validar)
BotonValidar.pack()
ventana.mainloop()