#interface simples de cadastro#

#importando bioblioptexcas#

import sys
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QLabel

from PyQt6.QtGui import QPixmap




app = QApplication(sys.argv)
appWindow = QWidget()
with open('style.css', 'r') as file:
    app.setStyleSheet(file.read())


appWindow.resize(400,410)
appWindow.setWindowTitle("PyCalc")


numOne = QLineEdit("")
numTwo = QLineEdit("")
operador = QLineEdit("")
soma = 0


def clear():
    textName.clear()

def addNum(x):
    textoAtual = textName.text()
    novoTexto = textoAtual + x
    textName.setText(novoTexto)

def divisao():
    numOne.setText(textName.text())
    print(numOne.text())
    operador.setText("/")
    textName.clear()
    
def soma():
    numOne.setText(textName.text())
    print(numOne.text())
    operador.setText("+")
    textName.clear()

def subtrair():
    numOne.setText(textName.text())
    print(numOne.text())
    operador.setText("-")
    textName.clear()

def multiplicar():
    numOne.setText(textName.text())
    print(numOne.text())
    operador.setText("x")
    textName.clear()

def result():
    numTwo.setText(textName.text())
    if operador.text() == "/":
        soma = float(numOne.text()) / float(numTwo.text())
        textName.setText(str(soma));

    if operador.text() == "x":
        soma = float(numOne.text()) * float(numTwo.text())
        textName.setText(str(soma))
        print(soma);

    if operador.text() == "+":
        soma = float(numOne.text()) + float(numTwo.text())
        textName.setText(str(soma));

    if operador.text() == "-":
        soma = float(numOne.text()) - float(numTwo.text())
        textName.setText(str(soma));
    


  
    



textName = QLineEdit("",appWindow)
textName.setGeometry(23,20,350,100)



btnClear = QPushButton('C', appWindow)
btnClear.setGeometry(23, 125, 40, 20)
btnClear.clicked.connect(clear)

btnOne = QPushButton('1', appWindow)
btnOne.setGeometry(23, 150, 80, 50)
btnOne.clicked.connect(lambda: addNum('1'))


btnTwo = QPushButton('2', appWindow)
btnTwo.setGeometry(110, 150, 80, 50)
btnTwo.clicked.connect(lambda: addNum('2'))


btnTree = QPushButton('3', appWindow)
btnTree.setGeometry(200, 150, 80, 50)
btnTree.clicked.connect(lambda: addNum('3'))



btnBarra = QPushButton('/', appWindow)
btnBarra.setGeometry(293, 150, 80, 50)
btnBarra.clicked.connect(divisao)


btnFour = QPushButton('4', appWindow)
btnFour.setGeometry(23, 210, 80, 50)
btnFour.clicked.connect(lambda: addNum('4'))


btnFive = QPushButton('5', appWindow)
btnFive.setGeometry(110, 210, 80, 50)
btnFive.clicked.connect(lambda: addNum('5'))


btnSix = QPushButton('6', appWindow)
btnSix.setGeometry(200, 210, 80, 50)
btnSix.clicked.connect(lambda: addNum('6'))


btnX = QPushButton('x', appWindow)
btnX.setGeometry(293, 210, 80, 50)
btnX.clicked.connect(multiplicar)


btnSeven = QPushButton('7', appWindow)
btnSeven.setGeometry(23, 270, 80, 50)
btnSeven.clicked.connect(lambda: addNum('7'))


btnEight = QPushButton('8', appWindow)
btnEight.setGeometry(110, 270, 80, 50)
btnEight.clicked.connect(lambda: addNum('8'))


btnNine = QPushButton('9', appWindow)
btnNine.setGeometry(200, 270, 80, 50)
btnNine.clicked.connect(lambda: addNum('9'))


btnMenos = QPushButton('-', appWindow)
btnMenos.setGeometry(293, 270, 80, 50)
btnMenos.clicked.connect(subtrair)


btnZero = QPushButton('0', appWindow)
btnZero.setGeometry(23, 330, 80, 50)
btnZero.clicked.connect(lambda: addNum('0'))


btnDot = QPushButton('.', appWindow)
btnDot.setGeometry(110, 330, 80, 50)
btnDot.clicked.connect(lambda: addNum('.'))


btnResult = QPushButton('=', appWindow)
btnResult.setGeometry(200, 330, 80, 50)
btnResult.clicked.connect(result)


btnMais = QPushButton('+', appWindow)
btnMais.setGeometry(293, 330, 80, 50)
btnMais.clicked.connect(soma)








img = QLabel("",appWindow)
img.setPixmap(QPixmap(""))

appWindow.show()
app.exec()