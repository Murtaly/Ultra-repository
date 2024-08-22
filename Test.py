from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QRadioButton, QMessageBox, QLabel, QVBoxLayout, QHBoxLayout)

def show_win():
    win = QMessageBox()
    win.setWindowTitle("СБУ")
    win.setText("Правильно! Тепер ви їдете в на фронт :)")
    win.exec_()

def show_lose():
    lose = QMessageBox()
    lose.setWindowTitle("СБУ")
    lose.setText("Не правильно! Тепер ви їдете в Ґулаґ :)")
    lose.exec_()

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Nigge")
main_win.resize(800, 400)

text = QLabel("Якого року канал отримав 'золоту кнопку' від YouTube?")
butt = QRadioButton("2005")
butt1 = QRadioButton("2010")
butt2 = QRadioButton("2015")
butt3 = QRadioButton("2020")



Layout_main = QVBoxLayout()
LayoutH1 = QHBoxLayout()
LayoutH2 = QHBoxLayout()
LayoutH3 = QHBoxLayout()
LayoutH1.addWidget(text, alignment= Qt.AlignCenter)
LayoutH2.addWidget(butt, alignment= Qt.AlignCenter)
LayoutH2.addWidget(butt1, alignment= Qt.AlignCenter)
LayoutH3.addWidget(butt2, alignment= Qt.AlignCenter)
LayoutH3.addWidget(butt3, alignment= Qt.AlignCenter)

Layout_main.addLayout(LayoutH1)
Layout_main.addLayout(LayoutH2)
Layout_main.addLayout(LayoutH3)

main_win.setLayout(Layout_main)

butt2.clicked.connect(show_win)
butt.clicked.connect(show_lose)
butt3.clicked.connect(show_lose)
butt1.clicked.connect(show_lose)


main_win.show()
app.exec_()