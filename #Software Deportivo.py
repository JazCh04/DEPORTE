
#Importar marcos para app y widget de diseño
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#Importar etiqueta de los paquetes UIX, botones y textos
from kivy.uix.label import Label
from kivy.uix.button import Button
#Crear pantalla y mantenerla abierta mientras se ejecuta
#Definir variables para retornar las clases
class Simplekivy (App):
        def build (self):
            contenedor = BoxLayout(orientation = 'horizontal', spacing = 10, padding = (10,10,10,10))
            boton1 = Button (text = 'Visualizar', size_hint_y = None,height = 50)
            boton2 = Button (text = 'Registrarse', size_hint_y = None,height = 50)
            etiqueta = Label (text = 'Bienvenid@ a la aplicación FitEnergy') 
            contenedor.add_widget (etiqueta)

#Funcionalidad de los botones
            boton1.bind (on_press = self.accion1)
            boton2.bind (on_press = self.accion2)

#colocar botones en el pie de pagina
            contenedor.add_widget (boton1)
            contenedor.add_widget (boton2)
            return contenedor
        
#Funcion para la acciones de los botones
        def accion1 (self, instance):
                print ("Hola Jaz")
        def accion2 (self, instance):
                print ("Hola Migue")

if __name__== "__main__":
            Simplekivy().run()