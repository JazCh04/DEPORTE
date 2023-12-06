
#Importar marcos para app y widget de diseño
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#Importar etiqueta de los paquetes UIX, botones y textos
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from functools import partial

#Importar interfaz para web de usuarios
import webbrowser

#Crear pantalla
class SimpleScreen (BoxLayout):
    def _init_(self,**kwargs):
        super (SimpleScreen, self)._init_(**kwargs)
        self.orientacion = 'vertical'
        self.add_widget(Label(text = 'Bienvenid@ a la aplicación FitEnergy'))   

#Mantener la pantalla abierta
while True:
    class SimpleApp (App):
        def build(self):
            return SimpleScreen ()
    
    if __name__ =='_main_':
        SimpleApp().run()

#Colocar boton visualizacion en el menu principal
class MyButton (Button):
    #_int_ inicializar los atributos de la clase my button
    def _int_(self,**kwargs):
        super(MyButton,self)._int_(**kwargs)
        self.text = 'Visualizacion'
        self.size_hint = (0.2, 0.2)
        self.post_hint = {0.4, 0.4}
        self.blind(on_press=self.imprimir_mensaje)

class MyApp(App):
    def build(self):
        return MyButton()
    
#Colocar boton registro en el menu principal
class MyButton (Button):
    #_int_ inicializar los atributos de la clase my button
    def _int_(self,**kwargs):
        super(MyButton,self)._int_(**kwargs)
        self.text = 'Registro'
        self.size_hint = (0.2, 0.2)
        self.post_hint = {0.4, 0.4}
        self.blind(on_press=self.imprimir_mensaje)

class MyApp(App):
    def build(self):
        return MyButton()