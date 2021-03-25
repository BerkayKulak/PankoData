import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class HumidityPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nem Verisi Ekle")
        self.setWindowIcon(QIcon("icons/topraknemi.ico"))
        self.setGeometry(600,350,650,550)
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
        img = QPixmap("icons/Topraknemips.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Nem Verisi Ekle",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.humidity_tarih_entry = QLineEdit(bottomFrame)
        self.humidity_tarih_entry.setPlaceholderText("Tarih")
        self.humidity_tarih_entry.setStyleSheet("background-color:white")
        self.nem_entry = QLineEdit(bottomFrame)
        self.nem_entry.setPlaceholderText("1.Saksı Nem %")
        self.nem_entry.setStyleSheet("background-color:white")
        self.nem_entry2 = QLineEdit(bottomFrame)
        self.nem_entry2.setPlaceholderText("2.Saksı Nem %")
        self.nem_entry2.setStyleSheet("background-color:white")
        self.nem_entry3 = QLineEdit(bottomFrame)
        self.nem_entry3.setPlaceholderText("3.Saksı Nem %")
        self.nem_entry3.setStyleSheet("background-color:white")
        self.nem_entry4 = QLineEdit(bottomFrame)
        self.nem_entry4.setPlaceholderText("4.Saksı Nem %")
        self.nem_entry4.setStyleSheet("background-color:white")
        self.nem_entry5 = QLineEdit(bottomFrame)
        self.nem_entry5.setPlaceholderText("5.Saksı Nem %")
        self.nem_entry5.setStyleSheet("background-color:white")
        self.nem_entry6 = QLineEdit(bottomFrame)
        self.nem_entry6.setPlaceholderText("6.Saksı Nem %")
        self.nem_entry6.setStyleSheet("background-color:white")
        self.nem_entry7 = QLineEdit(bottomFrame)
        self.nem_entry7.setPlaceholderText("7.Saksı Nem %")
        self.nem_entry7.setStyleSheet("background-color:white")
        self.nem_entry8 = QLineEdit(bottomFrame)
        self.nem_entry8.setPlaceholderText("8.Saksı Nem %")
        self.nem_entry8.setStyleSheet("background-color:white")
        humidity_add_button = QPushButton("Ekle",bottomFrame)
        humidity_add_button.clicked.connect(self.humiditypage)
        bottom_layout.addRow(QLabel("Tarih Giriniz :"),self.humidity_tarih_entry)
        bottom_layout.addRow(QLabel("1.Saksı Nemi Giriniz :"),self.nem_entry)
        bottom_layout.addRow(QLabel("2.Saksı Nemi Giriniz :"), self.nem_entry2)
        bottom_layout.addRow(QLabel("3.Saksı Nemi Giriniz :"), self.nem_entry3)
        bottom_layout.addRow(QLabel("4.Saksı Nemi Giriniz :"), self.nem_entry4)
        bottom_layout.addRow(QLabel("5.Saksı Nemi Giriniz :"), self.nem_entry5)
        bottom_layout.addRow(QLabel("6.Saksı Nemi Giriniz :"), self.nem_entry6)
        bottom_layout.addRow(QLabel("7.Saksı Nemi Giriniz :"), self.nem_entry7)
        bottom_layout.addRow(QLabel("8.Saksı Nemi Giriniz :"), self.nem_entry8)
        bottom_layout.addRow(QLabel(""),humidity_add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def humiditypage(self):
        tarih = self.humidity_tarih_entry.text()
        nem = self.nem_entry.text()
        nem2 = self.nem_entry2.text()
        nem3 = self.nem_entry3.text()
        nem4 = self.nem_entry4.text()
        nem5 = self.nem_entry5.text()
        nem6 = self.nem_entry6.text()
        nem7 = self.nem_entry7.text()
        nem8 = self.nem_entry8.text()

        if (tarih and (nem or nem2 or nem3 or nem4 or nem5 or nem6 or nem7 or nem8) != ""):
            try:
                query = "INSERT INTO 'humidity' (tarih,nem,nem2,nem3,nem4,nem5,nem6,nem7,nem8) VALUES (?,?,?,?,?,?,?,?,?)"
                cursor.execute(query,(tarih,nem,nem2,nem3,nem4,nem5,nem6,nem7,nem8))
                connection.commit()
                self.humidity_tarih_entry.setText("")
                self.nem_entry.setText("")
                self.nem_entry2.setText("")
                self.nem_entry3.setText("")
                self.nem_entry4.setText("")
                self.nem_entry5.setText("")
                self.nem_entry6.setText("")
                self.nem_entry7.setText("")
                self.nem_entry8.setText("")
                QMessageBox.information(self,"Nem","Nem eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Nem Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")