import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = qtw.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1: ")
        self.lbl_sayi1.move(50, 30)

        self.txt_sayi1 = qtw.QLineEdit(self)
        self.txt_sayi1.move(150, 30)
        self.txt_sayi1.resize(200, 32)


        self.lbl_sayi2 = qtw.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2: ")
        self.lbl_sayi2.move(50, 80)

        self.txt_sayi2 = qtw.QLineEdit(self)
        self.txt_sayi2.move(150, 80)
        self.txt_sayi2.resize(200, 32)

        self.btn_topla = qtw.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.topla)

        self.btn_cikarma= qtw.QPushButton(self)
        self.btn_cikarma.setText("Çıkarma")
        self.btn_cikarma.move(150,180)
        self.btn_cikarma.clicked.connect(self.cikarma)

        self.btn_carpma = qtw.QPushButton(self)
        self.btn_carpma.setText("Çarpma")
        self.btn_carpma.move(250,130)
        self.btn_carpma.clicked.connect(self.carpma)

        self.btn_bolme = qtw.QPushButton(self)
        self.btn_bolme.setText("Bölme")
        self.btn_bolme.move(250,180)
        self.btn_bolme.clicked.connect(self.bolme)

        self.lbl_sonuc = qtw.QLabel(self)
        self.lbl_sonuc.setGeometry(230,230,250,75)
        self.lbl_sonuc.setText("Sonuç")

    def topla(self):
        result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç: "+str(result))

    def cikarma(self):
        result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç: "+str(result))

    def bolme(self):
        result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç: "+str(result))

    def carpma(self):
        result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç: "+str(result))



def window():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

window()