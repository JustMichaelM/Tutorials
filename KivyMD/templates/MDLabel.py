#NAJWAŻNIEJSZE IMPORTY APLIKACJI
#EWNTUALNIE JESZCZE BUILDER
from kivymd.app import MDApp
from kivymd.uix.screen import Screen

#IMPORT PÓL TEKSTOWYCH
from kivymd.uix.label import MDLabel, MDIcon

class mainApp(MDApp):
    def build(self):
        screen = Screen()
        
        #Zabawy z tekstem
        text = MDLabel(text = "Hello World", halign = "center",
                       theme_text_color = "Custom",text_color = ("#54f542"),
                       font_style = "H1")
        screen.add_widget(text)

        #Nie wiem jak ustawiać ikonki :/
        #Prawdopodbnie builderem
        icon = MDIcon(icon = "check-circle")
        screen.add_widget(icon)

        return screen
    
mainApp().run()