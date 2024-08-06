from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class LubiePlackiApp(MDApp):
    def build(self):
        screen = MDScreen()
        self.toolbar = MDTopAppBar(title = "Bla")
        self.toolbar.pos_hint = {"Top": 1}
        return screen

def main():
    LubiePlackiApp().run()

if __name__ == '__main__':
    main()

