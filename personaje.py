class Personaje:
    #atributos
    def __init__(self,esp,nom,alt):
        self.__especie=esp
        self.__nombre=nom
        self.__altura=alt
   
    
    #metodos
    def correr(self,status):
        if (status):
            print("El personaje "+self.__nombre +" esta corriendo")
        else:
            print("El personaje "+self.__nombre +" se detuvo")
    def LanzarGranadas(self):
        print("Se lanzó la granada")
    def RecargarArma(self,municiones):
        cargador=10
        cargador=cargador+ municiones
        print("El arma recargada tiene ", cargador, " balas")
        
    def __pensar(self):
        print("Estoy pensando.........")
    def getEspecie(self):
        return self.__especie
    def setEspecie(self,esp):
        self.__especie=esp
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nom):
        self._nombre=nom
    def getAltura(self):
        return self.__altura
    def setAltura(self,alt):
        self.__altura=alt
    