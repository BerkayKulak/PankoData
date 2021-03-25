import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import main


fontTitle = QFont("Arial",24)
fontText = QFont("Arial",18)


class Help(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hakkımızda")
        self.setWindowIcon(QIcon("icons/about.ico"))
        self.setGeometry(200,200,250,250)
        self.UI()

    def UI(self):
        self.setStyleSheet("background-color:white")
        vbox = QVBoxLayout(self)
        textTitle = QLabel("Hakkımızda")
        textHakkimizda = QLabel("""Hezarfen Drone olarak Hazırlık sınıfında bu işlere adım atmış bulunmaktayız. 
                            \nEkibimiz hedefleri doğrultusunda çalışmalarını düzenlemektedir. Şuanda Akıllı
                            \nSera projesinde gönüllü olarak çalışmaktadırlar. Akademik Görevlimiz Hasan Basri
                            \nve Harun Meral Hocalarımıza sonsuz teşekkürlerimizi iletiyoruz.""")
        textTitle.setFont(fontTitle)
        textHakkimizda.setFont(fontText)
        vbox.addWidget(textTitle)
        vbox.addWidget(textHakkimizda)
        self.setLayout(vbox)







