from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorDB:
    
    def __init__(self):
        pass
    
    def conexionDB (self):
        try:
            conexion = sqlite3.connect("C:/Users/Pablo/Documents/GitHub/POO/TkinterSQLite/DBUsuarios.db")
            print("Conectado a la DB")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def guardarUsuario(self,nom,corr,con):
        #1. llamo el metodo conexion
        conx = self.conexionDB()
        #2. Validar vacios
        if(nom =="" or corr == "" or con == ""):
            messagebox.showwarning("Aguas!!","Formulario incompleto")
            conx.close()
        else:
            #3. realizar el insert a la DB
            #4. Preparamos las variables necesarias
            cursor = conx.cursor()
            conH = self.ecriptarContra(con)
            datos = (nom,corr,conH)
            sqlInsert = "insert into tbRegistrados(nombre,correo,contra) values (?,?,?)"
            
            #5. Ejecutamos el Insert y cerramos la conexion
            cursor.execute(sqlInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario guardado")
        
    def ecriptarContra(self,con):
        #preparamos contraseña y sal para hash
        conPlana = con
        conPlana = conPlana.encode() #Contraseña convertida a bytes
        sal = bcrypt.gensalt()
        #encriptamos
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)
        #regresamos la contraseña encriptada
        return conHa