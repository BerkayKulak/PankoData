import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import main

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()


class uyeEkle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Üye Ekle")
        self.setWindowIcon(QIcon("icons/addperson.ico"))
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
        img = QPixmap("icons/addpersonps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Üye Ekle",topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setPlaceholderText("Ad")
        self.name_entry.setStyleSheet("background-color:white")
        self.telefon_entry = QLineEdit(bottomFrame)
        self.telefon_entry.setPlaceholderText("Telefon")
        self.telefon_entry.setStyleSheet("background-color:white")
        telefon_add_button = QPushButton("Ekle",bottomFrame)
        telefon_add_button.clicked.connect(self.uyeEklePage)
        bottom_layout.addRow(QLabel("İsim Soyisim :"),self.name_entry)
        bottom_layout.addRow(QLabel("Telefon :"),self.telefon_entry)
        bottom_layout.addRow(QLabel(""),telefon_add_button)
        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def uyeEklePage(self):
        name = self.name_entry.text()
        telephone = self.telefon_entry.text()

        if (name and telephone != ""):
            try:
                query = "INSERT INTO 'üyeler' (isim,telefon) VALUES (?,?)"
                cursor.execute(query,(name,telephone))
                connection.commit()
                self.name_entry.setText("")
                self.telefon_entry.setText("")
                QMessageBox.information(self,"Üye Ekle","Üye eklendi")

            except:
                QMessageBox.information(self, "Uyarı!", "Üye Eklenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")