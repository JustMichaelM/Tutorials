from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem

list = """
Screen:
    ScrollView:
        MDList:
            OneLineListItem:
                text: "Item 1"
            OneLineListItem:
                text: "Item 2"
"""

for_list = """
Screen:
    ScrollView:
        MDList:
            id: for_list
"""

class MainApp(MDApp):
    def build(self): #Build musi być i raczej nie może nazywać się inaczej
        #screen = Builder.load_string(list) #To nadpisuje typową klasę Screen
        screen = Builder.load_string(for_list)

        return screen 

    def on_start(self):
        for i in range(20):
            item = OneLineListItem(text = "Item" + str(i))
            self.root.ids.for_list.add_widget(item) #To jest formułka która odwołuje się do ID danego przedmiotu

MainApp().run()