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
    
    def consultarUsuario(self,id):
        #1. realizar conexion DB
        conx = self.conexionDB()
        #2. verificar que el id vacio
        if(id==""):
            messagebox.showwarning("Cuidado","Escribe un identificador")
        else:
            #3. Ejecutar la consulta
            try:
                #4. Preparamos lo necesario
                cursor=conx.cursor()
                sqlselect= "select * from tbRegistrados where id ="+id
                #5. Ejecutamos y cerramos conexion
                cursor.execute(sqlselect)
                RSUsuario = cursor.fetchall()
                conx.close()
                return RSUsuario
                
            except sqlite3.OperationalError:
                print("Error de consulta")
    def consulta(self):
        #1. realizar conexion DB
        conx = self.conexionDB()
        try:
            #4. Preparamos lo necesario
            cursor=conx.cursor()
            sqlselect= "select * from tbRegistrados"
            #5. Ejecutamos y cerramos conexion
            cursor.execute(sqlselect)
            RSUsuarios = cursor.fetchall()
            conx.close()
            return RSUsuarios
                
        except sqlite3.OperationalError:
            print("Error de consulta")
            
    def actualizar(self, id,nom,corr,con):
        conx = self.conexionDB()
        # 2. Validar vacios
        if(id==""):
            messagebox.showwarning("Error","Ingresa un ID")
        else:
            if nom == "" or corr == "" or con == "":
                messagebox.showwarning("Aguas!!", "Formulario incompleto")
                conx.close()
            else:
                try:
                    cursor = conx.cursor()
                    conH = self.ecriptarContra(con)
                    datos = (nom, corr, conH, id)
                    sqlUpdate = "UPDATE tbRegistrados SET nombre=?, correo=?, contra=? WHERE id=?"
                    cursor.execute(sqlUpdate, datos)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Exito", "Usuario actualizado exitosamente")
                except sqlite3.OperationalError:
                    print("Error de actualización")
    
    def eliminar(self, id):
        conx = self.conexionDB()
        # 2. Validar vacios
        if(id==""):
            messagebox.showwarning("Error","Ingresa un ID")
        else:
            try:
                cursor = conx.cursor()
                sqldelete = "DELETE FROM tbRegistrados WHERE id=?"
                cursor.execute(sqldelete, id)
                sqlupdate = "UPDATE tbRegistrados SET id=id-1 WHERE id > ?"
                cursor.execute(sqlupdate, id)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito", "Usuario eliminado exitosamente")
            except sqlite3.OperationalError:
                    print("Error al eliminar")