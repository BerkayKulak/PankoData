import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class parcaBilgisi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parça Bilgisi")
        self.setWindowIcon(QIcon("icons/parca.ico"))
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
        img = QPixmap("icons/cubeps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Parça Bilgisi ",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.parca_entry = QLineEdit(bottomFrame)
        self.parca_entry.setPlaceholderText("Parça Adı")
        self.parca_entry.setStyleSheet("background-color:white")
        self.parca_durum_entry = QLineEdit(bottomFrame)
        self.parca_durum_entry.setPlaceholderText("Mevcut/Mevcut değil")
        self.parca_durum_entry.setStyleSheet("background-color:white")
        parca_add_button = QPushButton("Ekle",bottomFrame)
        parca_add_button.clicked.connect(self.parcaDurumPage)
        bottom_layout.addRow(QLabel("Parça Adı Giriniz :"),self.parca_entry)
        bottom_layout.addRow(QLabel("Mevcut/Mevcut Değil :"),self.parca_durum_entry)
        bottom_layout.addRow(QLabel(""),parca_add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def parcaDurumPage(self):
        parca_isim = self.parca_entry.text()
        parca_durum = self.parca_durum_entry.text()

        if (parca_isim and parca_durum != ""):
            try:
                query = "INSERT INTO 'parcadurum' (parca_isim,parca_durum) VALUES (?,?)"
                cursor.execute(query,(parca_isim,parca_durum))
                connection.commit()
                self.parca_entry.setText("")
                self.parca_durum_entry.setText("")
                QMessageBox.information(self,"Parça Bilgisi","Parça Bilgisi eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Parça Bilgisi Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")