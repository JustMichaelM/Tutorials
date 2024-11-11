from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout
import random 



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")
        self.resize(300,200)

    def window_random_background(self):
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.setStyleSheet(f"background-color: rgb({self.r},{self.g},{self.b});")


def main():
    app = QApplication([])

    title = QLabel("Random Things")
    text1 = QLabel("?")
    text2 = QLabel("?")
    text3 = QLabel("?")

    button1 = QPushButton("Click Me!")
    button2 = QPushButton("Click Me!")
    button3 = QPushButton("Click Me!")
    
    master_layout = QVBoxLayout()

    row1 = QHBoxLayout()
    row2 = QHBoxLayout()
    row3 = QHBoxLayout()
    main_window = Window()

    row1.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter) 
    row2.addWidget(text1, alignment=Qt.AlignmentFlag.AlignCenter)
    row2.addWidget(text2, alignment=Qt.AlignmentFlag.AlignCenter)
    row2.addWidget(text3, alignment=Qt.AlignmentFlag.AlignCenter)

    row3.addWidget(button1)
    row3.addWidget(button2)
    row3.addWidget(button3)

    master_layout.addLayout(row1)
    master_layout.addLayout(row2)
    master_layout.addLayout(row3)

    main_window.setLayout(master_layout)
    button2.clicked.connect(main_window.window_random_background)

    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()
