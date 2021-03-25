import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class seraKapak(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sera Kapağı")
        self.setWindowIcon(QIcon("icons/serakapak.ico"))
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
        img = QPixmap("icons/automationps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Sera Kapağı",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.sera_kapağı_tarih_entry = QLineEdit(bottomFrame)
        self.sera_kapağı_tarih_entry.setPlaceholderText("Tarih")
        self.sera_kapağı_tarih_entry.setStyleSheet("background-color:white")
        self.sera_kapak_durum_entry = QLineEdit(bottomFrame)
        self.sera_kapak_durum_entry.setPlaceholderText("Açık/Kapalı")
        self.sera_kapak_durum_entry.setStyleSheet("background-color:white")
        sera_kapak_durum_add_button = QPushButton("Ekle",bottomFrame)
        sera_kapak_durum_add_button.clicked.connect(self.seraKapakpage)
        bottom_layout.addRow(QLabel("Tarih Giriniz :"),self.sera_kapağı_tarih_entry)
        bottom_layout.addRow(QLabel("Durum Giriniz Açık/Kapalı :"),self.sera_kapak_durum_entry)
        bottom_layout.addRow(QLabel(""),sera_kapak_durum_add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def seraKapakpage(self):
        tarih = self.sera_kapağı_tarih_entry.text()
        serakapakdurum = self.sera_kapak_durum_entry.text()

        if (tarih and serakapakdurum != ""):
            try:
                query = "INSERT INTO 'seradurum' (tarih,durum) VALUES (?,?)"
                cursor.execute(query,(tarih,serakapakdurum))
                connection.commit()
                self.sera_kapağı_tarih_entry.setText("")
                self.sera_kapak_durum_entry.setText("")
                QMessageBox.information(self,"Sera Kapağı","Sera Kapak Durumu eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Sera Kapak Durumu Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")