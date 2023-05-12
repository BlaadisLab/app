from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

Window.size = (480, 753)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

def get_ing(m):
    nitro = str(m ** 2 )
    salt = str(m ** 3)
    starts = str(m ** 4)
    dextrose = str(m ** 5)
    salting_time = str(round(m ** 6))

    return {'nitro': nitro, 'salt': salt, 'starts': starts,
            'dextrose': dextrose, 'salting_time': salting_time}

class Con(GridLayout):
    
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0
        
        ingridients = get_ing(mass)

        self.salt.text = ingridients.get('salt') 
        self.nitro.text = ingridients.get('nitro')
        
        self.dextrose.text = ingridients.get('dextrose')
        self.starts.text = ingridients.get('starts')
        self.salting_time.text = ingridients.get('salting_time')

class NaApp(App):
    def build(self):

        
        return Con()

    

if __name__ == "__main__":
    
    NaApp().run()