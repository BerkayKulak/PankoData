import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class harcananSuMiktari(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Harcanan Su Miktarı")
        self.setWindowIcon(QIcon("icons/liquid.ico"))
        self.setGeometry(600,350,600,450)
        self.setFixedSize(self.size())#kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):
        self.setStyleSheet("background-color:white")
        main_layout = QVBoxLayout()

        topFrame = QFrame(self)
        topFrame.setStyleSheet("background-color:white")
        top_layout = QHBoxLayout(topFrame)
        bottomFrame = QFrame(self)
        bottom_layout = QFormLayout(bottomFrame)
        bottomFrame.setStyleSheet("font:15pt Times Bold;background-color:#fcc324")

        img_book = QLabel(topFrame)
        img = QPixmap("icons/liquidps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Harcanan Su Miktarı",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.tarih_entry = QLineEdit(bottomFrame)
        self.tarih_entry.setPlaceholderText("Tarih")
        self.tarih_entry.setStyleSheet("background-color:white")
        self.harcanan_su = QLineEdit(bottomFrame)
        self.harcanan_su.setPlaceholderText("Harcanan Su")
        self.harcanan_su.setStyleSheet("background-color:white")
        self.toplam_su = QLineEdit(bottomFrame)
        self.toplam_su.setPlaceholderText("Toplam Su")
        self.toplam_su.setStyleSheet("background-color:white")
        self.ph = QLineEdit(bottomFrame)
        self.ph.setPlaceholderText("pH")
        self.ph.setStyleSheet("background-color:white")
        self.ec = QLineEdit(bottomFrame)
        self.ec.setPlaceholderText("Sıcaklık Cº-4-SAĞ")
        self.ec.setStyleSheet("background-color:white")
        add_button = QPushButton("Ekle", bottomFrame)
        add_button.clicked.connect(self.temperaturepage)
        bottom_layout.addRow(QLabel("Tarih Giriniz :"), self.tarih_entry)
        bottom_layout.addRow(QLabel("Harcanan su Giriniz1 :"), self.harcanan_su)
        bottom_layout.addRow(QLabel("Toplam su Giriniz :"), self.toplam_su)
        bottom_layout.addRow(QLabel("pH Giriniz :"), self.ph)
        bottom_layout.addRow(QLabel("ec Giriniz :"), self.ec)
        bottom_layout.addRow(QLabel(""), add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def temperaturepage(self):
        tarih = self.tarih_entry.text()
        harcanansu = self.harcanan_su.text()
        toplamsu = self.toplam_su.text()
        ph = self.ph.text()
        ec = self.ec.text()

        if (tarih and (harcanansu or toplamsu or ph or ec) != ""):
            try:
                query = "INSERT INTO 'temperature' (tarih,harcanan_su,toplam_su,pH,ec) VALUES (?,?,?,?,?)"
                cursor.execute(query, (tarih, harcanansu, toplamsu, ph, ec))
                connection.commit()
                self.tarih_entry.setText("")
                self.harcanansu.setText("")
                self.toplamsu.setText("")
                self.ph.setText("")
                self.ec.setText("")
                QMessageBox.information(self, "Su", "Su Verisi Eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Su Verisi Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")