from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDButton
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer

username_string = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "Forgot username?"
    helper_text_mode: "on_focus"
    icon_right: "android" 
    pos_hint: {"center_x": 0.5, "center_y": 0.9}
    size_hint_x: None
    width: 300
"""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "A400"
        self.theme_cls.theme_style = "Light"

        screen = Screen()
        
        self.username = Builder.load_string(username_string)
        screen.add_widget(self.username)
        
        button = MDButton(_button_text = "Show", pos_hint = {'center_x': 0.5, 'center_y': 0.8}, on_release = self.show_data) #on_release to specjalny parametr do którego dodajemy metodę (to co ma się dziać po kliknięciu). Konieczne jest słówko 'self'
        screen.add_widget(button)

        return screen
    
    #Zawsze musi być 'self' - co jest oczywiste oraz 'obj' (object) co jest mniej oczywiste.
    def show_data(self):
        dialog = MDDialog(
                            MDDialogHeadlineText(
                                text = "Czy Lubisz Placki?",
                                halign = "left",
                            ),
                        )
        dialog.open()

MainApp().run()