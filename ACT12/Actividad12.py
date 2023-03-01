from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def validar():
    if correo=="121038827@upq.edu.mx" and contraseña=="upq1234":
        messagebox.showinfo("Correcto","Sus datos son correctos")
    else:
        messagebox.showerror("Error", "Correo o contraseña incorrectos")

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

passw = ttk.Entry(width= 30)
passw.place(x=200,y=80)

Validar=Button(seccion1,text="Validar",bg="#255748",fg="white",command=validar)
Validar.pack()
ventana.mainloop()