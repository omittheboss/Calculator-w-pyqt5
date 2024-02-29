import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(200, 200, 500, 500)
        self.initUI()
        self.setWindowIcon(QIcon('calculator.png'))

    def initUI(self):
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText('Number 1: ')
        self.lbl_number1.move(50, 30)

        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(150, 30)
        self.txt_number1.resize(200, 32)

        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText('Number 2: ')
        self.lbl_number2.move(50, 80)

        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(150, 80)
        self.txt_number2.resize(200, 32)

        self.btn_addition = QtWidgets.QPushButton(self)
        self.btn_addition.setText('Addition')
        self.btn_addition.move(150, 130)
        self.btn_addition.clicked.connect(self.calculate)

        self.btn_substraction = QtWidgets.QPushButton(self)
        self.btn_substraction.setText('Substraction')
        self.btn_substraction.move(150, 180)
        self.btn_substraction.clicked.connect(self.calculate)

        self.btn_multiplication = QtWidgets.QPushButton(self)
        self.btn_multiplication.setText('Multiplication')
        self.btn_multiplication.move(150, 230)
        self.btn_multiplication.clicked.connect(self.calculate)

        self.btn_division = QtWidgets.QPushButton(self)
        self.btn_division.setText('Division')
        self.btn_division.move(150, 280)
        self.btn_division.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('Result: ')
        self.lbl_result.move(150, 310)

    def calculate(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Addition':
            result = int(self.txt_number1.text()) + int(self.txt_number2.text())
        elif sender == 'Substraction':
            result = int(self.txt_number1.text()) - int(self.txt_number2.text())
        elif sender == 'Multiplication':
            result = int(self.txt_number1.text()) * int(self.txt_number2.text())
        elif sender == 'Division':
            result = int(self.txt_number1.text()) / int(self.txt_number2.text())

        self.lbl_result.setText('Result: ' + str(result))

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()
