import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class TemperaturePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sıcaklık Ekle")
        self.setWindowIcon(QIcon("icons/temperature.ico"))
        self.setGeometry(600,350,550,450)
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
        img = QPixmap("icons/sıcaklıkps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Sıcaklık ekle",topFrame)
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
        self.sicaklik_entry = QLineEdit(bottomFrame)
        self.sicaklik_entry.setPlaceholderText("Sıcaklık Cº-1-ÖN")
        self.sicaklik_entry.setStyleSheet("background-color:white")
        self.sicaklik_entry2 = QLineEdit(bottomFrame)
        self.sicaklik_entry2.setPlaceholderText("Sıcaklık Cº-2-ARKA")
        self.sicaklik_entry2.setStyleSheet("background-color:white")
        self.sicaklik_entry3 = QLineEdit(bottomFrame)
        self.sicaklik_entry3.setPlaceholderText("Sıcaklık Cº-3-SOL")
        self.sicaklik_entry3.setStyleSheet("background-color:white")
        self.sicaklik_entry4 = QLineEdit(bottomFrame)
        self.sicaklik_entry4.setPlaceholderText("Sıcaklık Cº-4-SAĞ")
        self.sicaklik_entry4.setStyleSheet("background-color:white")
        add_button = QPushButton("Ekle",bottomFrame)
        add_button.clicked.connect(self.temperaturepage)
        bottom_layout.addRow(QLabel("Tarih Giriniz :"),self.tarih_entry)
        bottom_layout.addRow(QLabel("Sıcaklık Giriniz 1 :"),self.sicaklik_entry)
        bottom_layout.addRow(QLabel("Sıcaklık Giriniz 2 :"),self.sicaklik_entry2)
        bottom_layout.addRow(QLabel("Sıcaklık Giriniz 3 :"),self.sicaklik_entry3)
        bottom_layout.addRow(QLabel("Sıcaklık Giriniz 4 :"),self.sicaklik_entry4)
        bottom_layout.addRow(QLabel(""),add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def temperaturepage(self):
        tarih = self.tarih_entry.text()
        sicaklik = self.sicaklik_entry.text()
        sicaklik2 = self.sicaklik_entry2.text()
        sicaklik3 = self.sicaklik_entry3.text()
        sicaklik4 = self.sicaklik_entry4.text()


        if (tarih and (sicaklik or sicaklik2 or sicaklik3 or sicaklik4) != ""):
            try:
                query = "INSERT INTO 'temperature' (tarih,sicaklik,sicaklik2,sicaklik3,sicaklik4) VALUES (?,?,?,?,?)"
                cursor.execute(query,(tarih,sicaklik,sicaklik2,sicaklik3,sicaklik4))
                connection.commit()
                self.tarih_entry.setText("")
                self.sicaklik_entry.setText("")
                self.sicaklik_entry2.setText("")
                self.sicaklik_entry3.setText("")
                self.sicaklik_entry4.setText("")
                QMessageBox.information(self,"Sıcaklık","Sıcaklık eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Sıcaklık Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")

