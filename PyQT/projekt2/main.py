from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QVBoxLayout,QHBoxLayout, QGridLayout, QLineEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        
    def ui_init(self):
        self.buttons = [
        '7','8','9','/',
        '4','5','6','*',
        '1','2','3','-',
        '0','.','=','+'
        ]
        self.setWindowTitle("Calculator App")
        self.resize(250,300)
        
        self.grid = QGridLayout()
        self.text_box = QLineEdit()
        self.master_layout = QVBoxLayout()
        self.button_row = QHBoxLayout()

        self.clear = QPushButton("clear", self)
        self.clear.clicked.connect(self.button_click)
        
        self.delete = QPushButton("<", self)
        self.delete.clicked.connect(self.button_click)
        
        row = 0
        col = 0

        for text in self.buttons:
            self.button: QPushButton = QPushButton(text, self)
            self.button.clicked.connect(self.button_click)
            
            self.grid.addWidget(self.button,row,col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.master_layout.addWidget(self.text_box)
        self.master_layout.addLayout(self.grid)

        self.button_row.addWidget(self.clear)
        self.button_row.addWidget(self.delete)
        
        self.master_layout.addLayout(self.button_row)

        self.setLayout(self.master_layout)

    
    def button_click(self):
        button = self.sender()

        if isinstance(button, QPushButton):
            text = button.text()

        if text == '=':
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                print("Error:", e)
        
        elif text == "clear":
            self.text_box.clear()
        
        elif text == "<":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])
        
        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

def main():
    app = QApplication([])
    main_window = Window()
    main_window.show()
    app.exec_()


if __name__ == "__main__":
    main()