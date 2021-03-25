import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class fanBilgisi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fan Durum")
        self.setWindowIcon(QIcon("icons/fan.ico"))
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
        img = QPixmap("icons/fanps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Fan Durum",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.fan_tarih_entry = QLineEdit(bottomFrame)
        self.fan_tarih_entry.setPlaceholderText("Tarih")
        self.fan_tarih_entry.setStyleSheet("background-color:white")
        self.fan_durum_entry = QLineEdit(bottomFrame)
        self.fan_durum_entry.setPlaceholderText("Durum Açık/Kapalı")
        self.fan_durum_entry.setStyleSheet("background-color:white")
        fan_add_button = QPushButton("Ekle",bottomFrame)
        fan_add_button.clicked.connect(self.fanDurumpage)
        bottom_layout.addRow(QLabel("Tarih Giriniz :"),self.fan_tarih_entry)
        bottom_layout.addRow(QLabel("Fan Durumu Giriniz :"),self.fan_durum_entry)
        bottom_layout.addRow(QLabel(""),fan_add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def fanDurumpage(self):
        tarih = self.fan_tarih_entry.text()
        fandurum = self.fan_durum_entry.text()

        if (tarih and fandurum != ""):
            try:
                query = "INSERT INTO 'fandurum' (tarih,fandurum) VALUES (?,?)"
                cursor.execute(query,(tarih,fandurum))
                connection.commit()
                self.fan_tarih_entry.setText("")
                self.fan_durum_entry.setText("")
                QMessageBox.information(self,"Fan Durum","Fan Durum eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Fan Durum Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")
