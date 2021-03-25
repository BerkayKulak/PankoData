import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QIcon
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
butonFont = QFont("Arial",12)
yaziFont= QFont("Arial",16)
from firebase import firebase
import time
import manuelsistem
import pyrebase
import live
firebase = firebase.FirebaseApplication("https://pankotek-3306f.firebaseio.com/",None)


class ToprakNem(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toprak Nem Verileri")
        self.setGeometry(50,50,800,320)
        self.setWindowIcon(QIcon("icons2/live-news.png"))
        self.setStyleSheet("background-color:#ccffff")#backgroundu oluşturmak için pencere rengi için
        self.arayuz()
        self.setFixedSize(800,320)

    def arayuz(self):




        topraknem1 = firebase.get("toprak_nem/nem1","")
        print(topraknem1)
        topraknem1 = QPushButton(str("nem1 = " + topraknem1 ),self)
        topraknem1.setStyleSheet("background-color:#F0FFF0;border: solid 2px #EE82EE;border-radius:5px;")
        topraknem1.resize(400,80)
        topraknem1.move(0,0)
        topraknem1.setFont(butonFont)
        topraknem1.setIcon(QIcon("icons2/soil.png"))


        topraknem2 = firebase.get("toprak_nem/nem2","")
        topraknem2 = QPushButton(str("nem2 = " + topraknem2 ), self)
        topraknem2.setStyleSheet("background-color:#F5FFFA;border: solid 2px #228B22;border-radius:5px;")
        topraknem2.resize(400, 80)
        topraknem2.move(400, 0)
        topraknem2.setFont(butonFont)
        topraknem2.setIcon(QIcon("icons2/soil.png"))

        topraknem3 = firebase.get("toprak_nem/nem3", "")
        topraknem3 = QPushButton(str("nem3 = " + topraknem3 ), self)
        topraknem3.setStyleSheet("background-color:#F0FFFF;border: solid 2px #006400;border-radius:5px;")
        topraknem3.resize(400, 80)
        topraknem3.move(0, 80)
        topraknem3.setFont(butonFont)
        topraknem3.setIcon(QIcon("icons2/soil.png"))

        topraknem4 = firebase.get("toprak_nem/nem4", "")
        topraknem4 = QPushButton(str("nem4 = " + topraknem4), self)
        topraknem4.setStyleSheet("background-color:#FAF0E6;border: solid 2px #ADFF2F;border-radius:5px;")
        topraknem4.resize(400, 80)
        topraknem4.move(400, 80)
        topraknem4.setFont(butonFont)
        topraknem4.setIcon(QIcon("icons2/soil.png"))


        topraknem5 = firebase.get("toprak_nem/nem5", "")
        topraknem5 = QPushButton(str("nem5 = " + topraknem5 ), self)
        topraknem5.setStyleSheet("background-color:#F8F8FF;border: solid 2px #9ACD32;border-radius:5px;")
        topraknem5.resize(400, 80)
        topraknem5.move(0, 160)
        topraknem5.setFont(butonFont)
        topraknem5.setIcon(QIcon("icons2/soil.png"))

        topraknem6 = firebase.get("toprak_nem/nem6", "")
        topraknem6 = QPushButton(str("nem6 = " + topraknem6 ), self)
        topraknem6.setStyleSheet("background-color:#FDF5E6;border: solid 2px #00FF7F;border-radius:5px;")
        topraknem6.resize(400, 80)
        topraknem6.move(400, 160)
        topraknem6.setFont(butonFont)
        topraknem6.setIcon(QIcon("icons2/soil.png"))

        topraknem7 = firebase.get("toprak_nem/nem7", "")
        topraknem7 = QPushButton(str("nem7 = " + topraknem7 ), self)
        topraknem7.setStyleSheet("background-color:#F5F5F5;border: solid 2px #90EE90;border-radius:5px;")
        topraknem7.resize(400, 80)
        topraknem7.move(0, 240)
        topraknem7.setFont(butonFont)
        topraknem7.setIcon(QIcon("icons2/soil.png"))

        topraknem8 = firebase.get("toprak_nem/nem8", "")
        topraknem8 = QPushButton(str("nem8 = " + topraknem8 ), self)
        topraknem8.setStyleSheet("background-color:#FFF5EE;border: solid 2px #3CB371;border-radius:5px;")
        topraknem8.resize(400, 80)
        topraknem8.move(400, 240)
        topraknem8.setFont(butonFont)
        topraknem8.setIcon(QIcon("icons2/soil.png"))

        self.show()





def main():
    uygulama = QApplication(sys.argv)
    pencere = ToprakNem()
    sys.exit(uygulama.exec_())

if __name__ == "__main__":
    main()



