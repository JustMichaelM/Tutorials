from kivymd.app import MDApp
from kivymd.uix.screen import Screen

from kivymd.uix.dialog import MDDialog
from kivy.uix.scrollview import ScrollView

from kivymd.uix.list import MDList,OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, OneLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.list import IconLeftWidget



class MainApp(MDApp):
    def build(self): #Build musi być i raczej nie może nazywać się inaczej
        screen = Screen()
        
        list_view = MDList()
        scroll_view = ScrollView()
        
        icon = IconLeftWidget(icon = "android") #Ikonkę trzeba dodawać do poszczególnych elementów z listy
        #Które wgl mogą ją posiadać. JEDNA IKONKA NA JEDEN ITEM!!!!

        image = ImageLeftWidget(source = "C:/Users/marcz/Desktop/Programowanie/KivyMD/templates/python-logo-only.png")



        item1 = OneLineListItem(text = "Item1")
        item2 = OneLineListItem(text = "Item2")
        item3 = TwoLineListItem(text = "To jest Two Line Item", secondary_text = "Secondary Text of Item")
        item4 = ThreeLineListItem(text = "To jest Three Line Item",
                                      secondary_text = "Second Text of Item",
                                      tertiary_text = "Third Text of Item")

        icon_item = OneLineIconListItem(text = "To jest icon item")
        icon_item.add_widget(icon) # Dodajemy ikonkę tak samo jak rzeczy do listy i rzeczy do screena
            
        list_view.add_widget(icon_item)

        avatar_item = OneLineAvatarIconListItem(text = "To jest Left Avatar Item")
        avatar_item.add_widget(image)

        list_view.add_widget(avatar_item)
        
        #jeśli chcemy dodać wiele rzeczy do listy to:
        for i in range(0,10):
            item = OneLineListItem(text = "item " + str(i))
            list_view.add_widget(item)
            
        list_view.add_widget(item1)
        list_view.add_widget(item2)
        list_view.add_widget(item3)
        list_view.add_widget(item4)

        scroll_view.add_widget(list_view)
        screen.add_widget(scroll_view)

        return screen 


MainApp().run()