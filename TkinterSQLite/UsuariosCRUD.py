from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorDB import *

#Instancia: Puente entre los 2 archivos
controlador = ControladorDB()

#Metodo que usa mi obj controlador para insertar

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCorr.get(),varPass.get())

ventana = Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)

#Pestaña 1: Fotmulario de registro
titulo = Label(pestaña1,text="Registro de usuarios",fg="blue",font=("Modern",18)).pack()
varNom = tk.StringVar()
lblNom = Label(pestaña1,text="Nombre: ").pack()
txtNom = Entry(pestaña1,textvariable=varNom).pack()
varCorr = tk.StringVar()
lblCorr = Label(pestaña1,text="Correo: ").pack()
txtCorr = Entry(pestaña1,textvariable=varCorr).pack()
varPass = tk.StringVar()
lblPass = Label(pestaña1,text="Contraseña: ").pack()
txtPass = Entry(pestaña1,textvariable=varPass).pack()

btnGuard = Button(pestaña1,text="Guardar usuario",command = ejecutaInsert).pack()

panel.add(pestaña1,text="Formulario usuarios")
panel.add(pestaña2,text="Buscar usuario")
panel.add(pestaña3,text="Consultar usuarios")
panel.add(pestaña4,text="Actualizar usuario")

ventana.mainloop()