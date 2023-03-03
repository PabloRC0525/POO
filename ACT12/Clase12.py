from tkinter import messagebox
class Validacion:
    def __init__(self,corr, passw,word1,word2):
        self.corr = corr
        self.passw = passw
        self.word1 = word1
        self.word2 = word2
    def validar(self):
        if self.corr.get() == self.word1 and self.passw.get()==self.word2:
            messagebox.showinfo("Correcto","Se ha iniciado sesion correctamente")
        else:
            messagebox.showerror("Error","Usuario o contraseña incorrectos")
