import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class isikMiktari(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Işık Şiddedi")
        self.setWindowIcon(QIcon("icons/idea.ico"))
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
        img = QPixmap("icons/ideaps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Işık Şiddeti",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.light_tarih_entry = QLineEdit(bottomFrame)
        self.light_tarih_entry.setPlaceholderText("Tarih")
        self.light_tarih_entry.setStyleSheet("background-color:white")
        self.isik_alma_süresi_entry = QLineEdit(bottomFrame)
        self.isik_alma_süresi_entry.setPlaceholderText("Işık Şiddeti (lux)")
        self.isik_alma_süresi_entry.setStyleSheet("background-color:white")
        isik_alma_süresi_add_button = QPushButton("Ekle",bottomFrame)
        isik_alma_süresi_add_button.clicked.connect(self.isikMiktaripage)
        bottom_layout.addRow(QLabel("Tarih Giriniz :"),self.light_tarih_entry)
        bottom_layout.addRow(QLabel("Işık alma Süresi Giriniz :"),self.isik_alma_süresi_entry)
        bottom_layout.addRow(QLabel(""),isik_alma_süresi_add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def isikMiktaripage(self):
        tarih = self.light_tarih_entry.text()
        isikalmasüresi = self.isik_alma_süresi_entry.text()

        if (tarih and isikalmasüresi != ""):
            try:
                query = "INSERT INTO 'isikalmasüresi' (tarih,isik_alma_süresi) VALUES (?,?)"
                cursor.execute(query,(tarih,isikalmasüresi))
                connection.commit()
                self.light_tarih_entry.setText("")
                self.isik_alma_süresi_entry.setText("")
                QMessageBox.information(self,"Işık miktarı","Işık Şiddeti eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Işık Şiddeti Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")