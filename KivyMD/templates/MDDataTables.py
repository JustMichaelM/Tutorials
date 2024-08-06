from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp #dp - display size

class mainApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(
            pos_hint = {'center_x':0.5, 'center_y': 0.5},
            size_hint = (0.9,0.6),
            check = True,
            rows_num = 10, 
            column_data = [
                ("No.", dp(30)),
                ("food", dp(30)),
                ("calories", dp(30))
            ],
            row_data = [
                ("1","Apple", 100),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300),
                ("2","Burger", 300)
            ])
        
        #dodawanie funkcji do tabelki.
        table.bind(on_check_press = self.check_press)
        table.bind(on_row_press = self.row_press)

        screen.add_widget(table)
        return screen
    
    def check_press(self,instance_table,current_row):
        print(instance_table,current_row)

    def row_press(self,instance_table,instance_row):
        print(instance_table,instance_row)

mainApp().run()