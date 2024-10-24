from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDIcon

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    
    MDLabel:
        text: "To jest MDLabel"
        halign: "center"
"""


class MyKivyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        label = MDLabel()
        print(help(label))
        

        return Builder.load_string(KV)
    
MyKivyApp().run()