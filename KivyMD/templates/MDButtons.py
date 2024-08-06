from kivymd.app import MDApp
from kivymd.uix.screen import Screen

from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class mainApp(MDApp):
    def build(self):
        screen = Screen()
                
        #Zmiana Theme'u
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "A400"
        self.theme_cls.theme_style = "Light"
        #Ważna rzecz dodawać na początku obiekt typu klasy

        #Tworzenie buttona i dodawanie go do obiektu screen
        btn_flat = MDRectangleFlatButton(text = "Hello World", 
                                pos_hint = {"center_x": 0.5, "center_y": 0.5})
        screen.add_widget(btn_flat)
        
        icon_btn = MDIconButton(icon = "android",pos_hint = {"center_x": 0.5, "center_y": 0.3})
        screen.add_widget(icon_btn)
        
        action_btn = MDFloatingActionButton(icon = "language_python",pos_hint = {"center_x": 0.5, "center_y": 0.1})
        screen.add_widget(action_btn)

        return screen
    
mainApp().run()