class Personaje:
    #atributos
    def __init__(self,esp,nom,alt):
        self.especie=esp
        self.nombre=nom
        self.altura=alt
   
    
    #metodos
    def correr(self,status):
        if (status):
            print("El personaje "+self.nombre +" esta corriendo")
        else:
            print("El personaje "+self.nombre +" se detuvo")
    def LanzarGranadas(self):
        print("Se lanzó la granada")
    def RecargarArma(self,municiones):
        cargador=10
        cargador=cargador+ municiones
        print("El arma recargada tiene ", cargador, " balas")
        