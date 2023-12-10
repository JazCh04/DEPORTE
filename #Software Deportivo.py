
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
            pantalla = BoxLayout(orientation = 'horizontal', spacing = 10, padding = (10,10,10,10))
            boton1 = Button (text = 'Iniciar sesion', size_hint_y = None,height = 50)
            boton2 = Button (text = 'Registrarse', size_hint_y = None,height = 50)
            etiqueta = Label (text = 'Athlete App') 
            pantalla.add_widget (etiqueta)

#Funcionalidad de los botones
            boton1.bind (on_press = self.accion1)    
            boton2.bind (on_press = self.accion2)

#colocar botones en la pantalla
            pantalla.add_widget (boton1)
            pantalla.add_widget (boton2)
            return pantalla
        
#Funcion para la acciones de los botones
        def accion2 (self, instance):
                #Ingresar mail, contrasena y validar longitud de la misma
                mail = input("Ingresa tu correo electrónico: ")
        while True:
                contrasena = input("Ingresa tu contraseña: ")
                if len(contrasena) < 8:
                        print ('La contrasena es demasiado corta, debe tener al menos 8 caracteres')
                else: 
                        print ('Tu registro se ha realizado correctamente')
                        break
        def accion1 (self, instance):
                ingmail = input ('Correo electronico: ')
                ingcontrasena = input ('Contrasena:  ')
        while True:
                if contrasena != contrasena:
                        print ("La contrasena no coincide. Intentalo de nuevo.")
                else: 
                        print ('Bienvenido')
                break

if __name__== "__main__":
            Simplekivy().run()