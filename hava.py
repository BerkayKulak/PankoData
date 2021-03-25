import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class HavaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hava Nemi")
        self.setWindowIcon(QIcon("icons/co2.ico"))
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
        img = QPixmap("icons/co2ps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Hava Nem Oranı",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.hava_tarih_entry = QLineEdit(bottomFrame)
        self.hava_tarih_entry.setPlaceholderText("Tarih")
        self.hava_tarih_entry.setStyleSheet("background-color:white")
        self.hava_entry = QLineEdit(bottomFrame)
        self.hava_entry.setPlaceholderText("Hava Nem Oranı")
        self.hava_entry.setStyleSheet("background-color:white")
        carbondioksit_alma_miktari_add_button = QPushButton("Ekle",bottomFrame)
        carbondioksit_alma_miktari_add_button.clicked.connect(self.havapage)
        bottom_layout.addRow(QLabel("Tarih Giriniz :"),self.hava_tarih_entry)
        bottom_layout.addRow(QLabel("Hava Nem Oranı :"),self.hava_entry)
        bottom_layout.addRow(QLabel(""),carbondioksit_alma_miktari_add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def havapage(self):
        tarih = self.hava_tarih_entry.text()
        hava = self.hava_entry.text()

        if (tarih and hava != ""):
            try:
                query = "INSERT INTO 'hava' (hava_tarih,hava_nem) VALUES (?,?)"
                cursor.execute(query,(tarih,hava))
                connection.commit()
                self.hava_tarih_entry.setText("")
                self.hava_entry.setText("")
                QMessageBox.information(self,"Hava nemi","Hava Nem Oranı Eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Hava Nem Oranı Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")
