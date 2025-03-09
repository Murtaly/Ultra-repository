from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QRadioButton, QLCDNumber, QMessageBox, QLabel, QVBoxLayout, QHBoxLayout)

global a, n, b, m, l
a = "0"
n = "0"
b = "0"
m = "0"
l = "0"

def one():
    global a
    if a == "0":
        a = "1"
    else:
        a = a + "1"
    output_txt.display(a)

def two():
    global a
    if a == "0":
        a = "2"
    else:
        a = a + "2"
    output_txt.display(a)

def three():
    global a
    if a == "0":
        a = "3"
    else:
        a = a + "3"
    output_txt.display(a)  

def four():
    global a
    if a == "0":
        a = "4"
    else:
        a = a + "4"
    output_txt.display(a)       

def five():
    global a
    if a == "0":
        a = "5"
    else:
        a = a + "5"
    output_txt.display(a)

def six():
    global a
    if a == "0":
        a = "6"
    else:
        a = a + "6"
    output_txt.display(a)

def seven():
    global a
    if a == "0":
        a = "7"
    else:
        a = a + "7"
    output_txt.display(a)

def eight():
    global a
    if a == "0":
        a = "8"
    else:
        a = a + "8"
    output_txt.display(a)

def nine():
    global a
    if a == "0":
        a = "9"
    else:
        a = a + "9"
    output_txt.display(a)

def plus():
    global a, n
    n = a
    a = "0"
    output_txt.display(a)

def minus():
    global a, b
    b = a
    a = "0"
    output_txt.display(a)

def multi():
    global a, m
    m = a
    a = "0"
    output_txt.display(a)

def divide():
    global a, l
    l = a
    a = "0"
    output_txt.display(a)

def equal():
    global a, n, b, m, l
    if n != "0":
        n = int(n)
        a = int(a)
        a = n + a
        a = str(a)
        n = "0"
    elif b != "0":
        b = int(b)
        a = int(a)
        a = b - a
        a = str(a)
        b = "0"
    elif m != "0":
        m = int(m)
        a = int(a)
        a = m * a
        a = str(a)
        m = "0"
    elif l != "0":
        l = int(l)
        a = int(a)
        a = l / a
        a = str(a)
        l = "0"

    output_txt.display(a)
    
QLCDlen = 15

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Calculator Sanyochka")
main_win.resize(400, 600)

output_txt = QLCDNumber(QLCDlen)
butt1 = QPushButton("1")
butt2 = QPushButton("2")
butt3 = QPushButton("3")
butt4 = QPushButton("4")
butt5 = QPushButton("5")
butt6 = QPushButton("6")
butt7 = QPushButton("7")
butt8 = QPushButton("8")
butt9 = QPushButton("9")
buttPlus = QPushButton("+")
buttMinus = QPushButton("-")
buttmulti = QPushButton("*")
buttdivide = QPushButton("/")
buttEqual = QPushButton("=")

Layout_main = QVBoxLayout()
LayoutH1 = QHBoxLayout()
LayoutH2 = QHBoxLayout()
LayoutH3 = QHBoxLayout()
LayoutH4 = QHBoxLayout()
LayoutH5 = QHBoxLayout()
LayoutH6 = QHBoxLayout()

LayoutH1.addWidget(output_txt, alignment= Qt.AlignCenter)
LayoutH2.addWidget(butt1, alignment= Qt.AlignCenter)
LayoutH2.addWidget(butt2, alignment= Qt.AlignCenter)
LayoutH2.addWidget(butt3, alignment= Qt.AlignCenter)
LayoutH3.addWidget(butt4, alignment= Qt.AlignCenter)
LayoutH3.addWidget(butt5, alignment= Qt.AlignCenter)
LayoutH3.addWidget(butt6, alignment= Qt.AlignCenter)
LayoutH4.addWidget(butt7, alignment= Qt.AlignCenter)
LayoutH4.addWidget(butt8, alignment= Qt.AlignCenter)
LayoutH4.addWidget(butt9, alignment= Qt.AlignCenter)
LayoutH5.addWidget(buttPlus, alignment= Qt.AlignCenter)
LayoutH5.addWidget(buttMinus, alignment= Qt.AlignCenter)
LayoutH5.addWidget(buttEqual, alignment= Qt.AlignCenter)
LayoutH6.addWidget(buttmulti, alignment= Qt.AlignCenter)
LayoutH6.addWidget(buttdivide, alignment= Qt.AlignCenter)

Layout_main.addLayout(LayoutH1)
Layout_main.addLayout(LayoutH2)
Layout_main.addLayout(LayoutH3)
Layout_main.addLayout(LayoutH4)
Layout_main.addLayout(LayoutH5)
Layout_main.addLayout(LayoutH6)

main_win.setLayout(Layout_main)

butt1.clicked.connect(one)
butt2.clicked.connect(two)
butt3.clicked.connect(three)
butt4.clicked.connect(four)
butt5.clicked.connect(five)
butt6.clicked.connect(six)
butt7.clicked.connect(seven)
butt8.clicked.connect(eight)
butt9.clicked.connect(nine)
buttPlus.clicked.connect(plus)
buttMinus.clicked.connect(minus)
buttmulti.clicked.connect(multi)
buttdivide.clicked.connect(divide)
buttEqual.clicked.connect(equal)

output_txt.display(a)

main_win.show()
app.exec_()