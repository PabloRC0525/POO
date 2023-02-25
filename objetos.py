from personaje import *
#Solicitar datos
print("")
print("##SOLICITUD DATOS DEL HEROE ##")
especieH = input("Escribe la especie del heroe: ")
nombreH = input("Escribe el nombre del heroe: ")
alturaH = float(input("Altura del heroe: "))
recargaH = int(input("Ingresa las balas del heroe: "))

print("")
print("##SOLICITUD DATOS DEL VILLANO ##")
especieV = input("Escribe la especie del villano: ")
nombreV = input("Escribe el nombre del villano: ")
alturaV = float(input("Altura del villano: "))
recargaV = int(input("Ingresa las balas del villano: "))
#Creamos los objetos

Heroe=Personaje(especieH,nombreH,alturaH)
Villano=Personaje(especieV,nombreV,alturaV)

print("El personaje se llama "+ nombreH)
print("El personaje pertenece a la especie "+ especieH)
print("Tiene una altura de  ",alturaH," metros")

print("El personaje se llama "+ nombreV)
print("El personaje pertenece a la especie "+ especieV)
print("Tiene una altura de  ",alturaV," metros")

#Metodos
Heroe.correr(True)
Heroe.LanzarGranadas()
Heroe.RecargarArma(recargaH)

Villano.correr(True)
Villano.LanzarGranadas()
Villano.RecargarArma(recargaV)