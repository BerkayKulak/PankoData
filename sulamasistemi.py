import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

butonFont = QFont("Arial", 12)
yaziFont = QFont("Arial", 16)
from firebase import firebase
import time
import manuelsistem
import pyrebase
import live


firebase = firebase.FirebaseApplication("https://pankotek-3306f.firebaseio.com/", None)

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


# CSS CODES


class sulamaSistemi(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sulama Sistemi")
        self.setGeometry(50, 50, 800, 640)
        self.setWindowIcon(QIcon("icons2/water-pump.png"))
        self.setStyleSheet("background-color:#ccffff")  # backgroundu oluşturmak için pencere rengi için
        self.arayuz()
        self.setFixedSize(800, 640)

    def arayuz(self):

        # db.child("pankotek-3306f").update({"cati":"1"})
        # Çatı Aç
        result = firebase.get("sulamasistemi/sulama1", "")
        sulama1Ac = QPushButton(str("Sulama-1 AÇ"), self)
        sulama1Ac.setStyleSheet("background-color:#B0E0E6;")
        sulama1Ac.resize(400, 80)
        sulama1Ac.move(0, 0)
        sulama1Ac.setFont(butonFont)
        sulama1Ac.setIcon(QIcon("icons2/water-pump.png"))
        sulama1Ac.clicked.connect(self.sulama1Ac)
        # Çatı Kapat
        result = firebase.get("sulamasistemi/sulama1", "")
        sulama1Kapat = QPushButton(str("Sulama-1 KAPAT"), self)
        sulama1Kapat.setStyleSheet("background-color:#ADD8E6;")
        sulama1Kapat.resize(400, 80)
        sulama1Kapat.move(400, 0)
        sulama1Kapat.setFont(butonFont)
        sulama1Kapat.setIcon(QIcon("icons2/water-pump.png"))
        sulama1Kapat.clicked.connect(self.sulama1Kapat)
        # Fan Aç
        result = firebase.get("sulamasistemi/sulama2", "")
        sulama2Ac = QPushButton(str("Sulama-2 AÇ"), self)
        sulama2Ac.setStyleSheet("background-color:#87CEFA;")
        sulama2Ac.resize(400, 80)
        sulama2Ac.move(0, 80)
        sulama2Ac.setFont(butonFont)
        sulama2Ac.setIcon(QIcon("icons2/water-pump.png"))
        sulama2Ac.clicked.connect(self.sulama2Ac)
        # Fan Kapat
        result = firebase.get("sulamasistemi/sulama2", "")

        sulama2Kapat = QPushButton(str("Sulama-2 KAPAT"), self)
        sulama2Kapat.setStyleSheet("background-color:#87CEEB;")
        sulama2Kapat.resize(400, 80)
        sulama2Kapat.move(400, 80)
        sulama2Kapat.setFont(butonFont)
        sulama2Kapat.setIcon(QIcon("icons2/water-pump.png"))
        sulama2Kapat.clicked.connect(self.sulama2Kapat)
        # Işık Aç
        result = firebase.get("sulamasistemi/sulama3", "")

        sulama3Ac = QPushButton(str("Sulama-3 AÇ"), self)
        sulama3Ac.setStyleSheet("background-color:#00BFFF;")
        sulama3Ac.resize(400, 80)
        sulama3Ac.move(0, 160)
        sulama3Ac.setFont(butonFont)
        sulama3Ac.setIcon(QIcon("icons2/water-pump.png"))
        sulama3Ac.clicked.connect(self.sulama3Ac)
        # Işık Kapat
        result = firebase.get("sulamasistemi/sulama3", "")

        sulama3kapat = QPushButton(str("Sulama-3 KAPAT"), self)
        sulama3kapat.setStyleSheet("background-color:#B0C4DE;")
        sulama3kapat.resize(400, 80)
        sulama3kapat.move(400, 160)
        sulama3kapat.setFont(butonFont)
        sulama3kapat.setIcon(QIcon("icons2/water-pump.png"))
        sulama3kapat.clicked.connect(self.sulama3kapat)
        # Mistleme Aç
        result = firebase.get("sulamasistemi/sulama4", "")

        sulama4Ac = QPushButton(str("Sulama-4 AÇ"), self)
        sulama4Ac.setStyleSheet("background-color:#1E90FF;")
        sulama4Ac.resize(400, 80)
        sulama4Ac.move(0, 240)
        sulama4Ac.setFont(butonFont)
        sulama4Ac.setIcon(QIcon("icons2/water-pump.png"))
        sulama4Ac.clicked.connect(self.sulama4Ac)
        # Mistleme Kapat
        result = firebase.get("sulamasistemi/sulama4", "")

        sulama4kapat = QPushButton(str("Sulama-4 KAPAT"), self)
        sulama4kapat.setStyleSheet("background-color:#6495ED;")
        sulama4kapat.resize(400, 80)
        sulama4kapat.move(400, 240)
        sulama4kapat.setFont(butonFont)
        sulama4kapat.setIcon(QIcon("icons2/water-pump.png"))
        sulama4kapat.clicked.connect(self.sulama4kapat)



        result = firebase.get("sulamasistemi/sulama5", "")

        sulama5Ac = QPushButton(str("Sulama-5 AÇ"), self)
        sulama5Ac.setStyleSheet("background-color:#4682B4;")
        sulama5Ac.resize(400, 80)
        sulama5Ac.move(0, 320)
        sulama5Ac.setFont(butonFont)
        sulama5Ac.setIcon(QIcon("icons2/water-pump.png"))
        sulama5Ac.clicked.connect(self.sulama5Ac)
        # Çatı Kapat
        result = firebase.get("sulamasistemi/sulama5", "")

        sulama5Kapat = QPushButton(str("Sulama-5 KAPAT"), self)
        sulama5Kapat.setStyleSheet("background-color:#4169E1;")
        sulama5Kapat.resize(400, 80)
        sulama5Kapat.move(400, 320)
        sulama5Kapat.setFont(butonFont)
        sulama5Kapat.setIcon(QIcon("icons2/water-pump.png"))
        sulama5Kapat.clicked.connect(self.sulama5Kapat)
        # Fan Aç
        result = firebase.get("sulamasistemi/sulama6", "")

        sulama6Ac = QPushButton(str("Sulama-6 AÇ"), self)
        sulama6Ac.setStyleSheet("background-color:#0000FF;")
        sulama6Ac.resize(400, 80)
        sulama6Ac.move(0, 400)
        sulama6Ac.setFont(butonFont)
        sulama6Ac.setIcon(QIcon("icons2/water-pump.png"))
        sulama6Ac.clicked.connect(self.sulama6Ac)
        # Fan Kapat
        result = firebase.get("sulamasistemi/sulama2", "")

        sulama6Kapat = QPushButton(str("Sulama-6 KAPAT"), self)
        sulama6Kapat.setStyleSheet("background-color:#0000CD;")
        sulama6Kapat.resize(400, 80)
        sulama6Kapat.move(400, 400)
        sulama6Kapat.setFont(butonFont)
        sulama6Kapat.setIcon(QIcon("icons2/water-pump.png"))
        sulama6Kapat.clicked.connect(self.sulama6Kapat)
        # Işık Aç
        result = firebase.get("sulamasistemi/sulama6", "")

        sulama7Ac = QPushButton(str("Sulama-7 AÇ"), self)
        sulama7Ac.setStyleSheet("background-color:#00008B;")
        sulama7Ac.resize(400, 80)
        sulama7Ac.move(0, 480)
        sulama7Ac.setFont(butonFont)
        sulama7Ac.setIcon(QIcon("icons2/water-pump.png"))
        sulama7Ac.clicked.connect(self.sulama7Ac)
        # Işık Kapat
        result = firebase.get("sulamasistemi/sulama7", "")

        sulama7kapat = QPushButton(str("Sulama-7 KAPAT"), self)
        sulama7kapat.setStyleSheet("background-color:#000080;")
        sulama7kapat.resize(400, 80)
        sulama7kapat.move(400, 480)
        sulama7kapat.setFont(butonFont)
        sulama7kapat.setIcon(QIcon("icons2/water-pump.png"))
        sulama7kapat.clicked.connect(self.sulama7kapat)
        # Mistleme Aç
        result = firebase.get("sulamasistemi/sulama7", "")

        sulama8Ac = QPushButton(str("Sulama-8 AÇ"), self)
        sulama8Ac.setStyleSheet("background-color:#191970;")
        sulama8Ac.resize(400, 80)
        sulama8Ac.move(0, 560)
        sulama8Ac.setFont(butonFont)
        sulama8Ac.setIcon(QIcon("icons2/water-pump.png"))
        sulama8Ac.clicked.connect(self.sulama8Ac)
        # Mistleme Kapat
        result = firebase.get("sulamasistemi/sulama8", "")

        sulama8kapat = QPushButton(str("Sulama-8 KAPAT"), self)
        sulama8kapat.setStyleSheet("background-color:#7B68EE;")
        sulama8kapat.resize(400, 80)
        sulama8kapat.move(400, 560)
        sulama8kapat.setFont(butonFont)
        sulama8kapat.setIcon(QIcon("icons2/water-pump.png"))
        sulama8kapat.clicked.connect(self.sulama8kapat)

        self.show()

    def sulama1Ac(self):
        result = firebase.get("sulamasistemi/sulama1", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-1'i Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-1'i Açılıyor . . .")
                db.child("sulamasistemi").update({"sulama1": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-1'i Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-1 Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-1 Değişmedi")

    def sulama1Kapat(self):
        result = firebase.get("sulamasistemi/sulama1", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-1'i Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-1 Kapanıyor . . .")
                db.child("sulamasistemi").update({"sulama1": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-1 Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-1 Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-1 Değişmedi")

    def sulama2Ac(self):
        result = firebase.get("sulamasistemi/sulama2", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-2 Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-2 Açılıyor . . .")
                db.child("sulamasistemi").update({"sulama2": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-2 Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-2 Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-2 Değişmedi")

    def sulama2Kapat(self):
        result = firebase.get("sulamasistemi/sulama2", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-2'yi Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-2 Kapanıyor . . .")
                db.child("sulamasistemi").update({"sulama2": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-2 Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-2 Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-2 Değişmedi")

    def sulama3Ac(self):
        result = firebase.get("sulamasistemi/sulama3", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-3 Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-3  Açılıyor . . .")
                db.child("sulamasistemi").update({"sulama3": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-3 Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-3 Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-3 Sistemi Değişmedi")

    def sulama3kapat(self):
        result = firebase.get("sulamasistemi/sulama3", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-3'ü Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-3 Kapanıyor . . .")
                db.child("sulamasistemi").update({"sulama3": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-3 Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-3 Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-3 Sistemi Değişmedi")

    def sulama4Ac(self):
        result = firebase.get("sulamasistemi/sulama4", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-4'ü Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-4 Açılıyor . . .")
                db.child("sulamasistemi").update({"sulama4": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-4 Açlmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-4 Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Mistleme Sistemi Değişmedi")

    def sulama4kapat(self):
        result = firebase.get("sulamasistemi/sulama4", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-4'ü Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Mistleme", "Sulama-4 Kapanıyor . . .")
                db.child("sulamasistemi").update({"sulama4": "0"})
            except:
                QMessageBox.information(self, "Mistleme", "Sulama-4 Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Mistleme", "Sulama-4 Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Mistleme", "Sulama-4 Sistemi Değişmedi")

    def sulama5Ac(self):
        result = firebase.get("sulamasistemi/sulama5", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-5'i Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-5'i Açılıyor . . .")
                db.child("sulamasistemi").update({"sulama5": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-5'i Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-5 Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-5 Değişmedi")

    def sulama5Kapat(self):
        result = firebase.get("sulamasistemi/sulama5", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-5'i Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-5 Kapanıyor . . .")
                db.child("sulamasistemi").update({"sulama5": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-5 Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-5 Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-1 Değişmedi")

    def sulama6Ac(self):
        result = firebase.get("sulamasistemi/sulama6", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-6'yı Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-6 Açılıyor . . .")
                db.child("sulamasistemi").update({"sulama6": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-6 Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-6 Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-6 Değişmedi")

    def sulama6Kapat(self):
        result = firebase.get("sulamasistemi/sulama6", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-6'yı Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-6 Kapanıyor . . .")
                db.child("sulamasistemi").update({"sulama6": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-6 Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-6 Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-6 Değişmedi")

    def sulama7Ac(self):
        result = firebase.get("sulamasistemi/sulama7", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-7 Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-7  Açılıyor . . .")
                db.child("sulamasistemi").update({"sulama7": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-7 Açılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-7 Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-7 Sistemi Değişmedi")

    def sulama7kapat(self):
        result = firebase.get("sulamasistemi/sulama7", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-7'yi Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-7 Kapanıyor . . .")
                db.child("sulamasistemi").update({"sulama7": "0"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-7 Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-7 Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Sulama-7 Sistemi Değişmedi")

    def sulama8Ac(self):
        result = firebase.get("sulamasistemi/sulama8", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-8'i Açmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-8 Açılıyor . . .")
                db.child("sulamasistemi").update({"sulama8": "1"})
            except:
                QMessageBox.information(self, "Bilgi", "Sulama-8 Açlmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Bilgi", "Sulama-8 Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Bilgi", "Mistleme Sistemi Değişmedi")

    def sulama8kapat(self):
        result = firebase.get("sulamasistemi/sulama8", "")
        mbox = QMessageBox.question(self, "Uyarı", "Sulama-8'i Kapatmak İstediğinize Emin misiniz ?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                QMessageBox.information(self, "Mistleme", "Sulama-8 Kapanıyor . . .")
                db.child("sulamasistemi").update({"sulama8": "0"})
            except:
                QMessageBox.information(self, "Mistleme", "Sulama-8 Kapatılmak İstenmedi")
        elif mbox == QMessageBox.No:
            try:
                QMessageBox.information(self, "Mistleme", "Sulama-8 Sistemi Değişmedi")

            except:
                QMessageBox.information(self, "Mistleme", "Sulama-8 Sistemi Değişmedi")




def main():
    uygulama = QApplication(sys.argv)
    pencere = sulamaSistemi()
    sys.exit(uygulama.exec_())


if __name__ == "__main__":
    main()