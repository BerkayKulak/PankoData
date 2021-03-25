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
import sulamasistemi

firebase = firebase.FirebaseApplication("https://pankotek-3306f.firebaseio.com/",None)

firebaseConfig = {
    "apiKey": "AIzaSyDgxEV3FGL4f2b5Lf0Tk-IQu0FaNy-2MZY",
    "authDomain": "pankotek-3306f.firebaseapp.com",
    "databaseURL": "https://pankotek-3306f.firebaseio.com",
    "projectId": "pankotek-3306f",
    "storageBucket": "pankotek-3306f.appspot.com",
    "messagingSenderId": "722491833362",
    "appId": "1:722491833362:web:e91ec344b9a1a74a022ccb"
  }

firebase2 = pyrebase.initialize_app(firebaseConfig)
db = firebase2.database()

#CSS CODES



class Manuel(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KONTROL SİSTEMLERİ")
        self.setGeometry(50,50,800,400)
        self.setWindowIcon(QIcon("icons2/home-automation.png"))
        self.setStyleSheet("background-color:#ccffff")#backgroundu oluşturmak için pencere rengi için
        self.arayuz()
        self.setFixedSize(800,400)

    def arayuz(self):


        #db.child("pankotek-3306f").update({"cati":"1"})
        #Çatı Aç
        result = firebase.get("cati", "")
        print(result)
        catiac = QPushButton(str("Sera Çatısı AÇ"),self)
        catiac.setStyleSheet("background-color:	#FFF8DC;")
        catiac.resize(400,80)
        catiac.move(0,0)
        catiac.setFont(butonFont)
        catiac.setIcon(QIcon("icons2/catiac.png"))
        catiac.clicked.connect(self.catiAc)
        #Çatı Kapat
        result = firebase.get("cati", "")
        print(result)
        catikapat = QPushButton(str("Sera Çatısı KAPAT"), self)
        catikapat.setStyleSheet("background-color:#800000;")
        catikapat.resize(400, 80)
        catikapat.move(400, 0)
        catikapat.setFont(butonFont)
        catikapat.setIcon(QIcon("icons2/catiac.png"))
        catikapat.clicked.connect(self.catiKapat)
        #Fan Aç
        result = firebase.get("fan", "")
        print(result)
        fanAc = QPushButton(str("Fanları AÇ"), self)
        fanAc.setStyleSheet("background-color:#FFEBCD;")
        fanAc.resize(400, 80)
        fanAc.move(0, 80)
        fanAc.setFont(butonFont)
        fanAc.setIcon(QIcon("icons2/fan_sistem.png"))
        fanAc.clicked.connect(self.FanAc)
        #Fan Kapat
        result = firebase.get("fan", "")
        print(result)
        fanKapat = QPushButton(str("Fanları KAPAT"), self)
        fanKapat.setStyleSheet("background-color:#A52A2A;")
        fanKapat.resize(400, 80)
        fanKapat.move(400, 80)
        fanKapat.setFont(butonFont)
        fanKapat.setIcon(QIcon("icons2/fan_sistem.png"))
        fanKapat.clicked.connect(self.FanKapat)
        #Işık Aç
        result = firebase.get("isik", "")
        print(result)
        isikAc = QPushButton(str("Işıkları AÇ"), self)
        isikAc.setStyleSheet("background-color:#FFDEAD;")
        isikAc.resize(400, 80)
        isikAc.move(0, 160)
        isikAc.setFont(butonFont)
        isikAc.setIcon(QIcon("icons2/smart-farm.png"))
        isikAc.clicked.connect(self.IsikAc)
        # Işık Kapat
        result = firebase.get("isik", "")
        print(result)
        isikKapat = QPushButton(str("Işıkları Kapat"), self)
        isikKapat.setStyleSheet("background-color:#A0522D;")
        isikKapat.resize(400, 80)
        isikKapat.move(400, 160)
        isikKapat.setFont(butonFont)
        isikKapat.setIcon(QIcon("icons2/smart-farm.png"))
        isikKapat.clicked.connect(self.IsikKapat)
        # Mistleme Aç
        result = firebase.get("mistleme", "")
        print(result)
        mistlemeAc = QPushButton(str("Mistleme AÇ"), self)
        mistlemeAc.setStyleSheet("background-color:#DEB887;")
        mistlemeAc.resize(400, 80)
        mistlemeAc.move(0, 240)
        mistlemeAc.setFont(butonFont)
        mistlemeAc.setIcon(QIcon("icons2/hose.png"))
        mistlemeAc.clicked.connect(self.mistlemeAc)
        # Mistleme Kapat
        result = firebase.get("mistleme", "")
        print(result)
        mistlemeKapat = QPushButton(str("Mistleme KAPAT"), self)
        mistlemeKapat.setStyleSheet("background-color:#D2691E;")
        mistlemeKapat.resize(400, 80)
        mistlemeKapat.move(400, 240)
        mistlemeKapat.setFont(butonFont)
        mistlemeKapat.setIcon(QIcon("icons2/hose.png"))
        mistlemeKapat.clicked.connect(self.mistlemeKapat)
        result = firebase.get("mistleme", "")

        sulamaSistemi =  QPushButton("Sulama Sistemine Git", self)
        sulamaSistemi.setStyleSheet("background-color:#BC8F8F;")
        sulamaSistemi.resize(800, 80)
        sulamaSistemi.move(0, 320)
        sulamaSistemi.setFont(butonFont)
        sulamaSistemi.setIcon(QIcon("icons2/water-pump.png"))
        sulamaSistemi.clicked.connect(self.SulamaSistemi)








        self.show()


    def catiAc(self):
        result = firebase.get("cati", "")
        mbox = QMessageBox.question(self,"Uyarı","Çatıyı Açmak İstediğinize Emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self,"Bilgi","Çatı Açılıyor . . .")
                db.update({"cati": "1"})
            except:
                QMessageBox.information(self,"Bilgi","Çatı Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self,"Bilgi", "Çatı Sistemi Değişmedi")

            except:
                QMessageBox.information( self,"Bilgi","Çatı Sistemi Değişmedi")


    def catiKapat(self):
        result = firebase.get("cati", "")
        mbox = QMessageBox.question(self, "Uyarı", "Çatıyı Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Çatı Kapanıyor . . .")
                db.update({"cati": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Çatı Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Çatı Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Çatı Sistemi Değişmedi")

    def FanAc(self):
        result = firebase.get("fan", "")
        mbox = QMessageBox.question(self, "Uyarı", "Fanları Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Fanlar Açılıyor . . .")
                db.update({"fan": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Fanlar Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Fanlar Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Fanlar Sistemi Değişmedi")


    def FanKapat(self):
        result = firebase.get("fan", "")
        mbox = QMessageBox.question(self, "Uyarı", "Fanları Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Fanlar Kapanıyor . . .")
                db.update({"fan": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Fanlar Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Fan Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Fan Sistemi Değişmedi")
    def IsikAc(self):
        result = firebase.get("isik", "")
        mbox = QMessageBox.question(self, "Uyarı", "Işıkları Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Işıklar Açılıyor . . .")
                db.update({"isik": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Işıklar Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Işık Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Işık Sistemi Değişmedi")

    def IsikKapat(self):
        result = firebase.get("isik", "")
        mbox = QMessageBox.question(self, "Uyarı", "Işıkları Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Işıklar Kapanıyor . . .")
                db.update({"isik": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Işıklar Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Işık Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Işık Sistemi Değişmedi")

    def mistlemeAc(self):
        result = firebase.get("mistleme", "")
        mbox = QMessageBox.question(self, "Uyarı", "Mistlemeyi Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Mistleme Açılıyor . . .")
                db.update({"mistleme": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Mistleme Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Mistleme Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Mistleme Sistemi Değişmedi")
    def mistlemeKapat(self):
        result = firebase.get("mistleme", "")
        mbox = QMessageBox.question(self, "Uyarı", "Mistlemeyi Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Mistleme", "Mistleme Kapanıyor . . .")
                db.update({"mistleme": "0"})
            except:
                QMessageBox.information(self, "Mistleme", "Mistleme Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Mistleme", "Mistleme Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Mistleme", "Mistleme Sistemi Değişmedi")

    def SulamaSistemi(self):
        self.ayarla3 = sulamasistemi.sulamaSistemi()
        self.ayarla3.show()

def main():
    uygulama = QApplication(sys.argv)
    pencere = Manuel()
    sys.exit(uygulama.exec_())

if __name__ == "__main__":
    main()