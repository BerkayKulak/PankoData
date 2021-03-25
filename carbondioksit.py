import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class carbondioksitMiktari(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Karbondioksit Oranı")
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
        lbl_title = QLabel("Karbondioksit Oranı",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.carbondioksit_tarih_entry = QLineEdit(bottomFrame)
        self.carbondioksit_tarih_entry.setPlaceholderText("Tarih")
        self.carbondioksit_tarih_entry.setStyleSheet("background-color:white")
        self.carbondioksit_alma_miktari_entry = QLineEdit(bottomFrame)
        self.carbondioksit_alma_miktari_entry.setPlaceholderText("Karbondioksit Oranı")
        self.carbondioksit_alma_miktari_entry.setStyleSheet("background-color:white")
        carbondioksit_alma_miktari_add_button = QPushButton("Ekle",bottomFrame)
        carbondioksit_alma_miktari_add_button.clicked.connect(self.carbondioksitMiktaripage)
        bottom_layout.addRow(QLabel("Tarih Giriniz :"),self.carbondioksit_tarih_entry)
        bottom_layout.addRow(QLabel("Karbondioksit Oranı :"),self.carbondioksit_alma_miktari_entry)
        bottom_layout.addRow(QLabel(""),carbondioksit_alma_miktari_add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def carbondioksitMiktaripage(self):
        tarih = self.carbondioksit_tarih_entry.text()
        carbondioksitalmamiktari = self.carbondioksit_alma_miktari_entry.text()

        if (tarih and carbondioksitalmamiktari != ""):
            try:
                query = "INSERT INTO 'carbondioksitmiktari' (tarih,carbondioksit_alma_miktari) VALUES (?,?)"
                cursor.execute(query,(tarih,carbondioksitalmamiktari))
                connection.commit()
                self.carbondioksit_tarih_entry.setText("")
                self.carbondioksit_alma_miktari_entry.setText("")
                QMessageBox.information(self,"Carbondioksit Miktarı","Carbondioksit Miktarı eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Carbondioksit Miktarı Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")
