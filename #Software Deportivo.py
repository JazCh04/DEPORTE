
#Bienvenida
print ("Bienvenid@ a la aplicación FitEnergy")

#Extraer etiqueta de los paquetes UIX de Kivy
from kivy.uix.label import Label

#Crear aplicación principal
class SimpleKivy:
    def build(self):
         return Label(text="Bienvenido")
