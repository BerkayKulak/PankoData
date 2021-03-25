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
import topraknem

firebase = firebase.FirebaseApplication("https://pankotek-3306f.firebaseio.com/",None)


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ANLIK VERİ")
        self.setGeometry(50,50,800,480)
        self.setWindowIcon(QIcon("icons2/live-news.png"))
        self.setStyleSheet("background-color:#ccffff")#backgroundu oluşturmak için pencere rengi için
        self.arayuz()
        self.setFixedSize(800,480)

    def arayuz(self):




        co2 = firebase.get("co2","")
        print(co2)
        co2 = QPushButton(str("co2 = " + co2 + " %"),self)
        co2.setStyleSheet("background-color:#7CFC00;border: solid 2px #EE82EE;border-radius:5px;")
        co2.resize(400,80)
        co2.move(0,0)
        co2.setFont(butonFont)
        co2.setIcon(QIcon("icons2/co2_live.png"))


        hava_nem = firebase.get("havanem","")
        hava_nem = QPushButton(str("hava nemi = " + hava_nem + " %"), self)
        hava_nem.setStyleSheet("background-color:#228B22;border: solid 2px #228B22;border-radius:5px;")
        hava_nem.resize(400, 80)
        hava_nem.move(400, 0)
        hava_nem.setFont(butonFont)
        hava_nem.setIcon(QIcon("icons2/humidity.png"))

        isik_yogunlugu = firebase.get("isik_yogunlugu", "")
        isik_yogunlugu = QPushButton(str("Işık Yoğunluğu = " + isik_yogunlugu + " lux"), self)
        isik_yogunlugu.setStyleSheet("background-color:#006400;border: solid 2px #006400;border-radius:5px;")
        isik_yogunlugu.resize(400, 80)
        isik_yogunlugu.move(0, 80)
        isik_yogunlugu.setFont(butonFont)
        isik_yogunlugu.setIcon(QIcon("icons2/light-bulb.png"))

        isitici_sicakligi = firebase.get("isitici_sicakligi", "")
        isitici_sicakligi = QPushButton(str("Isıtıcı Sıcaklığı = " + isitici_sicakligi + " °C"), self)
        isitici_sicakligi.setStyleSheet("background-color:#ADFF2F;border: solid 2px #ADFF2F;border-radius:5px;")
        isitici_sicakligi.resize(400, 80)
        isitici_sicakligi.move(400, 80)
        isitici_sicakligi.setFont(butonFont)
        isitici_sicakligi.setIcon(QIcon("icons2/heater.png"))


        sicaklik = firebase.get("sicaklik", "")
        sicaklik = QPushButton(str("Hava Sıcaklığı = " + sicaklik + " °C"), self)
        sicaklik.setStyleSheet("background-color:#9ACD32;border: solid 2px #9ACD32;border-radius:5px;")
        sicaklik.resize(400, 80)
        sicaklik.move(0, 160)
        sicaklik.setFont(butonFont)
        sicaklik.setIcon(QIcon("icons2/temperature.png"))

        su_kalitesi = firebase.get("su_kalitesi", "")
        su_kalitesi = QPushButton(str("Su Kalitesi = " + su_kalitesi + " ppm"), self)
        su_kalitesi.setStyleSheet("background-color:#00FF7F;border: solid 2px #00FF7F;border-radius:5px;")
        su_kalitesi.resize(400, 80)
        su_kalitesi.move(400, 160)
        su_kalitesi.setFont(butonFont)
        su_kalitesi.setIcon(QIcon("icons2/water.png"))

        suseviye = firebase.get("suseviye", "")
        suseviye = QPushButton(str("Su Seviye = " + suseviye + " cm"), self)
        suseviye.setStyleSheet("background-color:#90EE90;border: solid 2px #90EE90;border-radius:5px;")
        suseviye.resize(400, 80)
        suseviye.move(0, 240)
        suseviye.setFont(butonFont)
        suseviye.setIcon(QIcon("icons2/water-level.png"))

        suyun_ph = firebase.get("suyun_ph", "")
        suyun_ph = QPushButton(str("Su pH = " + suyun_ph + " pH"), self)
        suyun_ph.setStyleSheet("background-color:#3CB371;border: solid 2px #3CB371;border-radius:5px;")
        suyun_ph.resize(400, 80)
        suyun_ph.move(400, 240)
        suyun_ph.setFont(butonFont)
        suyun_ph.setIcon(QIcon("icons2/ph.png"))

        Yönet = QPushButton("Topran Nem Verilerini Göster", self)
        Yönet.setStyleSheet("background-color:#808000;")
        Yönet.resize(800, 80)
        Yönet.move(0, 320)
        Yönet.setFont(butonFont)
        Yönet.setIcon(QIcon("icons2/soil.png"))
        Yönet.clicked.connect(self.toprakNem)


        Yönet = QPushButton("Kontrol Sistemlerine Git", self)
        Yönet.setStyleSheet("background-color:#BC8F8F;")
        Yönet.resize(800, 80)
        Yönet.move(0, 400)
        Yönet.setFont(butonFont)
        Yönet.setIcon(QIcon("icons2/ph.png"))
        Yönet.clicked.connect(self.Yonet)

        self.show()

    def Yonet(self):
        self.ayarla = manuelsistem.Manuel()
        self.ayarla.show()
    def toprakNem(self):
        self.ayarla1 = topraknem.ToprakNem()
        self.ayarla1.show()



def main():
    uygulama = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(uygulama.exec_())

if __name__ == "__main__":
    main()



