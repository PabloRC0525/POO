from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorDB import *

#Instancia: Puente entre los 2 archivos
controlador = ControladorDB()

#Metodo que usa mi obj controlador para insertar

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCorr.get(),varPass.get())
#Metodo que usa mi obj controlador para buscar un usuario

def ejecutaSelect():
    rsUsu= controlador.consultarUsuario(varBus.get())
    for usu in rsUsu:
        cadena= str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])

    if(rsUsu): 
        textBus.config(state='normal')  # Configuración del estado del widget Text
        textBus.delete(1.0, 'end')  # Limpia el contenido del widget Text
        textBus.insert('end', cadena)  # Inserta la cadena en el widget Text
        textBus.config(state='disabled')  # Restaura el estado del widget Text a 'disabled'
    else:
        messagebox.showerror("Error","El usuario no existe en la base de datos")
        
def ejecutaconsulta():
    # Obtiene los usuarios de la base de datos
    rUsu= controlador.consulta()
    # Borra los datos existentes en la tabla
    tabla.delete(*tabla.get_children())
    # Inserta los nuevos datos en la tabla
    for usu in rUsu:
        tabla.insert('', 'end', text=usu[0], values=(usu[1], usu[2], usu[3]))
        
def ejecutaACT(varNomAE, varCorrAE, varPassAE):
    controlador.actualizar(varActElim.get(),varNomAE.get(), varCorrAE.get(), varPassAE.get())
    
def ejecutadelete():
    controlador.eliminar(varActElim.get())
    
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

#Pestaña 2: Buscar usuario
titulo2 = Label(pestaña2,text="Buscar usuario:",fg ="green",font=("Modern",18)).pack()

varBus=tk.StringVar()
lblid= Label(pestaña2,text="Identificador de usuario:")
txtid= Entry(pestaña2,textvariable=varBus).pack()
btnBusqueda= Button(pestaña2,text="Buscar",command=ejecutaSelect).pack()

subBus= Label(pestaña2,text= "Registrado:",fg="blue",font=("Modern",15)).pack()
textBus = tk.Text(pestaña2, height=5, width=52)
textBus.pack() 

#Pestaña 3: Consultar usuarios

subUS= Label(pestaña3,text= "Usuarios:",fg="blue",font=("Modern",15)).pack()
tabla = ttk.Treeview(pestaña3)
tabla['columns'] = ('nombre', 'correo', 'contraseña')
tabla.column('#0', width=50, minwidth=50)
tabla.column('nombre', width=120, minwidth=120)
tabla.column('correo', width=150, minwidth=150)
tabla.column('contraseña', width=100, minwidth=100)
tabla.heading('#0', text='ID', anchor=tk.CENTER)
tabla.heading('nombre', text='Nombre', anchor=tk.CENTER)
tabla.heading('correo', text='Correo', anchor=tk.CENTER)
tabla.heading('contraseña', text='Contraseña', anchor=tk.CENTER)
tabla.pack() 

Consultar= Button(pestaña3,text="Consultar",command=ejecutaconsulta).pack()

#Pestaña 4: Actualizar y eliminar
def ACT():
    global widgets_ACT # Declarar una variable global para almacenar las referencias de los widgets creados
    if id=="":
        messagebox.showerror("Error","Ingrese un ID")
    else:
        varNomAE = tk.StringVar()
        lblNomAE = Label(pestaña4,text="Nuevo nombre: ")
        lblNomAE.pack()
        txtNomAE = Entry(pestaña4,textvariable=varNomAE)
        txtNomAE.pack()

        varCorrAE = tk.StringVar()
        lblCorrAE = Label(pestaña4,text="Nuevo correo: ")
        lblCorrAE.pack()
        txtCorrAE = Entry(pestaña4,textvariable=varCorrAE)
        txtCorrAE.pack()

        varPassAE = tk.StringVar()
        lblPassAE = Label(pestaña4,text="Nueva contraseña: ")
        lblPassAE.pack()
        txtPassAE = Entry(pestaña4,textvariable=varPassAE)
        txtPassAE.pack()

        btnACT = Button(pestaña4,text="Actualizar usuario", command=lambda: ejecutaACT(varNomAE, varCorrAE, varPassAE))
        btnACT.pack()
        
        # Almacenar las referencias de los widgets creados
        widgets_ACT = [lblNomAE, txtNomAE, lblCorrAE, txtCorrAE, lblPassAE, txtPassAE, btnActualiza]
        btnActualiza.destroy()
    

titulo3 = Label(pestaña4,text="Actualizar y Eliminar Usuario:",fg ="purple",font=("Modern",18))
titulo3.pack()

varActElim = tk.StringVar()
lblidAE = Label(pestaña4,text="Identificador de usuario:")
lblidAE.pack()
txtidAE = Entry(pestaña4,textvariable=varActElim)
txtidAE.pack()

btnActualiza = Button(pestaña4,text="Actualizar usuario", command=ACT)
btnActualiza.pack()

btnElimina = Button(pestaña4,text="Eliminar usuario", command=ejecutadelete)
btnElimina.pack()

mensajeAE = tk.StringVar()
lblMensajeAE = Label(pestaña4, textvariable=mensajeAE)
lblMensajeAE.pack()

panel.add(pestaña1,text="Formulario usuarios")
panel.add(pestaña2,text="Buscar usuario")
panel.add(pestaña3,text="Consultar usuarios")
panel.add(pestaña4,text="Actualizar usuario")

ventana.mainloop()