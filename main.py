
###################################################HEZARFEN MİLLİ YAZILIMIR TÜM HAKLARI SAKLIDIR#########################################################

#HEZARFEN L.T.D


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
from PyQt5 import QtCore
import sys
import matplotlib
matplotlib.use('Qt5Agg')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
import time
from itertools import count
import random
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
#from firebase import firebase


#firebase = firebase.FirebaseApplication("https://pankotek-3306f.firebaseio.com/",None)

import sqlite3
import temperature
import humidity
import harcanansumiktari
import isikmiktari
import carbondioksit
import hava
import serakapak
import uyeekle
import parcabilgisi
import fandurum
import about
import time
import grafikgoster
import grafikgoster2
import grafikgoster3
import grafikgoster4
import grafikgoster5
import grafikgoster6
import grafikgoster7
import grafikgoster8
import grafikgoster9

connection = sqlite3.connect("hezarfendata.db")
cursor = connection.cursor()

textChanged = False
url = ""

tbcheched = True
dockChecked = True
statusbarChecked = True

cs = False
wwo = False
var = 0
f = ""
choiceStr = ""


class Find(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle("Bul ve Değiştir")

        self.initUI()

    def initUI(self):
        self.lb1 = QLabel("Kelime Ara: ", self)
        self.lb1.setStyleSheet("font-size: 15px; ")
        self.lb1.move(10, 10)

        self.te = QTextEdit(self)
        self.te.move(10, 40)
        self.te.resize(250, 25)

        self.src = QPushButton("Kelime Bul", self)
        self.src.move(270, 40)

        self.lb2 = QLabel("Kelimeyi Değiştir: ", self)
        self.lb2.setStyleSheet("font-size: 15px; ")
        self.lb2.move(10, 80)

        self.rp = QTextEdit(self)
        self.rp.move(10, 110)
        self.rp.resize(250, 25)

        self.rpb = QPushButton("Kelime Değiştir", self)
        self.rpb.move(270, 110)



        self.close = QPushButton("Kapat", self)
        self.close.move(270, 220)
        self.close.clicked.connect(self.Close)

        self.setGeometry(300, 300, 360, 250)



    def Close(self):
        self.hide()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PANKO DATA")
        self.setWindowIcon(QIcon("icons/database10.png"))
        self.setGeometry(200,100,1600,900)
        self.UI()
        self.show()

    def UI(self):
        self.toolbar()
        self.design()
        self.menu()
        self.getTemperature()
        self.gethava()
        self.getHumiditiy()
        self.getWater()
        self.getLight()
        self.getCarbondioksit()
        self.getSeraKapak()
        self.getUye()
        self.getParca()
        self.getStatistics()
        self.getFan()
        self.statusbar()
        self.dockbar()
        self.ButtonChangeText()




    def menu(self):

        ###################ANA MENÜ################
        menubar = self.menuBar()
        file = menubar.addMenu("Dosya")
        edit = menubar.addMenu("Düzenle")
        view = menubar.addMenu("Görüntüle")
        graphs = menubar.addMenu("Grafikler")
        help_menu = menubar.addMenu("Hakkımızda")
        #################Alt Menüler###############
        new = QAction(QIcon("icons/new.png"), "Yeni", self)
        new.setShortcut("Alt+Insert")
        new.triggered.connect(self.newFile)
        file.addAction(new)
        ###########################################
        open = QAction(QIcon("icons/open.png"), "Aç", self)
        open.setShortcut("Ctrl+O")
        open.triggered.connect(self.openFile)
        file.addAction(open)
        ###########################################
        save = QAction(QIcon("icons/save.png"), "Kaydet", self)
        save.setShortcut("Ctrl+S")
        save.triggered.connect(self.saveFile)
        file.addAction(save)
        ###########################################
        exit = QAction(QIcon("icons/exit.png"), "Çıkış", self)
        exit.triggered.connect(self.exitFile)
        file.addAction(exit)
        ###########################################
        undo = QAction(QIcon("icons/undo.png"), "Geri Al", self)
        undo.setShortcut("Ctrl+Z")
        undo.triggered.connect(self.Undo)
        edit.addAction(undo)
        ###########################################
        cut = QAction(QIcon("icons/cut.png"), "Kes", self)
        cut.setShortcut("Ctrl+X")
        cut.triggered.connect(self.Cut)
        edit.addAction(cut)
        ###########################################
        copy = QAction(QIcon("icons/copy.png"), "Kopya", self)
        copy.setShortcut("Ctrl+C")
        copy.triggered.connect(self.Copy)
        edit.addAction(copy)
        ###########################################
        paste = QAction(QIcon("icons/paste.png"), "Yapıştır", self)
        paste.setShortcut("Ctrl+V")
        paste.triggered.connect(self.Paste)
        edit.addAction(paste)
        ###########################################
        find = QAction(QIcon("icons/find.png"), "Kelime Bul", self)
        find.setShortcut("Ctrl+F")
        find.triggered.connect(self.Find)
        edit.addAction(find)
        ###########################################
        time_date = QAction(QIcon("icons/datetime.png"), "Tarih", self)
        time_date.setShortcut("F5")
        time_date.triggered.connect(self.Time_Date)
        edit.addAction(time_date)
        ###########################################
        toggleStatusBar = QAction("Durum Çubuğunu Değiştir", self, checkable=True)  # tik olayı için son parametreyi yazdık
        toggleStatusBar.triggered.connect(self.funcToggleStatusBar)
        view.addAction(toggleStatusBar)
        ###########################################
        toogleToolBar = QAction("Araç Çubuğunu Aç", self, checkable=True)  # tik olayı için son parametreyi yazdık
        toogleToolBar.triggered.connect(self.funcToogleToolBar)
        view.addAction(toogleToolBar)
        ###########################################
        toogleDockBar = QAction("Dockbarı Değiştir", self, checkable=True)  # tik olayı için son parametreyi yazdık
        toogleDockBar.triggered.connect(self.funcToogleDockBar)
        view.addAction(toogleDockBar)
        ###########################################
        about_us = QAction("Hakkımızda", self)
        about_us.triggered.connect(self.About)
        help_menu.addAction(about_us)
        ############################################
        base_grafik = QAction("Sıcaklık Ön-Arka-Sol-Sağ Grafiği", self)
        base_grafik.triggered.connect(self.GraphGoster6)
        graphs.addAction(base_grafik)
        ############################################
        base_grafik = QAction("Saksı Nemleri Grafiği", self)
        base_grafik.triggered.connect(self.GraphGoster7)
        graphs.addAction(base_grafik)
        ############################################
        base_grafik = QAction("Harcanan Su Grafiği", self)
        base_grafik.triggered.connect(self.GraphGoster8)
        graphs.addAction(base_grafik)
        ############################################
        base_grafik = QAction("Işık Şiddeti Grafiği", self)
        base_grafik.triggered.connect(self.GraphGoster3)
        graphs.addAction(base_grafik)
        ############################################
        base_grafik = QAction("Karbondioksit Oranı Grafiği", self)
        base_grafik.triggered.connect(self.GraphGoster4)
        graphs.addAction(base_grafik)
        ############################################
        base_grafik = QMenu("Sıcaklık-Harcanan Su Grafiği", self)
        base_grafik_alt = QAction("Bar Grafik", self)
        base_grafik_alt2 = QAction("Linear Grafik", self)
        base_grafik.addAction(base_grafik_alt)
        base_grafik.addAction(base_grafik_alt2)
        base_grafik_alt.triggered.connect(self.GraphGoster10)
        base_grafik_alt2.triggered.connect(self.GraphGoster9)
        graphs.addMenu(base_grafik)
        ############################################
        base_grafik = QMenu("Sıcaklık-Toprak Nem Grafiği", self)
        base_grafik_alt = QAction("Bar Grafik",self)
        base_grafik_alt2 = QAction("Linear Grafik",self)
        base_grafik.addAction(base_grafik_alt)
        base_grafik.addAction(base_grafik_alt2)
        base_grafik_alt.triggered.connect(self.GraphGoster2)
        base_grafik_alt2.triggered.connect(self.GraphGoster)
        graphs.addMenu(base_grafik)




    def toolbar(self):
        ##################sıcaklık####################
        self.tb = self.addToolBar(("Toolbar"))
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.temperature_data = QAction(QIcon("icons/sıcaklık.png"),"Sıcaklık verisi ekle",self)
        self.temperature_data.setFont(QFont("Times",10))
        self.temperature_data.triggered.connect(self.temperatureData)
        self.tb.addAction(self.temperature_data)
        self.tb.addSeparator()
        ##################Nem####################
        self.humidity_data = QAction(QIcon("icons/Topraknemi.png"),"Toprak nem verisi ekle",self)
        self.humidity_data.setFont(QFont("Times", 10))
        self.humidity_data.triggered.connect(self.HumidityData)
        self.tb.addAction(self.humidity_data)
        self.tb.addSeparator()
        ##################Nem####################
        self.hava_data = QAction(QIcon("icons/havanemi.png"), "Hava nem verisi ekle", self)
        self.hava_data.setFont(QFont("Times", 10))
        self.hava_data.triggered.connect(self.havaData)
        self.tb.addAction(self.hava_data)
        self.tb.addSeparator()
        ################Su Miktarı Ekle########################
        self.water_data = QAction(QIcon("icons/liquid.png"),"Su Verisi ekle",self)
        self.water_data.setFont(QFont("Times", 10))
        self.water_data.triggered.connect(self.waterData)
        self.tb.addAction(self.water_data)
        self.tb.addSeparator()
        ######################Işık Alma Süresi  Ekle#####################
        self.light_data = QAction(QIcon("icons/idea.png"), "Işık Şiddeti Ekle", self)
        self.light_data.setFont(QFont("Times", 10))
        self.light_data.triggered.connect(self.lightData)
        self.tb.addAction(self.light_data)
        self.tb.addSeparator()
        ######################Co2 miktarı Ekle#####################
        self.carbondioksit_data = QAction(QIcon("icons/co2.png"), "Karbondioksit Oranı Ekle", self)
        self.carbondioksit_data.setFont(QFont("Times", 10))
        self.carbondioksit_data.triggered.connect(self.carbondioksitData)
        self.tb.addAction(self.carbondioksit_data)
        self.tb.addSeparator()
        ######################Sera Kapağı#####################
        self.sera_kapağı = QAction(QIcon("icons/agriculture.png"), "Sera çatı sistemi verisi ekle", self)
        self.sera_kapağı.setFont(QFont("Times", 10))
        self.sera_kapağı.triggered.connect(self.seraKapak)
        self.tb.addAction(self.sera_kapağı)
        self.tb.addSeparator()
        ######################Fan Durum#####################
        self.fan_control = QAction(QIcon("icons/fanps.png"), "Fan Durum", self)
        self.fan_control.setFont(QFont("Times", 10))
        self.fan_control.triggered.connect(self.fanControl)
        self.tb.addAction(self.fan_control)
        self.tb.addSeparator()
        #####################Üye ekle#################
        self.add_member = QAction(QIcon("icons/üye.png"), "Üye ekle", self)
        self.add_member.setFont(QFont("Times", 10))
        self.add_member.triggered.connect(self.addMember)
        self.tb.addAction(self.add_member)
        self.tb.addSeparator()
        #####################Parça Bilgisi#################
        self.parca_bilgisi = QAction(QIcon("icons/cube.png"), "Parça Bilgisi", self)
        self.parca_bilgisi.setFont(QFont("Times", 10))
        self.parca_bilgisi.triggered.connect(self.parcaBilgisi)
        self.tb.addAction(self.parca_bilgisi)
        self.tb.addSeparator()




    def design(self):
        temperature_main_layout = QHBoxLayout()
        temperature_main_left_layout = QVBoxLayout()
        temperature_main_right_layout = QVBoxLayout()
        temperature_main_layout.addLayout(temperature_main_left_layout,65)
        temperature_main_layout.addLayout(temperature_main_right_layout,35)
        #################Tabs########################
        self.tabs = QTabWidget(self)
        self.tabs.blockSignals(True)
        self.setCentralWidget(self.tabs)
        self.tabs.currentChanged.connect(self.tabChanged)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab12 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()
        self.tab9 = QWidget()
        self.tab10 = QWidget()
        self.tab11 = QWidget()
        self.tabs.addTab(self.tab1,"Sıcaklık")
        self.tabs.addTab(self.tab2,"Toprak Nem")
        self.tabs.addTab(self.tab12,"Hava Nem")
        self.tabs.addTab(self.tab3,"Harcanan-Toplam Su, pH, EC")
        self.tabs.addTab(self.tab4,"Işık Şiddeti")
        self.tabs.addTab(self.tab5,"Karbondioksit Oranı")
        self.tabs.addTab(self.tab6,"Sera Çatı Sistemi Durumu")
        self.tabs.addTab(self.tab11, "Fan Durumu")
        self.tabs.addTab(self.tab7,"Üye Bilgisi")
        self.tabs.addTab(self.tab8, "Parça Bilgisi")
        self.tabs.addTab(self.tab9,"İstatistikler")
        self.tabs.addTab(self.tab10,"Not Sistemi")



        ##############Tab1####################################
        ############main_left_layout##########################
        self.temperature_table = QTableWidget()
        self.temperature_table.setColumnCount(6)#id,tarih,sıcaklık
        self.temperature_table.setColumnHidden(0,True)
        self.temperature_table.setHorizontalHeaderItem(0,QTableWidgetItem("Temperature ID"))
        self.temperature_table.setHorizontalHeaderItem(1,QTableWidgetItem("Tarih"))
        self.temperature_table.setHorizontalHeaderItem(2,QTableWidgetItem("Cº-1-ÖN-SOL"))
        self.temperature_table.setHorizontalHeaderItem(3, QTableWidgetItem("Cº-2-ÖN-SAĞ"))
        self.temperature_table.setHorizontalHeaderItem(4, QTableWidgetItem("Cº-3-ARKA-SOL"))
        self.temperature_table.setHorizontalHeaderItem(5, QTableWidgetItem("Cº-4-ARKA-SAĞ"))
        self.temperature_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.temperature_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.temperature_table.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.temperature_table.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.temperature_table.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.temperature_table.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)
        self.temperature_table.doubleClicked.connect(self.selectedTemperatureTable)
        temperature_main_left_layout.addWidget(self.temperature_table)
        self.tab1.setLayout(temperature_main_layout)
        ##############Tab2####################################
        ############main_left_layout##########################
        humidity_main_layout = QHBoxLayout()
        humidity_main_left_layout = QVBoxLayout()
        humidity_main_right_layout = QVBoxLayout()
        humidity_main_layout.addLayout(humidity_main_left_layout, 65)
        humidity_main_layout.addLayout(humidity_main_right_layout, 35)
        self.humidity_table = QTableWidget()
        self.humidity_table.setColumnCount(10)  # id,gün,ay,yıl,Nem
        self.humidity_table.setColumnHidden(0, True)
        self.humidity_table.setHorizontalHeaderItem(0, QTableWidgetItem("Nem ID"))
        self.humidity_table.setHorizontalHeaderItem(1, QTableWidgetItem("Tarih"))
        self.humidity_table.setHorizontalHeaderItem(2, QTableWidgetItem("1.Saksı %"))
        self.humidity_table.setHorizontalHeaderItem(3, QTableWidgetItem("2.Saksı %"))
        self.humidity_table.setHorizontalHeaderItem(4, QTableWidgetItem("3.Saksı %"))
        self.humidity_table.setHorizontalHeaderItem(5, QTableWidgetItem("4.Saksı %"))
        self.humidity_table.setHorizontalHeaderItem(6, QTableWidgetItem("5.Saksı %"))
        self.humidity_table.setHorizontalHeaderItem(7, QTableWidgetItem("6.Saksı %"))
        self.humidity_table.setHorizontalHeaderItem(8, QTableWidgetItem("7.Saksı %"))
        self.humidity_table.setHorizontalHeaderItem(9, QTableWidgetItem("8.Saksı %"))
        self.humidity_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.humidity_table.horizontalHeader().setSectionResizeMode(1)
        self.humidity_table.horizontalHeader().setSectionResizeMode(2)
        self.humidity_table.horizontalHeader().setSectionResizeMode(3)
        self.humidity_table.horizontalHeader().setSectionResizeMode(4)
        self.humidity_table.horizontalHeader().setSectionResizeMode(5)
        self.humidity_table.horizontalHeader().setSectionResizeMode(6)
        self.humidity_table.horizontalHeader().setSectionResizeMode(7)
        self.humidity_table.horizontalHeader().setSectionResizeMode(8)
        self.humidity_table.horizontalHeader().setSectionResizeMode(9)
        self.humidity_table.doubleClicked.connect(self.selectedHumidityTable)
        humidity_main_left_layout.addWidget(self.humidity_table)
        self.tab2.setLayout(humidity_main_layout)
        ##############Tab3####################################
        ############main_left_layout##########################
        hava_main_layout = QHBoxLayout()
        hava_main_left_layout = QVBoxLayout()
        hava_main_right_layout = QVBoxLayout()
        hava_main_layout.addLayout(hava_main_left_layout, 65)
        hava_main_layout.addLayout(hava_main_right_layout, 35)
        self.hava_table = QTableWidget()
        self.hava_table.setColumnCount(3)  # id,gün,ay,yıl,Nem
        self.hava_table.setColumnHidden(0, True)
        self.hava_table.setHorizontalHeaderItem(0, QTableWidgetItem("Hava ID"))
        self.hava_table.setHorizontalHeaderItem(1, QTableWidgetItem("Tarih"))
        self.hava_table.setHorizontalHeaderItem(2, QTableWidgetItem("Hava Nem %"))
        self.hava_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.hava_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.hava_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.hava_table.doubleClicked.connect(self.selectedhava)
        hava_main_left_layout.addWidget(self.hava_table)
        self.tab12.setLayout(hava_main_layout)
        ############main_left_layout##########################
        water_main_layout = QHBoxLayout()
        water_main_left_layout = QVBoxLayout()
        water_main_right_layout = QVBoxLayout()
        water_main_layout.addLayout(water_main_left_layout, 65)
        water_main_layout.addLayout(water_main_right_layout, 35)
        self.water_table = QTableWidget()
        self.water_table.setColumnCount(6)  # id,gün,ay,yıl,Nem
        self.water_table.setColumnHidden(0, True)
        self.water_table.setHorizontalHeaderItem(0, QTableWidgetItem("Su ID"))
        self.water_table.setHorizontalHeaderItem(1, QTableWidgetItem("Tarih"))
        self.water_table.setHorizontalHeaderItem(2, QTableWidgetItem("Harcanan Su"))
        self.water_table.setHorizontalHeaderItem(3, QTableWidgetItem("Toplam Su"))
        self.water_table.setHorizontalHeaderItem(4, QTableWidgetItem("pH"))
        self.water_table.setHorizontalHeaderItem(5, QTableWidgetItem("EC"))
        self.water_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.water_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.water_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.water_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.water_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.water_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.water_table.doubleClicked.connect(self.selectedWater)
        water_main_left_layout.addWidget(self.water_table)
        self.tab3.setLayout(water_main_layout)
        ##############Tab4####################################
        ############main_left_layout##########################
        light_main_layout = QHBoxLayout()
        light_main_left_layout = QVBoxLayout()
        light_main_right_layout = QVBoxLayout()
        light_main_layout.addLayout(light_main_left_layout, 65)
        light_main_layout.addLayout(light_main_right_layout, 35)
        self.light_table = QTableWidget()
        self.light_table.setColumnCount(3)  # id,gün,ay,yıl,Nem
        self.light_table.setColumnHidden(0, True)
        self.light_table.setHorizontalHeaderItem(0, QTableWidgetItem("Işık ID"))
        self.light_table.setHorizontalHeaderItem(1, QTableWidgetItem("Tarih"))
        self.light_table.setHorizontalHeaderItem(2, QTableWidgetItem("Işık Şiddeti: Lux"))
        self.light_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.light_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.light_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.light_table.doubleClicked.connect(self.selectedLight)
        light_main_left_layout.addWidget(self.light_table)
        self.tab4.setLayout(light_main_layout)
        ##############Tab5####################################
        ############main_left_layout##########################
        carbondioksit_main_layout = QHBoxLayout()
        carbondioksit_main_left_layout = QVBoxLayout()
        carbondioksit_main_right_layout = QVBoxLayout()
        carbondioksit_main_layout.addLayout(carbondioksit_main_left_layout, 65)
        carbondioksit_main_layout.addLayout(carbondioksit_main_right_layout, 35)
        self.carbondioksit_table = QTableWidget()
        self.carbondioksit_table.setColumnCount(3)#id,gün,ay,yıl,Nem
        self.carbondioksit_table.setColumnHidden(0, True)
        self.carbondioksit_table.setHorizontalHeaderItem(0, QTableWidgetItem("Karbondioksit Oranı ID"))
        self.carbondioksit_table.setHorizontalHeaderItem(1, QTableWidgetItem("Tarih"))
        self.carbondioksit_table.setHorizontalHeaderItem(2, QTableWidgetItem("Karbondioksit Oranı"))
        self.carbondioksit_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.carbondioksit_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.carbondioksit_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.carbondioksit_table.doubleClicked.connect(self.selectedCarbondioksit)
        carbondioksit_main_left_layout.addWidget(self.carbondioksit_table)
        self.tab5.setLayout(carbondioksit_main_layout)
        ##############Tab6####################################
        ############main_left_layout##########################
        sera_cati_main_layout = QHBoxLayout()
        sera_cati_main_left_layout = QVBoxLayout()
        sera_cati_main_right_layout = QVBoxLayout()
        sera_cati_main_layout.addLayout(sera_cati_main_left_layout, 65)
        sera_cati_main_layout.addLayout(sera_cati_main_right_layout, 35)
        self.sera_cati_table = QTableWidget()
        self.sera_cati_table.setColumnCount(3)  # id,gün,ay,yıl,Nem
        self.sera_cati_table.setColumnHidden(0, True)
        self.sera_cati_table.setHorizontalHeaderItem(0, QTableWidgetItem("Sera Çatı ID"))
        self.sera_cati_table.setHorizontalHeaderItem(1, QTableWidgetItem("Tarih"))
        self.sera_cati_table.setHorizontalHeaderItem(2, QTableWidgetItem("Durum: Açık/Kapalı"))
        self.sera_cati_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.sera_cati_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.sera_cati_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.sera_cati_table.doubleClicked.connect(self.selectedCati)
        sera_cati_main_left_layout.addWidget(self.sera_cati_table)
        self.tab6.setLayout(sera_cati_main_layout)
        ##############Tab7####################################
        ############main_left_layout##########################
        uye_main_layout = QHBoxLayout()
        uye_main_left_layout = QVBoxLayout()
        uye_main_right_layout = QVBoxLayout()
        uye_main_layout.addLayout(uye_main_left_layout, 65)
        uye_main_layout.addLayout(uye_main_right_layout, 35)
        self.uye_table = QTableWidget()
        self.uye_table.setColumnCount(3)  # id,gün,ay,yıl,Nem
        self.uye_table.setHorizontalHeaderItem(0, QTableWidgetItem("Üye ID"))
        self.uye_table.setHorizontalHeaderItem(1, QTableWidgetItem("Üye Adı"))
        self.uye_table.setHorizontalHeaderItem(2, QTableWidgetItem("Üye Telefonu"))
        self.uye_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.uye_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.uye_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.uye_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.uye_table.doubleClicked.connect(self.selectedUye)
        uye_main_left_layout.addWidget(self.uye_table)
        self.tab7.setLayout(uye_main_layout)
        ##############Tab8####################################
        ############main_left_layout##########################
        parca_bilgi_main_layout = QHBoxLayout()
        parca_bilgi_main_left_layout = QVBoxLayout()
        parca_bilgi_main_right_layout = QVBoxLayout()
        parca_bilgi_main_layout.addLayout(parca_bilgi_main_left_layout, 65)
        parca_bilgi_main_layout.addLayout(parca_bilgi_main_right_layout, 35)
        self.parca_bilgi_table = QTableWidget()
        self.parca_bilgi_table.setColumnCount(3)  # id,gün,ay,yıl,Nem
        self.parca_bilgi_table.setColumnHidden(0, True)
        self.parca_bilgi_table.setHorizontalHeaderItem(0, QTableWidgetItem("parca ID"))
        self.parca_bilgi_table.setHorizontalHeaderItem(1, QTableWidgetItem("Parça Adı"))
        self.parca_bilgi_table.setHorizontalHeaderItem(2, QTableWidgetItem("Durum: Mevcut/Mevcut Değil"))
        self.parca_bilgi_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.parca_bilgi_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.parca_bilgi_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.parca_bilgi_table.doubleClicked.connect(self.selectedParca)
        parca_bilgi_main_left_layout.addWidget(self.parca_bilgi_table)
        self.tab8.setLayout(parca_bilgi_main_layout)
        ##############Tab9####################################
        ############main_left_layout##########################
        self.veri_degistir_main_layout = QVBoxLayout()
        self.veri_degistir_main_left_layout = QHBoxLayout()
        self.veri_degistir_main_right_layout = QHBoxLayout()
        self.veri_degistir_main_layout.addLayout(self.veri_degistir_main_left_layout,20)
        self.veri_degistir_main_layout.addLayout(self.veri_degistir_main_right_layout,80)
        self.veri_bilgi = QTextEdit()
        self.veri_bilgi.setFont(QFont("Times",16.0))
        self.veri_degistir_main_right_layout.addWidget(self.veri_bilgi)
        self.tab10.setLayout(self.veri_degistir_main_layout)
        self.veri_bilgi.textChanged.connect(self.funcTextChanged)
        ##############Tab10####################################
        ############main_left_layout##########################
        fan_main_layout = QHBoxLayout()
        fan_main_left_layout = QVBoxLayout()
        fan_main_right_layout = QVBoxLayout()
        fan_main_layout.addLayout(fan_main_left_layout, 65)
        fan_main_layout.addLayout(fan_main_right_layout, 35)
        self.fan_table = QTableWidget()
        self.fan_table.setColumnCount(3)  # id,gün,ay,yıl,Nem
        self.fan_table.setColumnHidden(0, True)
        self.fan_table.setHorizontalHeaderItem(0, QTableWidgetItem("Fan ID"))
        self.fan_table.setHorizontalHeaderItem(1, QTableWidgetItem("Tarih"))
        self.fan_table.setHorizontalHeaderItem(2, QTableWidgetItem("Durum: Açık/Kapalı"))
        self.fan_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fan_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.fan_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.fan_table.doubleClicked.connect(self.selectedFan)
        fan_main_left_layout.addWidget(self.fan_table)
        self.tab11.setLayout(fan_main_layout)





















        ##############main temperatue right layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Veri Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#40E0D0;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px;}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        temperature_lbl_search = QLabel("Veri gir: ",right_top_frame)
        temperature_lbl_search.setStyleSheet("font: 13pt Times Bold;color:#000080")
        self.temperature_search_entry = QLineEdit(right_top_frame)
        self.temperature_search_entry.setStyleSheet("border:4px solid gray;border-radius: 7px")
        temperature_search_button = QPushButton("Arama",right_top_frame)
        temperature_search_button.setStyleSheet("background-color:#8FBC8F;font:13pt Times Bold;color:white")
        temperature_search_button.clicked.connect(self.temperatureSearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(temperature_lbl_search)
        right_top_frame_box.addWidget(self.temperature_search_entry)
        right_top_frame_box.addWidget(temperature_search_button)
        right_top_frame_box.addStretch()
        temperature_main_right_layout.addWidget(right_top_frame,20)
        ####################seraRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle", self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet("#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.temperature_radio_btn1 = QRadioButton("Tüm veri", right_middle_frame)
        self.temperature_btn_list = QPushButton("Listele", right_middle_frame)
        self.temperature_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.temperature_btn_list.clicked.connect(self.temperatureRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.temperature_radio_btn1)
        right_middle_box.addWidget(self.temperature_btn_list)
        right_middle_box.addStretch()
        temperature_main_right_layout.addWidget(right_middle_frame, 20)

        ####################Right side Bottom list box#################################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Sıcaklık Verileri")
        lbl_title.setContentsMargins(5, 0, 0, 0)
        lbl_title.setFont(QFont("Times",20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/temperature-control.png")
        img_library.setContentsMargins(60, 0, 0, 0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        temperature_main_right_layout.addLayout(right_bottom_layout, 60)

        ##############main hava right layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Veri Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet(
            "#Main{background-color:#40E0D0;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px;}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        hava_lbl_search = QLabel("Veri gir: ", right_top_frame)
        hava_lbl_search.setStyleSheet("font: 13pt Times Bold;color:#000080")
        self.hava_search_entry = QLineEdit(right_top_frame)
        self.hava_search_entry.setStyleSheet("border:4px solid gray;border-radius: 7px")
        hava_search_button = QPushButton("Arama", right_top_frame)
        hava_search_button.setStyleSheet("background-color:#8FBC8F;font:13pt Times Bold;color:white")
        hava_search_button.clicked.connect(self.havaSearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(hava_lbl_search)
        right_top_frame_box.addWidget(self.hava_search_entry)
        right_top_frame_box.addWidget(hava_search_button)
        right_top_frame_box.addStretch()
        hava_main_right_layout.addWidget(right_top_frame, 20)
        ####################seraRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle", self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet(
            "#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.hava_radio_btn1 = QRadioButton("Tüm veri", right_middle_frame)
        self.hava_btn_list = QPushButton("Listele", right_middle_frame)
        self.hava_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.hava_btn_list.clicked.connect(self.havaRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.hava_radio_btn1)
        right_middle_box.addWidget(self.hava_btn_list)
        right_middle_box.addStretch()
        hava_main_right_layout.addWidget(right_middle_frame, 20)

        ####################Right side Bottom list box#################################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Hava Nem Verileri")
        lbl_title.setContentsMargins(5, 0, 0, 0)
        lbl_title.setFont(QFont("Times", 20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/havanemi.png")
        img_library.setContentsMargins(60, 0, 0, 0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        hava_main_right_layout.addLayout(right_bottom_layout, 60)

        ##############main humidity right layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Veri Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#FFD700;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        lbl_search = QLabel("Veri gir: ", right_top_frame)
        lbl_search.setStyleSheet("font: 13pt Times Bold;color:#8B0000")
        self.humidity_search_entry = QLineEdit(right_top_frame)
        self.humidity_search_entry.setStyleSheet("border:4px solid gray;border-radius: 7px")
        humidity_search_button = QPushButton("Arama", right_top_frame)
        humidity_search_button.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        humidity_search_button.clicked.connect(self.humiditySearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(lbl_search)
        right_top_frame_box.addWidget(self.humidity_search_entry)
        right_top_frame_box.addWidget(humidity_search_button)
        right_top_frame_box.addStretch()
        humidity_main_right_layout.addWidget(right_top_frame, 20)
        ####################humidityRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle", self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet("#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.humidity_radio_btn1 = QRadioButton("Tüm veri", right_middle_frame)
        self.humidity_btn_list = QPushButton("Listele", right_middle_frame)
        self.humidity_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.humidity_btn_list.clicked.connect(self.humidityRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.humidity_radio_btn1)
        right_middle_box.addWidget(self.humidity_btn_list)
        right_middle_box.addStretch()
        humidity_main_right_layout.addWidget(right_middle_frame, 20)
        ####################Right side Bottom list box#################################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Nem Verileri")
        lbl_title.setContentsMargins(5, 0, 0, 0)
        lbl_title.setFont(QFont("Times", 20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/fingerprint.png")
        img_library.setContentsMargins(60, 0, 0, 0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        humidity_main_right_layout.addLayout(right_bottom_layout, 60)



        ##############main water right layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Veri Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#483D8B;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        water_lbl_search = QLabel("Veri gir: ", right_top_frame)
        water_lbl_search.setStyleSheet("font: 13pt Times Bold;color:#DAA520")
        self.water_search_entry = QLineEdit(right_top_frame)
        self.water_search_entry.setStyleSheet("border:4px solid gray;border-radius: 7px")
        water_search_button = QPushButton("Arama", right_top_frame)
        water_search_button.setStyleSheet("background-color:#008080;font:13pt Times Bold;color:white")
        water_search_button.clicked.connect(self.waterSearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(water_lbl_search)
        right_top_frame_box.addWidget(self.water_search_entry)
        right_top_frame_box.addWidget(water_search_button)
        right_top_frame_box.addStretch()
        water_main_right_layout.addWidget(right_top_frame, 20)
        ####################waterRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle", self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet("#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.water_radio_btn1 = QRadioButton("Tüm veri", right_middle_frame)
        self.water_btn_list = QPushButton("Listele", right_middle_frame)
        self.water_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.water_btn_list.clicked.connect(self.waterRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.water_radio_btn1)
        right_middle_box.addWidget(self.water_btn_list)
        right_middle_box.addStretch()
        water_main_right_layout.addWidget(right_middle_frame, 20)
        ####################Right side Bottom list box#################################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Harcanan Su Miktarı")
        lbl_title.setContentsMargins(5, 0, 0, 0)
        lbl_title.setFont(QFont("Times", 20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/watertank.png")
        img_library.setContentsMargins(60, 0, 0, 0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        water_main_right_layout.addLayout(right_bottom_layout, 60)




        ##############main light right layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Veri Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#DC143C;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        lbl_search = QLabel("Veri gir: ", right_top_frame)
        lbl_search.setStyleSheet("font: 13pt Times Bold;color:#00FFFF")
        self.light_search_entry = QLineEdit(right_top_frame)
        self.light_search_entry.setStyleSheet("border:4px solid gray;border-radius: 7px")
        light_search_button = QPushButton("Arama", right_top_frame)
        light_search_button.setStyleSheet("background-color:#FFD700;font:13pt Times Bold;color:white")
        light_search_button.clicked.connect(self.lightSearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(lbl_search)
        right_top_frame_box.addWidget(self.light_search_entry)
        right_top_frame_box.addWidget(light_search_button)
        right_top_frame_box.addStretch()
        light_main_right_layout.addWidget(right_top_frame, 20)
        ####################lightRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle", self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet( "#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.light_radio_btn1 = QRadioButton("Tüm veri", right_middle_frame)
        self.light_btn_list = QPushButton("Listele", right_middle_frame)
        self.light_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.light_btn_list.clicked.connect(self.lightRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.light_radio_btn1)
        right_middle_box.addWidget(self.light_btn_list)
        right_middle_box.addStretch()
        light_main_right_layout.addWidget(right_middle_frame, 20)
        ####################Right side Bottom list box#################################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Işık Alma Miktarı")
        lbl_title.setContentsMargins(5, 0, 0, 0)
        lbl_title.setFont(QFont("Times", 20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/smart-home.png")
        img_library.setContentsMargins(60, 0, 0, 0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        light_main_right_layout.addLayout(right_bottom_layout, 60)

        ##############main carbondioksit right layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Veri Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#7B68EE;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        lbl_search = QLabel("Veri gir: ", right_top_frame)
        lbl_search.setStyleSheet("font: 13pt Times Bold;color:#4B0082")
        self.carbondioksit_search_entry = QLineEdit(right_top_frame)
        self.carbondioksit_search_entry.setStyleSheet("border:4px solid gray;border-radius: 7px")
        carbondioksit_search_button = QPushButton("Arama", right_top_frame)
        carbondioksit_search_button.setStyleSheet("background-color:#00BFFF;font:13pt Times Bold;color:white")
        carbondioksit_search_button.clicked.connect(self.carbondioksitSearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(lbl_search)
        right_top_frame_box.addWidget(self.carbondioksit_search_entry)
        right_top_frame_box.addWidget(carbondioksit_search_button)
        right_top_frame_box.addStretch()
        carbondioksit_main_right_layout.addWidget(right_top_frame, 20)
        ####################carbondioksitRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle", self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet( "#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.carbondioksit_radio_btn1 = QRadioButton("Tüm veri", right_middle_frame)
        self.carbondioksit_btn_list = QPushButton("Listele", right_middle_frame)
        self.carbondioksit_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.carbondioksit_btn_list.clicked.connect(self.carbondioksitRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.carbondioksit_radio_btn1)
        right_middle_box.addWidget(self.carbondioksit_btn_list)
        right_middle_box.addStretch()
        carbondioksit_main_right_layout.addWidget(right_middle_frame, 20)
        ####################Right side Bottom list box#################################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Karbondioksit Oranı")
        lbl_title.setContentsMargins(5, 0, 0, 0)
        lbl_title.setFont(QFont("Times", 20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/airquality.png")
        img_library.setContentsMargins(60, 0, 0, 0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        carbondioksit_main_right_layout.addLayout(right_bottom_layout, 60)



        ##############main çatı right layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Veri Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#708090;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        lbl_search = QLabel("Veri gir: ",right_top_frame)
        lbl_search.setStyleSheet("font:13pt Times Bold;color:white")
        self.kapak_search_entry = QLineEdit(right_top_frame)
        self.kapak_search_entry.setStyleSheet("border:2px solid gray;border-radius:5px")
        kapak_search_button = QPushButton("Arama",right_top_frame)
        kapak_search_button.setStyleSheet("background-color:#CD853F;font:13pt Times Bold;color:white")
        kapak_search_button.clicked.connect(self.catiSearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(lbl_search)
        right_top_frame_box.addWidget(self.kapak_search_entry)#başka fonksiyonda kullanılcak self
        right_top_frame_box.addWidget(kapak_search_button)
        # main_right_layout.addLayout(right_top_frame_box,20)  #%20
        right_top_frame_box.addStretch()
        sera_cati_main_right_layout.addWidget(right_top_frame,20)
        ####################catiRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle",self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet("#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.kapak_radio_btn1 = QRadioButton("Tüm veri",right_middle_frame)
        self.kapak_radio_btn2 = QRadioButton("Açık",right_middle_frame)
        self.kapak_radio_btn3 = QRadioButton("Kapalı",right_middle_frame)
        self.kapak_btn_list = QPushButton("Listele",right_middle_frame)
        self.kapak_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.kapak_btn_list.clicked.connect(self.catiRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.kapak_radio_btn1)
        right_middle_box.addWidget(self.kapak_radio_btn2)
        right_middle_box.addWidget(self.kapak_radio_btn3)
        right_middle_box.addWidget(self.kapak_btn_list)
        right_middle_box.addStretch()
        sera_cati_main_right_layout.addWidget(right_middle_frame,20)
        #####################cati Right Side bottom Widgets#######################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Çatı Sistemi Kontrol")
        lbl_title.setContentsMargins(30,0,0,0)#SOL ÜST SAĞ ALT
        lbl_title.setFont(QFont("Times",20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/automation.png")
        img_library.setContentsMargins(60,0,0,0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        sera_cati_main_right_layout.addLayout(right_bottom_layout,60)




        ###########################üye################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Üye Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#F8F8FF;font: 15pt Times Bold;color:#2F4F4F;border:2px solid gray;border-radius:15px}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        lbl_search = QLabel("Üye adı gir: ", right_top_frame)
        lbl_search.setStyleSheet("font: 13pt Times Bold;color:#2F4F4F")
        self.uye_search_entry = QLineEdit(right_top_frame)
        self.uye_search_entry.setStyleSheet("border:4px solid gray;border-radius: 7px")
        uye_search_button = QPushButton("Arama", right_top_frame)
        uye_search_button.setStyleSheet("background-color:#2F4F4F;font:13pt Times Bold;color:white")
        uye_search_button.clicked.connect(self.searchMember)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(lbl_search)
        right_top_frame_box.addWidget(self.uye_search_entry)
        right_top_frame_box.addWidget(uye_search_button)
        right_top_frame_box.addStretch()
        uye_main_right_layout.addWidget(right_top_frame, 20)
        ####################üyeRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle", self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet("#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.üye_radio_btn1 = QRadioButton("Tüm veri", right_middle_frame)
        self.üye_btn_list = QPushButton("Listele", right_middle_frame)
        self.üye_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.üye_btn_list.clicked.connect(self.uyeRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.üye_radio_btn1)
        right_middle_box.addWidget(self.üye_btn_list)
        right_middle_box.addStretch()
        uye_main_right_layout.addWidget(right_middle_frame, 20)
        #####################üye right side bottom ######################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Üye Bilgisi")
        lbl_title.setContentsMargins(5, 0, 0, 0)
        lbl_title.setFont(QFont("Times", 20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/production.png")
        img_library.setContentsMargins(60, 0, 0, 0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        uye_main_right_layout.addLayout(right_bottom_layout, 60)


         ##############main parçaright layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Parça Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#90EE90;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        lbl_search = QLabel("Veri gir: ",right_top_frame)
        lbl_search.setStyleSheet("font:13pt Times Bold;color:white")
        self.parca_search_entry = QLineEdit(right_top_frame)
        self.parca_search_entry.setStyleSheet("border:2px solid gray;border-radius:5px")
        parca_search_button = QPushButton("Arama",right_top_frame)
        parca_search_button.setStyleSheet("background-color:#F0E68C;font:13pt Times Bold;color:white")
        parca_search_button.clicked.connect(self.parcaSearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(lbl_search)
        right_top_frame_box.addWidget(self.parca_search_entry)#başka fonksiyonda kullanılcak self
        right_top_frame_box.addWidget(parca_search_button)
        # main_right_layout.addLayout(right_top_frame_box,20)  #%20
        right_top_frame_box.addStretch()
        parca_bilgi_main_right_layout.addWidget(right_top_frame,20)
        ####################catiRight side list box#################################
        right_middle_frame = QGroupBox("Parçaları Görüntüle",self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet("#Main{background-color:#F08080;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.parca_radio_btn1 = QRadioButton("Tüm veri",right_middle_frame)
        self.parca_radio_btn2 = QRadioButton("Mevcut",right_middle_frame)
        self.parca_radio_btn3 = QRadioButton("Mevcut değil",right_middle_frame)
        self.btn_list = QPushButton("Listele",right_middle_frame)
        self.btn_list.setStyleSheet("background-color:#D3D3D3;font:13pt Times Bold;color:white")
        self.btn_list.clicked.connect(self.parcaRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.parca_radio_btn1)
        right_middle_box.addWidget(self.parca_radio_btn2)
        right_middle_box.addWidget(self.parca_radio_btn3)
        right_middle_box.addWidget(self.btn_list)
        right_middle_box.addStretch()
        parca_bilgi_main_right_layout.addWidget(right_middle_frame,20)
        #####################cati Right Side bottom Widgets#######################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Parça Bilgisi")
        lbl_title.setContentsMargins(30,0,0,0)#SOL ÜST SAĞ ALT
        lbl_title.setFont(QFont("Times",20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/model.png")
        img_library.setContentsMargins(60,0,0,0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        parca_bilgi_main_right_layout.addLayout(right_bottom_layout,60)

        #####################Statistics################################
        statistics_main_layout = QVBoxLayout()
        self.statistic_group = QGroupBox("Akıllı Sera İstatistikleri")
        self.statistic_group.setObjectName("Main")
        self.statistic_group.setStyleSheet("#Main{background-color:#FFFFE0;color:#black;}")
        self.statistic_from_layout = QFormLayout()
        self.statistic_group.setFont(QFont("Arial", 10))
        self.ortalama_sicaklik = QLabel("")
        self.ortalama_sicaklik2 = QLabel("")
        self.ortalama_sicaklik3 = QLabel("")
        self.ortalama_sicaklik4 = QLabel("")
        self.ortalama_nem = QLabel("")
        self.ortalama_nem2 = QLabel("")
        self.ortalama_nem3 = QLabel("")
        self.ortalama_nem4 = QLabel("")
        self.ortalama_nem5 = QLabel("")
        self.ortalama_nem6 = QLabel("")
        self.ortalama_nem7 = QLabel("")
        self.ortalama_nem8 = QLabel("")
        self.toplam_harcanan_su_miktari = QLabel("")
        self.ortalama_harcanan_su_miktari = QLabel("")
        self.ortalama_isik_alma_süresi = QLabel("")
        self.ortalama_co2_miktari = QLabel("")
        self.toplam_üye = QLabel("")
        self.mevcut_parca = QLabel("")
        self.statistic_from_layout.addChildWidget(self.statistic_group)
        self.statistic_from_layout.addRow(QLabel("Ön Taraf Sıcaklık Ortalaması:\n"), self.ortalama_sicaklik)
        self.statistic_from_layout.addRow(QLabel("Arka Taraf Sıcaklık Ortalaması:\n"), self.ortalama_sicaklik2)
        self.statistic_from_layout.addRow(QLabel("Sol Taraf Sıcaklık Ortalaması:\n"), self.ortalama_sicaklik3)
        self.statistic_from_layout.addRow(QLabel("Sağ Taraf Sıcaklık Ortalaması:\n"), self.ortalama_sicaklik4)
        self.statistic_from_layout.addRow(QLabel("1.Saksı Ortalama Nem :\n"), self.ortalama_nem)
        self.statistic_from_layout.addRow(QLabel("2.Saksı Ortalama Nem :\n"), self.ortalama_nem2)
        self.statistic_from_layout.addRow(QLabel("3.Saksı Ortalama Nem :\n"), self.ortalama_nem3)
        self.statistic_from_layout.addRow(QLabel("4.Saksı Ortalama Nem :\n"), self.ortalama_nem4)
        self.statistic_from_layout.addRow(QLabel("5.Saksı Ortalama Nem :\n"), self.ortalama_nem5)
        self.statistic_from_layout.addRow(QLabel("6.Saksı Ortalama Nem :\n"), self.ortalama_nem6)
        self.statistic_from_layout.addRow(QLabel("7.Saksı Ortalama Nem :\n"), self.ortalama_nem7)
        self.statistic_from_layout.addRow(QLabel("8.Saksı Ortalama Nem :\n"), self.ortalama_nem8)
        self.statistic_from_layout.addRow(QLabel("Toplam Harcanan Su Miktarı :\n"), self.toplam_harcanan_su_miktari)
        self.statistic_from_layout.addRow(QLabel("Ortalama Harcanan Su Miktarı :\n"), self.ortalama_harcanan_su_miktari)
        self.statistic_from_layout.addRow(QLabel("Ortalama Işık Şiddeti :\n"), self.ortalama_isik_alma_süresi)
        self.statistic_from_layout.addRow(QLabel("Ortalama Karbondioksit Oranı :\n"), self.ortalama_co2_miktari)
        self.statistic_from_layout.addRow(QLabel("Toplam Üye :\n"), self.toplam_üye)
        self.statistic_from_layout.addRow(QLabel("Mevcut Parça :\n"), self.mevcut_parca)
        self.statistic_group.setLayout(self.statistic_from_layout)
        statistics_main_layout.addWidget(self.statistic_group)


        self.tab9.setLayout(statistics_main_layout)
        self.tabs.blockSignals(False)


        ##############main çatı right layout################################
        ####################right side top search box#################################
        right_top_frame = QGroupBox(self)
        right_top_frame.setTitle("Veri Arama Bölümü")
        right_top_frame.setObjectName("Main")
        right_top_frame.setStyleSheet("#Main{background-color:#708090;font: 15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        right_top_frame_box = QHBoxLayout(right_top_frame)
        lbl_search = QLabel("Veri gir: ",right_top_frame)
        lbl_search.setStyleSheet("font:13pt Times Bold;color:white")
        self.fan_search_entry = QLineEdit(right_top_frame)
        self.fan_search_entry.setStyleSheet("border:2px solid gray;border-radius:5px")
        fan_search_button = QPushButton("Arama",right_top_frame)
        fan_search_button.setStyleSheet("background-color:#CD853F;font:13pt Times Bold;color:white")
        fan_search_button.clicked.connect(self.fanSearchBooks)
        right_top_frame_box.addStretch()
        right_top_frame_box.addWidget(lbl_search)
        right_top_frame_box.addWidget(self.fan_search_entry)#başka fonksiyonda kullanılcak self
        right_top_frame_box.addWidget(fan_search_button)
        # main_right_layout.addLayout(right_top_frame_box,20)  #%20
        right_top_frame_box.addStretch()
        fan_main_right_layout.addWidget(right_top_frame,20)
        ####################catiRight side list box#################################
        right_middle_frame = QGroupBox("Verileri Görüntüle",self)
        right_middle_frame.setObjectName("Main")
        right_middle_frame.setStyleSheet("#Main{background-color:#F0E68C;font:15pt Times Bold;color:white;border:2px solid gray;border-radius:15px}")
        self.fan_radio_btn1 = QRadioButton("Tüm veri",right_middle_frame)
        self.fan_radio_btn2 = QRadioButton("Açık",right_middle_frame)
        self.fan_radio_btn3 = QRadioButton("Kapalı",right_middle_frame)
        self.fan_btn_list = QPushButton("Listele",right_middle_frame)
        self.fan_btn_list.setStyleSheet("background-color:#CD5C5C;font:13pt Times Bold;color:white")
        self.fan_btn_list.clicked.connect(self.fanRadioButton)
        right_middle_box = QHBoxLayout(right_middle_frame)
        right_middle_box.addStretch()
        right_middle_box.addWidget(self.fan_radio_btn1)
        right_middle_box.addWidget(self.fan_radio_btn2)
        right_middle_box.addWidget(self.fan_radio_btn3)
        right_middle_box.addWidget(self.fan_btn_list)
        right_middle_box.addStretch()
        fan_main_right_layout.addWidget(right_middle_frame,20)
        #####################cati Right Side bottom Widgets#######################
        right_bottom_layout = QVBoxLayout()
        lbl_title = QLabel("Fan Durum")
        lbl_title.setContentsMargins(30,0,0,0)#SOL ÜST SAĞ ALT
        lbl_title.setFont(QFont("Times",20))
        right_bottom_layout.addWidget(lbl_title)
        img_library = QLabel("")
        img = QPixmap("icons/fan.png")
        img_library.setContentsMargins(60,0,0,0)
        img_library.setPixmap(img)
        right_bottom_layout.addWidget(img_library)
        fan_main_right_layout.addLayout(right_bottom_layout,60)










    def tabChanged(self,i):
        self.getTemperature()
        self.getHumiditiy()
        self.getWater()
        self.getLight()
        self.getCarbondioksit()
        self.getSeraKapak()
        self.getUye()
        self.getParca()
        self.getFan()
        self.gethava()






    def getTemperature(self):
        self.temperature_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.temperature_table.rowCount())):
            self.temperature_table.removeRow(i)
        query = cursor.execute("SELECT temperature_id,tarih,sicaklik,sicaklik2,sicaklik3,sicaklik4 FROM temperature")
        for row_data in query:
            row_number = self.temperature_table.rowCount()
            self.temperature_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.temperature_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        #QTimer.singleShot(1000,self.getTemperature)
        self.temperature_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler
    def temperatureSearchBooks(self):
        value = self.temperature_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT temperature_id,tarih,sicaklik,sicaklik2,sicaklik3,sicaklik4 FROM temperature "
                "WHERE tarih LIKE ? or sicaklik LIKE ? or sicaklik2 LIKE ? or sicaklik3 LIKE ? or sicaklik4 LIKE ?",
                (value,
                 value ,  value , value , value )).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade olamaz")
            else:
                for i in reversed(range(self.temperature_table.rowCount())):
                    self.temperature_table.removeRow(i)
                for row_data in query:
                    row_number = self.temperature_table.rowCount()
                    self.temperature_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.temperature_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def temperatureRadioButton(self):
        print(self.temperature_radio_btn1.isChecked())
        if self.temperature_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT temperature_id,tarih,sicaklik,sicaklik2,sicaklik3,sicaklik4 FROM temperature")
            for i in reversed(range(self.temperature_table.rowCount())):
                self.temperature_table.removeRow(i)
            for row_data in query:
                row_number = self.temperature_table.rowCount()
                self.temperature_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.temperature_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))


    def getHumiditiy(self):
        self.humidity_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.humidity_table.rowCount())):
            self.humidity_table.removeRow(i)
        query = cursor.execute("SELECT humidity_id,tarih,nem,nem2,nem3,nem4,nem5,nem6,nem7,nem8 FROM humidity")
        for row_data in query:
            row_number = self.humidity_table.rowCount()
            self.humidity_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.humidity_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.humidity_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler

    def humiditySearchBooks(self):
        value = self.humidity_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT humidity_id,tarih,nem FROM humidity "
                "WHERE tarih LIKE ? or nem LIKE ? or nem2 LIKE ? or nem3 LIKE ? or nem4 LIKE ? or nem5 LIKE ? or nem6 LIKE ? or nem7 LIKE ? or nem8 LIKE ?",
                (value,
                 value,value,value,value,value,value,value,value,value)).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı!!!", "Böyle bir nem değeri yok")
            else:
                for i in reversed(range(self.humidity_table.rowCount())):
                    self.humidity_table.removeRow(i)
                for row_data in query:
                    row_number = self.humidity_table.rowCount()
                    self.humidity_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.humidity_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def humidityRadioButton(self):
        print(self.humidity_radio_btn1.isChecked())
        if self.humidity_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT humidity_id,tarih,nem,nem2,nem3,nem4,nem5,nem6,nem7,nem8 FROM humidity")
            for i in reversed(range(self.humidity_table.rowCount())):
                self.humidity_table.removeRow(i)
            for row_data in query:
                row_number = self.humidity_table.rowCount()
                self.humidity_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.humidity_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def getWater(self):
        self.water_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.water_table.rowCount())):
            self.water_table.removeRow(i)
        query = cursor.execute("SELECT harcanansu_id,tarih,harcanan_su,toplam_su,pH,ec FROM harcanansumiktari")
        for row_data in query:
            row_number = self.water_table.rowCount()
            self.water_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.water_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.water_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler
    def waterSearchBooks(self):
        value = self.water_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT harcanansu_id,tarih,harcanan_su,toplam_su,pH,ec FROM harcanansumiktari "
                "WHERE tarih LIKE ? or harcanan_su LIKE ? or toplam_su LIKE ?, pH LIKE ?, ec LIKE ? ",
                (value,value,value,value,value)).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade yok")
            else:
                for i in reversed(range(self.water_table.rowCount())):
                    self.water_table.removeRow(i)
                for row_data in query:
                    row_number = self.water_table.rowCount()
                    self.water_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.water_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
    def  waterRadioButton(self):
        print(self.water_radio_btn1.isChecked())
        if self.water_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT harcanansu_id,tarih,harcanan_su,toplam_su,pH,ec FROM harcanansumiktari")
            for i in reversed(range(self.water_table.rowCount())):
                self.water_table.removeRow(i)
            for row_data in query:
                row_number = self.water_table.rowCount()
                self.water_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.water_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def gethava(self):
        self.hava_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.hava_table.rowCount())):
            self.hava_table.removeRow(i)
        query = cursor.execute("SELECT hava_id,hava_tarih,hava_nem FROM hava")
        for row_data in query:
            row_number = self.hava_table.rowCount()
            self.hava_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.hava_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.hava_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler

    def havaSearchBooks(self):
        value = self.hava_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT hava_id,hava_tarih,hava_nem FROM hava "
                "WHERE hava_tarih LIKE ? or hava_nem LIKE ?",
                ('%' + value + '%',
                 '%' + value + '%')).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade yok")
            else:
                for i in reversed(range(self.water_table.rowCount())):
                    self.hava_table.removeRow(i)
                for row_data in query:
                    row_number = self.hava_table.rowCount()
                    self.hava_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.hava_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def havaRadioButton(self):
        print(self.hava_radio_btn1.isChecked())
        if self.hava_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT hava_id,hava_tarih,hava_nem FROM hava")
            for i in reversed(range(self.water_table.rowCount())):
                self.hava_table.removeRow(i)
            for row_data in query:
                row_number = self.hava_table.rowCount()
                self.hava_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.hava_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def getLight(self):
        self.light_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.light_table.rowCount())):
            self.light_table.removeRow(i)
        query = cursor.execute("SELECT isik_id,tarih,isik_alma_süresi FROM isikalmasüresi")
        for row_data in query:
            row_number = self.light_table.rowCount()
            self.light_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.light_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.light_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler

    def lightSearchBooks(self):
        value = self.light_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT isik_id,tarih,isik_alma_süresi FROM isikalmasüresi "
                "WHERE tarih LIKE ? or isik_alma_süresi LIKE ?",
                ('%' + value + '%',
                 '%' + value + '%')).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade yok")
            else:
                for i in reversed(range(self.light_table.rowCount())):
                    self.light_table.removeRow(i)
                for row_data in query:
                    row_number = self.light_table.rowCount()
                    self.light_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.light_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
    def lightRadioButton(self):
        print(self.light_radio_btn1.isChecked())
        if self.light_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT isik_id,tarih,isik_alma_süresi FROM isikalmasüresi")
            for i in reversed(range(self.light_table.rowCount())):
                self.light_table.removeRow(i)
            for row_data in query:
                row_number = self.light_table.rowCount()
                self.light_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.light_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def getCarbondioksit(self):
        self.carbondioksit_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.carbondioksit_table.rowCount())):
            self.carbondioksit_table.removeRow(i)
        query = cursor.execute("SELECT carbondioksit_id,tarih,carbondioksit_alma_miktari FROM carbondioksitmiktari")
        for row_data in query:
            row_number = self.carbondioksit_table.rowCount()
            self.carbondioksit_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.carbondioksit_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.carbondioksit_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler

    def carbondioksitSearchBooks(self):
        value = self.carbondioksit_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT carbondioksit_id,tarih,carbondioksit_alma_miktari FROM carbondioksitmiktari "
                "WHERE tarih LIKE ? or carbondioksit_alma_miktari LIKE ?",
                ('%' + value + '%',
                 '%' + value + '%')).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade yok")
            else:
                for i in reversed(range(self.carbondioksit_table.rowCount())):
                    self.carbondioksit_table.removeRow(i)
                for row_data in query:
                    row_number = self.carbondioksit_table.rowCount()
                    self.carbondioksit_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.carbondioksit_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def carbondioksitRadioButton(self):
        print(self.carbondioksit_radio_btn1.isChecked())
        if self.carbondioksit_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT carbondioksit_id,tarih,carbondioksit_alma_miktari FROM carbondioksitmiktari")
            for i in reversed(range(self.carbondioksit_table.rowCount())):
                self.carbondioksit_table.removeRow(i)
            for row_data in query:
                row_number = self.carbondioksit_table.rowCount()
                self.carbondioksit_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.carbondioksit_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def getSeraKapak(self):
        self.sera_cati_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.sera_cati_table.rowCount())):
            self.sera_cati_table.removeRow(i)
        query = cursor.execute("SELECT sera_kapak_id,tarih,durum FROM seradurum")
        for row_data in query:
            row_number = self.sera_cati_table.rowCount()
            self.sera_cati_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.sera_cati_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.sera_cati_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler

    def catiSearchBooks(self):
        value = self.kapak_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT sera_kapak_id,tarih,durum FROM seradurum "
                "WHERE tarih LIKE ? or durum LIKE ?",
                ('%' + value + '%',
                 '%' + value + '%')).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade yok")
            else:
                for i in reversed(range(self.sera_cati_table.rowCount())):
                    self.sera_cati_table.removeRow(i)
                for row_data in query:
                    row_number = self.sera_cati_table.rowCount()
                    self.sera_cati_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.sera_cati_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
    def catiRadioButton(self):
        print(self.kapak_radio_btn1.isChecked())
        if self.kapak_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT sera_kapak_id,tarih,durum FROM seradurum")
            for i in reversed(range(self.sera_cati_table.rowCount())):
                self.sera_cati_table.removeRow(i)
            for row_data in query:
                row_number = self.sera_cati_table.rowCount()
                self.sera_cati_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.sera_cati_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
        elif self.kapak_radio_btn2.isChecked() == True:
            print(self.kapak_radio_btn2.isChecked())
            query = cursor.execute(
                "SELECT sera_kapak_id,tarih,durum FROM seradurum WHERE durum =?",
                ("Açık",))

            for i in reversed(range(self.sera_cati_table.rowCount())):
                self.sera_cati_table.removeRow(i)
            for row_data in query:

                row_number = self.sera_cati_table.rowCount()
                self.sera_cati_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.sera_cati_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
        elif self.kapak_radio_btn3.isChecked() == True:
            query = cursor.execute(
                "SELECT sera_kapak_id,tarih,durum FROM seradurum WHERE durum =?",
                ("Kapalı",))

            for i in reversed(range(self.sera_cati_table.rowCount())):
                self.sera_cati_table.removeRow(i)
            for row_data in query:

                row_number = self.sera_cati_table.rowCount()
                self.sera_cati_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.sera_cati_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def getUye(self):
        self.uye_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.uye_table.rowCount())):
            self.uye_table.removeRow(i)
        query = cursor.execute("SELECT üye_id,isim,telefon FROM üyeler")
        for row_data in query:
            row_number = self.uye_table.rowCount()
            self.uye_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.uye_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.uye_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler

    def searchMember(self):
        value = self.uye_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT üye_id,isim,telefon FROM üyeler "
                "WHERE isim LIKE ? or telefon LIKE ?",
                ('%' + value + '%',
                 '%' + value + '%')).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade yok")
            else:
                for i in reversed(range(self.uye_table.rowCount())):
                    self.uye_table.removeRow(i)
                for row_data in query:
                    row_number = self.uye_table.rowCount()
                    self.uye_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.uye_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
    def uyeRadioButton(self):
        print(self.üye_radio_btn1.isChecked())
        if self.üye_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT üye_id,isim,telefon FROM üyeler")
            for i in reversed(range(self.uye_table.rowCount())):
                self.uye_table.removeRow(i)
            for row_data in query:
                row_number = self.uye_table.rowCount()
                self.uye_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.uye_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def getParca(self):
        self.parca_bilgi_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.parca_bilgi_table.rowCount())):
            self.parca_bilgi_table.removeRow(i)
        query = cursor.execute("SELECT parca_id,parca_isim,parca_durum FROM parcadurum")
        for row_data in query:
            row_number = self.parca_bilgi_table.rowCount()
            self.parca_bilgi_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.parca_bilgi_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.parca_bilgi_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler

    def parcaSearchBooks(self):
        value = self.parca_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT parca_id,parca_isim,parca_durum FROM parcadurum "
                "WHERE parca_isim LIKE ? or parca_durum LIKE ?",
                ('%' + value + '%',
                 '%' + value + '%')).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade yok")
            else:
                for i in reversed(range(self.parca_bilgi_table.rowCount())):
                    self.parca_bilgi_table.removeRow(i)
                for row_data in query:
                    row_number = self.parca_bilgi_table.rowCount()
                    self.parca_bilgi_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.parca_bilgi_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))

    def parcaRadioButton(self):
        print(self.parca_radio_btn1.isChecked())
        if self.parca_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT parca_id,parca_isim,parca_durum FROM parcadurum")
            for i in reversed(range(self.parca_bilgi_table.rowCount())):
                self.parca_bilgi_table.removeRow(i)
            for row_data in query:
                row_number = self.parca_bilgi_table.rowCount()
                self.parca_bilgi_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.parca_bilgi_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
        elif self.parca_radio_btn2.isChecked() == True:
            print(self.parca_radio_btn2.isChecked())
            query = cursor.execute(
                "SELECT parca_id,parca_isim,parca_durum FROM parcadurum WHERE parca_durum =?",
                ("Mevcut",))

            for i in reversed(range(self.parca_bilgi_table.rowCount())):
                self.parca_bilgi_table.removeRow(i)
            for row_data in query:

                row_number = self.parca_bilgi_table.rowCount()
                self.parca_bilgi_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.parca_bilgi_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
        elif self.parca_radio_btn3.isChecked() == True:
            query = cursor.execute(
                "SELECT parca_id,parca_isim,parca_durum FROM parcadurum WHERE parca_durum =?",
                ("Mevcut Değil",))

            for i in reversed(range(self.parca_bilgi_table.rowCount())):
                self.parca_bilgi_table.removeRow(i)
            for row_data in query:

                row_number = self.parca_bilgi_table.rowCount()
                self.parca_bilgi_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.parca_bilgi_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))


    def getFan(self):
        self.fan_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.fan_table.rowCount())):
            self.fan_table.removeRow(i)
        query = cursor.execute("SELECT fan_id,tarih,fandurum FROM fandurum")
        for row_data in query:
            row_number = self.fan_table.rowCount()
            self.fan_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.fan_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # QTimer.singleShot(1000,self.getTemperature)
        self.fan_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # belgeler
    def fanSearchBooks(self):
        value = self.fan_search_entry.text()
        print(value)
        if value == "":
            QMessageBox.information(self, "Uyarı", "Arama bölümü boş olamaz")
        else:
            query = cursor.execute(
                "SELECT fan_id,tarih,fandurum FROM fandurum "
                "WHERE tarih LIKE ? or fandurum LIKE ?",
                ('%' + value + '%',
                 '%' + value + '%')).fetchall()  # içeren kelimelerin hepsini gösterir ve değerlerin hepsini getir
            print(query)

            if query == []:
                QMessageBox.information(self, "Uyarı", "Böyle bir ifade yok")
            else:
                for i in reversed(range(self.parca_bilgi_table.rowCount())):
                    self.fan_table.removeRow(i)
                for row_data in query:
                    row_number = self.fan_table.rowCount()
                    self.fan_table.insertRow(row_number)

                    for column_numbber, data in enumerate(row_data):
                        self.fan_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
    def fanRadioButton(self):
        print(self.fan_radio_btn1.isChecked())
        if self.fan_radio_btn1.isChecked() == True:
            query = cursor.execute(
                "SELECT fan_id,tarih,fandurum FROM fandurum")
            for i in reversed(range(self.fan_table.rowCount())):
                self.fan_table.removeRow(i)
            for row_data in query:
                row_number = self.fan_table.rowCount()
                self.fan_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.fan_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
        elif self.fan_radio_btn2.isChecked() == True:
            print(self.parca_radio_btn2.isChecked())
            query = cursor.execute(
                "SELECT fan_id,tarih,fandurum FROM fandurum WHERE fandurum =?",
                ("Açık",))

            for i in reversed(range(self.fan_table.rowCount())):
                self.fan_table.removeRow(i)
            for row_data in query:

                row_number = self.fan_table.rowCount()
                self.fan_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.fan_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))
        elif self.fan_radio_btn3.isChecked() == True:
            query = cursor.execute(
                "SELECT fan_id,tarih,fandurum FROM fandurum WHERE fandurum =?",
                ("Kapalı",))

            for i in reversed(range(self.fan_table.rowCount())):
                self.fan_table.removeRow(i)
            for row_data in query:

                row_number = self.fan_table.rowCount()
                self.fan_table.insertRow(row_number)

                for column_numbber, data in enumerate(row_data):
                    self.fan_table.setItem(row_number, column_numbber, QTableWidgetItem(str(data)))


















    def temperatureData(self):
        self.temperature = temperature.TemperaturePage()
    def HumidityData(self):
        self.humidity = humidity.HumidityPage()
    def havaData(self):
        self.hava = hava.HavaPage()

    def waterData(self):
        self.harcanansumiktari = harcanansumiktari.harcananSuMiktari()

    def lightData(self):
        self.isikmiktari = isikmiktari.isikMiktari()

    def carbondioksitData(self):
        self.carbondioksit = carbondioksit.carbondioksitMiktari()

    def seraKapak(self):
        self.serakapak = serakapak.seraKapak()

    def addMember(self):
        self.uyeekle = uyeekle.uyeEkle()

    def parcaBilgisi(self):
        self.parcabilgisi = parcabilgisi.parcaBilgisi()
    def fanControl(self):
        self.fandurum = fandurum.fanBilgisi()


    def getStatistics(self):
        average_temperature = cursor.execute("SELECT AVG(sicaklik) FROM temperature").fetchall()
        self.ortalama_sicaklik.setText(str(average_temperature[0][0])+" Cº\n")
        average_temperature = cursor.execute("SELECT AVG(sicaklik2) FROM temperature").fetchall()
        self.ortalama_sicaklik2.setText(str(average_temperature[0][0]) + " Cº\n")
        average_temperature = cursor.execute("SELECT AVG(sicaklik3) FROM temperature").fetchall()
        self.ortalama_sicaklik3.setText(str(average_temperature[0][0]) + " Cº\n")
        average_temperature = cursor.execute("SELECT AVG(sicaklik4) FROM temperature").fetchall()
        self.ortalama_sicaklik4.setText(str(average_temperature[0][0]) + " Cº\n")

        average_humidity = cursor.execute("SELECT AVG(nem) from humidity").fetchall()
        self.ortalama_nem.setText(str(average_humidity[0][0])+" %\n")
        average_humidity = cursor.execute("SELECT AVG(nem2) from humidity").fetchall()
        self.ortalama_nem2.setText(str(average_humidity[0][0]) + " %\n")
        average_humidity = cursor.execute("SELECT AVG(nem3) from humidity").fetchall()
        self.ortalama_nem3.setText(str(average_humidity[0][0]) + " %\n")
        average_humidity = cursor.execute("SELECT AVG(nem4) from humidity").fetchall()
        self.ortalama_nem4.setText(str(average_humidity[0][0]) + " %\n")
        average_humidity = cursor.execute("SELECT AVG(nem5) from humidity").fetchall()
        self.ortalama_nem5.setText(str(average_humidity[0][0]) + " %\n")
        average_humidity = cursor.execute("SELECT AVG(nem6) from humidity").fetchall()
        self.ortalama_nem6.setText(str(average_humidity[0][0]) + " %\n")
        average_humidity = cursor.execute("SELECT AVG(nem7) from humidity").fetchall()
        self.ortalama_nem7.setText(str(average_humidity[0][0]) + " %\n")
        average_humidity = cursor.execute("SELECT AVG(nem8) from humidity").fetchall()
        self.ortalama_nem8.setText(str(average_humidity[0][0]) + " %\n")




        total_water = cursor.execute("SELECT SUM(harcanan_su) from harcanansumiktari").fetchall()
        self.toplam_harcanan_su_miktari.setText(str(total_water[0][0])+" ml\n")
        average_water = cursor.execute("SELECT AVG(harcanan_su) from harcanansumiktari").fetchall()
        self.ortalama_harcanan_su_miktari.setText(str(average_water[0][0]) + " ml\n")
        average_light = cursor.execute("SELECT AVG(isik_alma_süresi) from isikalmasüresi").fetchall()
        self.ortalama_isik_alma_süresi.setText(str(average_light[0][0]) + " lux\n")
        average_co2 = cursor.execute("SELECT AVG(carbondioksit_alma_miktari) from carbondioksitmiktari").fetchall()
        self.ortalama_co2_miktari.setText(str(average_co2[0][0]) + " \n")
        total_member = cursor.execute("SELECT COUNT(üye_id) from üyeler").fetchall()
        self.toplam_üye.setText(str(total_member[0][0]) + " Kişi\n")
        total_parca = cursor.execute("SELECT COUNT(parca_id) from parcadurum").fetchall()
        self.mevcut_parca.setText(str(total_parca[0][0]) + " Adet\n")
        QTimer.singleShot(1000, self.getStatistics)




















    def selectedTemperatureTable(self):
        global temperature_id
        temperature_list = []
        for i in range(0, 3):  # 6 alan var
            temperature_list.append(self.temperature_table.item(self.temperature_table.currentRow(), i).text())

        print(temperature_list)
        temperature_id = temperature_list[0]
        self.displaytemperature = DisplayTemperature()
        self.displaytemperature.show()

    def selectedHumidityTable(self):
        global humidity_id
        humidity_list = []
        for i in range(0, 3):  # 6 alan var
            humidity_list.append(self.humidity_table.item(self.humidity_table.currentRow(), i).text())

        print(humidity_list)
        humidity_id = humidity_list[0]
        self.displayhumidity = DisplayHumidity()
        self.displayhumidity.show()
    def selectedhava(self):
        global hava_id
        hava_list = []
        for i in range(0, 3):  # 6 alan var
            hava_list.append(self.hava_table.item(self.hava_table.currentRow(), i).text())

        print(hava_list)
        hava_id = hava_list[0]
        self.displayhava = Displayhava()
        self.displayhava.show()
    def selectedWater(self):
        global water_id
        water_list = []
        for i in range(0, 3):  # 6 alan var
            water_list.append(self.water_table.item(self.water_table.currentRow(), i).text())

        print(water_list)
        water_id = water_list[0]
        self.displaywater = DisplayWater()
        self.displaywater.show()
    def selectedLight(self):
        global light_id
        light_list = []
        for i in range(0, 3):  # 6 alan var
            light_list.append(self.light_table.item(self.light_table.currentRow(), i).text())

        print(light_list)
        light_id = light_list[0]
        self.displaylight = DisplayLight()
        self.displaylight.show()
    def selectedCarbondioksit(self):
        global carbondioksit_id
        carbondioksit_list = []
        for i in range(0, 3):  # 6 alan var
            carbondioksit_list.append(self.carbondioksit_table.item(self.carbondioksit_table.currentRow(), i).text())

        print(carbondioksit_list)
        carbondioksit_id = carbondioksit_list[0]
        self.displaycarbondioksit = DisplayCarbondioksit()
        self.displaycarbondioksit.show()

    def selectedCati(self):
        global cati_id
        cati_list = []
        for i in range(0, 3):  # 6 alan var
            cati_list.append(self.sera_cati_table.item(self.sera_cati_table.currentRow(), i).text())

        print(cati_list)
        cati_id = cati_list[0]
        self.displaycati = DisplayCati()
        self.displaycati.show()

    def selectedUye(self):
        global uye_id
        uye_list = []
        for i in range(0, 3):  # 6 alan var
            uye_list.append(self.uye_table.item(self.uye_table.currentRow(), i).text())

        print(uye_list)
        uye_id = uye_list[0]
        self.displauye = DisplayUye()
        self.displauye.show()

    def selectedParca(self):
        global parca_id
        parca_list = []
        for i in range(0, 3):  # 6 alan var
            parca_list.append(self.parca_bilgi_table.item(self.parca_bilgi_table.currentRow(), i).text())

        print(parca_list)
        parca_id = parca_list[0]
        self.displayparca = DisplayParca()
        self.displayparca.show()

    def selectedFan(self):
        global fan_id
        fan_list = []
        for i in range(0, 3):  # 6 alan var
            fan_list.append(self.fan_table.item(self.fan_table.currentRow(), i).text())

        print(fan_list)
        fan_id = fan_list[0]
        self.displayfan = DisplayFan()
        self.displayfan.show()


















    def statusbar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def funcTextChanged(self):
        global textChanged
        textChanged = True
        text = self.veri_bilgi.toPlainText()
        letters = len(text)
        words = len(text.split())
        self.status_bar.showMessage("Harf Sayısı : " + str(letters) + " Kelime Sayısı :" + str(words))

    def dockbar(self):
        self.dock = QDockWidget("Kısayollar", self)
        self.dock.setAllowedAreas( Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea)  # hangi bölgelere taşımak istiyorsak
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)  # solda görünsün
        self.dockWidget = QWidget(self)
        self.dock.setWidget(self.dockWidget)
        formLayout = QFormLayout()
        #######################################################
        btnFind = QToolButton()
        btnFind.setIcon(QIcon("icons/reference.png"))
        btnFind.setText("Kelime Bul")
        btnFind.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnFind.setIconSize(QSize(50, 50))
        btnFind.setCheckable(True)
        btnFind.toggled.connect(self.Find)
        #######################################################
        btnNew = QToolButton()
        btnNew.setIcon(QIcon("icons/new4.png"))
        btnNew.setText("Yeni")
        btnNew.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnNew.setIconSize(QSize(50, 50))
        btnNew.setCheckable(True)
        btnNew.toggled.connect(self.newFile)
        #######################################################
        btnOpen = QToolButton()
        btnOpen.setIcon(QIcon("icons/open3.png"))
        btnOpen.setText("Dosya Aç")
        btnOpen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnOpen.setIconSize(QSize(50, 50))
        btnOpen.setCheckable(True)
        btnOpen.toggled.connect(self.openFile)
        #######################################################
        btnSave = QToolButton()
        btnSave.setIcon(QIcon("icons/save2.png"))
        btnSave.setText("Kaydet")
        btnSave.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnSave.setIconSize(QSize(50, 50))
        btnSave.setCheckable(True)
        btnSave.toggled.connect(self.saveFile)
        #######################################################
        formLayout.addRow(btnFind, btnNew)
        formLayout.addRow(btnOpen, btnSave)
        self.dockWidget.setLayout(formLayout)
        self.veri_degistir_main_left_layout.addLayout(formLayout)
        self.tab10.setLayout(self.veri_degistir_main_layout)

        #########################Dock Bar BİTİŞ##############################
        # veri_degistir_main_layout = QHBoxLayout()
        # veri_degistir_main_left_layout = QVBoxLayout()
        # veri_degistir_main_layout.addLayout(veri_degistir_main_left_layout)
        # veri_degistir_main_layout.addWidget(self.veri_bilgi)
        # self.tab10.setLayout(veri_degistir_main_layout)


    def ButtonChangeText(self):
        self.tb = self.addToolBar("Tool Bar")
        self.fontFamily = QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.changeFont)
        self.tb.addWidget(self.fontFamily)
        self.veri_degistir_main_left_layout.addWidget(self.tb)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    ####################################################################
        self.fontSize = QComboBox(self)
        self.fontSize.setEditable(True)  # yazılabilir oldu
        for i in range(12, 101):
            self.fontSize.addItem(str(i))
        self.fontSize.setCurrentText("12")
        self.fontSize.currentTextChanged.connect(self.changeFontSize)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.fontSize)
        self.tb.addWidget(self.fontSize)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.bold = QPushButton(QIcon("icons/bold.png"), "", self)
        self.bold.clicked.connect(self.Bold)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.bold)
        self.tb.addWidget(self.bold)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.italic = QPushButton(QIcon("icons/italic.png"), "", self)
        self.italic.clicked.connect(self.Italic)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.italic)
        self.tb.addWidget(self.italic)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.underline = QPushButton(QIcon("icons/underline.png"), "", self)
        self.underline.clicked.connect(self.Underline)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.underline)
        self.tb.addWidget(self.underline)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.fontColor = QPushButton(QIcon("icons/color.png"), "", self)
        self.fontColor.clicked.connect(self.FontColor)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.fontColor)
        self.tb.addWidget(self.fontColor)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.fontBackColor = QPushButton(QIcon("icons/backcolor.png"), "", self)
        self.fontBackColor.clicked.connect(self.FontBackColor)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.fontBackColor)
        self.tb.addWidget(self.fontBackColor)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.alignLeft = QPushButton(QIcon("icons/alignleft.png"), "", self)
        self.alignLeft.clicked.connect(self.AlignLeft)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.alignLeft)
        self.tb.addWidget(self.alignLeft)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.alignCenter = QPushButton(QIcon("icons/aligncenter.png"), "", self)
        self.alignCenter.clicked.connect(self.AlignCenter)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.alignCenter)
        self.tb.addWidget(self.alignCenter)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.alignRight = QPushButton(QIcon("icons/aligncenter.png"), "", self)
        self.alignRight.clicked.connect(self.AlignRight)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.alignRight)
        self.tb.addWidget(self.alignRight)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.alignJustify = QPushButton(QIcon("icons/alignJustify.png"), "", self)
        self.alignJustify.clicked.connect(self.AlignJustify)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.alignJustify)
        self.tb.addWidget(self.alignJustify)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.bulletList = QPushButton(QIcon("icons/bulletlist.png"), "", self)
        self.bulletList.clicked.connect(self.BulletList)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.bulletList)
        self.tb.addWidget(self.bulletList)
        self.tab10.setLayout(self.veri_degistir_main_layout)
    #####################################################################
        self.numberedList = QPushButton(QIcon("icons/numberlist.png"), "", self)
        self.numberedList.clicked.connect(self.NumberedList)
        self.tb.addSeparator()
        self.tb.addSeparator()
        self.veri_degistir_main_left_layout.addWidget(self.numberedList)
        self.tb.addWidget(self.numberedList)
        self.tab10.setLayout(self.veri_degistir_main_layout)






    def changeFont(self):
        font = QFont(self.fontFamily.currentFont())
        self.veri_bilgi.setCurrentFont(font)
    def changeFontSize(self,fontSize):
        self.veri_bilgi.setFontPointSize(float(fontSize))
    def Bold(self):
        fontWeight = self.veri_bilgi.fontWeight()
        if fontWeight == 50:
            self.veri_bilgi.setFontWeight(QFont.Bold)
        elif fontWeight == 75:
            self.veri_bilgi.setFontWeight(QFont.Normal)
    def Italic(self):
        italic = self.veri_bilgi.fontItalic()
        if italic == True:
            self.veri_bilgi.setFontItalic(False)
        else:
            self.veri_bilgi.setFontItalic(True)
    def Underline(self):
        underline = self.veri_bilgi.fontUnderline()
        if underline == True:
            self.veri_bilgi.setFontUnderline(False)
        else:
            self.veri_bilgi.setFontUnderline(True)
    def FontColor(self):
        color = QColorDialog.getColor()
        self.veri_bilgi.setTextColor(color)
    def FontBackColor(self):
        bcolor = QColorDialog.getColor()
        self.veri_bilgi.setTextBackgroundColor(bcolor)
    def AlignJustify(self):
        self.veri_bilgi.setAlignment(Qt.AlignJustify)
    def AlignRight(self):
        self.veri_bilgi.setAlignment(Qt.AlignRight)
    def AlignLeft(self):
        self.veri_bilgi.setAlignment(Qt.AlignLeft)
    def AlignCenter(self):
        self.veri_bilgi.setAlignment(Qt.AlignCenter)
    def BulletList(self):
        self.veri_bilgi.insertHtml("<ul><li><h3>&nbsp;</h3><li></ul>")
    def NumberedList(self):
        self.veri_bilgi.insertHtml("<ol><li><h3>&nbsp;</h3><lis></ol>")


























    def newFile(self):
        try:
            global url
            url = ""
            self.veri_bilgi.clear()

        except:
            pass
    def openFile(self):
        global url
        try:
            url = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "All Files(*);;Txt Files *txt")
            with open(url[0], "r+", encoding="utf-8") as file:
                content = file.read()
                self.veri_bilgi.clear()  # mevcut yazının yazmaması için
                self.veri_bilgi.setText(content)
        except:
            pass
    def saveFile(self):
        global url
        try:
            if textChanged == True:
                if url != "":
                    content = self.veri_bilgi.toPlainText()
                    with open(url[0], "w", encoding="utf-8") as file:
                        file.write(content)
                else:
                    url = QFileDialog.getSaveFileName(self, "Dosyayı Kayıt Et", "", "Txt files(*.txt)")
                    content2 = self.veri_bilgi.toPlainText()
                    with open(url[0], "w", encoding="utf-8") as file2:
                        file2.write(content2)
        except:
            pass
    def exitFile(self):
        global url
        try:
            if textChanged == True:
                mbox = QMessageBox.information(self, "Dikkat", "Dosyayı kayıt etmek istiyor musunuz ?",
                                               QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel,
                                               QMessageBox.Cancel)

                if mbox == QMessageBox.Save:
                    if url != "":
                        content = self.veri_bilgi.toPlainText()
                        with open(url[0], "w", encoding="utf-8") as file:
                            file.write(content)
                    else:
                        url = QFileDialog.getSaveFileName(self, "Dosya Kaydet", "", "Txt files(*.txt)")
                        content2 = self.veri_bilgi.toPlainText()
                        with open(url[0], "w", encoding="utf-8") as file2:
                            file2.write(content2)
                elif mbox == QMessageBox.No:
                    qApp.quit()

            else:
                qApp.quit()
        except:
            pass
    def Undo(self):
        self.veri_bilgi.undo()
    def Cut(self):
        self.veri_bilgi.cut()
    def Copy(self):
        self.veri_bilgi.copy()
    def Paste(self):
        self.veri_bilgi.paste()

    def Find(self):
        global f

        find = Find(self)
        find.show()

        def handleFind():

            f = find.te.toPlainText()
            print(f)

            if cs == True and wwo == False:
                flag = QTextDocument.FindBackward and QTextDocument.FindCaseSensitively

            elif cs == False and wwo == False:
                flag = QTextDocument.FindBackward

            elif cs == False and wwo == True:
                flag = QTextDocument.FindBackward and QTextDocument.FindWholeWords

            elif cs == True and wwo == True:
                flag = QTextDocument.FindBackward and QTextDocument.FindCaseSensitively and QTextDocument.FindWholeWords

            self.veri_bilgi.find(f, flag)

        def handleReplace():
            f = find.te.toPlainText()
            r = find.rp.toPlainText()

            text = self.veri_bilgi.toPlainText()

            newText = text.replace(f, r)

            self.veri_bilgi.clear()
            self.veri_bilgi.append(newText)

        find.src.clicked.connect(handleFind)
        find.rpb.clicked.connect(handleReplace)
    def Time_Date(self):
        time_date = time.strftime("%d,%m,%Y %H:%M")
        self.veri_bilgi.append(time_date)
    def funcToggleStatusBar(self):
        global statusbarChecked
        if statusbarChecked == True:
            self.status_bar.hide()
            statusbarChecked = False

        else:
            self.status_bar.show()
            statusbarChecked = True
    def funcToogleToolBar(self):
        global tbcheched
        if tbcheched == True:
            self.tb.hide()
            tbcheched = False
        else:
            self.tb.show()
            tbcheched = True
    def funcToogleDockBar(self):
        global dockChecked
        if dockChecked == True:
            self.dock.hide()
            dockChecked = False
        else:
            self.dock.show()
            dockChecked = True
    def About(self):
        self.help = about.Help()
        self.help.show()




    def GraphGoster(self):
        self.grafik = grafikgoster.SicaklikToprakNemGrafigiLinear()
        self.grafik.show()
    def GraphGoster2(self):
        self.grafik7 = grafikgoster7.SicaklikToprakNemGrafigiBar()
        self.grafik7.show()
    def GraphGoster3(self):
        self.grafik5 = grafikgoster5.IsıkSiddeti()
        self.grafik5.show()
    def GraphGoster4(self):
        self.grafik6 = grafikgoster6.HavaKalitesi()
        self.grafik6.show()
    def GraphGoster6(self):
        self.grafik2 = grafikgoster2.SıcaklıkC1C2C3C4()
        self.grafik2.show()
    def GraphGoster7(self):
        self.grafik3 = grafikgoster3.SaksıNemleri()
        self.grafik3.show()
    def GraphGoster8(self):
        self.grafik4 = grafikgoster4.HarcananSu()
        self.grafik4.show()

    def GraphGoster9(self):
        self.grafik8 = grafikgoster8.SıcaklıkHarcananSuGrafigiLinear()
        self.grafik8.show()
    def GraphGoster10(self):
        self.grafik9 = grafikgoster9.SıcaklıkHarcananSuGrafigiBar()
        self.grafik9.show()






class DisplayTemperature(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sıcaklığı Göster")
        self.setWindowIcon(QIcon("icons/temperature.ico"))
        self.setGeometry(450, 150, 550, 550)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global temperature_id
        temperature = cursor.execute("SELECT * FROM temperature WHERE temperature_id=?",(temperature_id,)).fetchall()
        print(temperature)
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
        lbl_title = QLabel("Sıcaklık Detayı", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(temperature[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(temperature[0][2]))
        self.author_entry.setStyleSheet("background-color:white")
        self.author_entry2 = QLineEdit(bottomFrame)
        self.author_entry2.setText(str(temperature[0][3]))
        self.author_entry2.setStyleSheet("background-color:white")
        self.author_entry3 = QLineEdit(bottomFrame)
        self.author_entry3.setText(str(temperature[0][4]))
        self.author_entry3.setStyleSheet("background-color:white")
        self.author_entry4 = QLineEdit(bottomFrame)
        self.author_entry4.setText(str(temperature[0][5]))
        self.author_entry4.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deleteTemperature)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateTemperature)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("Sıcaklık Cº-1-ÖN :"), self.author_entry)
        bottom_layout.addRow(QLabel("Sıcaklık Cº-2-ARKA"), self.author_entry2)
        bottom_layout.addRow(QLabel("Sıcaklık Cº-3-SOL :"), self.author_entry3)
        bottom_layout.addRow(QLabel("Sıcaklık Cº-4-SAĞ :"), self.author_entry4)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def deleteTemperature(self):
        global temperature_id
        mbox = QMessageBox.question(self,"Uyarı","Sıcaklık değerini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM temperature WHERE temperature_id =?",(temperature_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Sıcaklık değeri silindi")

            except:
                QMessageBox.information(self,"Bilgi","Sıcaklık değeri silinemedi")
    def UpdateTemperature(self):
        tarih = self.name_entry.text()
        sicaklik = self.author_entry.text()
        sicaklik2 = self.author_entry.text()
        sicaklik3 = self.author_entry.text()
        sicaklik4 = self.author_entry.text()
        global temperature_id
        if (tarih and sicaklik != ""):
            try:
                query = "UPDATE temperature SET tarih=?,sicaklik=?,sicaklik2=?,sicaklik3=?,sicaklik4=?    WHERE temperature_id=?"
                cursor.execute(query, (tarih, sicaklik,sicaklik2,sicaklik3,sicaklik4, temperature_id))
                connection.commit()
                QMessageBox.information(self, "Sıcaklık Bilgisi Düzenlendi", "Sıcaklık Bilgisi Düzenlendi")

            except:
                QMessageBox.information(self, "Sıcaklık Bilgisi Düzenlenemedi", "Sıcaklık Bilgisi Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")


class Displayhava(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hava Nem Oranını Göster")
        self.setWindowIcon(QIcon("icons/hava.ico"))
        self.setGeometry(450, 150, 750, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global hava_id
        hava= cursor.execute("SELECT * FROM hava WHERE hava_id=?",(hava_id,)).fetchall()
        print(hava)
        self.setStyleSheet("background-color:white")
        main_layout = QVBoxLayout()

        topFrame = QFrame(self)
        topFrame.setStyleSheet("background-color:white")
        top_layout = QHBoxLayout(topFrame)
        bottomFrame = QFrame(self)
        bottom_layout = QFormLayout(bottomFrame)
        bottomFrame.setStyleSheet("font:15pt Times Bold;background-color:#fcc324")

        img_book = QLabel(topFrame)
        img = QPixmap("icons/havanemips.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Hava Nem Oranı Detayı", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(hava[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(hava[0][2]))
        self.author_entry.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deletehava)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.Updatehava)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("Hava Nem % :"), self.author_entry)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def deletehava(self):
        global hava_id
        mbox = QMessageBox.question(self,"Uyarı","Nem değerini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM hava WHERE hava_id =?",(hava_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Nem değeri silindi")

            except:
                QMessageBox.information(self,"Bilgi","Nem değeri silinemedi")
    def Updatehava(self):
        tarih = self.name_entry.text()
        nem = self.author_entry.text()
        global water_id
        if (tarih and nem != ""):
            try:
                query = "UPDATE hava SET hava_tarih=?,hava_nem=? WHERE hava_id=?"
                cursor.execute(query, (tarih, nem, hava_id))
                connection.commit()
                QMessageBox.information(self, "Hava nem Bilgisi Düzenlendi", "Hava nem Bilgisi Düzenlendi")

            except:
                QMessageBox.information(self, "Hava Bilgisi Düzenlenemedi", "Hava nem Bilgisi Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")




class DisplayHumidity(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nem Değerini Göster")
        self.setWindowIcon(QIcon("icons/topraknemi.ico"))
        self.setGeometry(450, 150, 650, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global humidity_id
        humidity = cursor.execute("SELECT * FROM humidity WHERE humidity_id=?",(humidity_id,)).fetchall()
        print(humidity)
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
        lbl_title = QLabel("Nem Detayı", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(humidity[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(humidity[0][2]))
        self.author_entry.setStyleSheet("background-color:white")
        self.author_entry2 = QLineEdit(bottomFrame)
        self.author_entry2.setText(str(humidity[0][3]))
        self.author_entry2.setStyleSheet("background-color:white")
        self.author_entry3 = QLineEdit(bottomFrame)
        self.author_entry3.setText(str(humidity[0][4]))
        self.author_entry3.setStyleSheet("background-color:white")
        self.author_entry4 = QLineEdit(bottomFrame)
        self.author_entry4.setText(str(humidity[0][5]))
        self.author_entry4.setStyleSheet("background-color:white")
        self.author_entry5 = QLineEdit(bottomFrame)
        self.author_entry5.setText(str(humidity[0][6]))
        self.author_entry5.setStyleSheet("background-color:white")
        self.author_entry6 = QLineEdit(bottomFrame)
        self.author_entry6.setText(str(humidity[0][7]))
        self.author_entry6.setStyleSheet("background-color:white")
        self.author_entry7 = QLineEdit(bottomFrame)
        self.author_entry7.setText(str(humidity[0][8]))
        self.author_entry7.setStyleSheet("background-color:white")
        self.author_entry8 = QLineEdit(bottomFrame)
        self.author_entry8.setText(str(humidity[0][9]))
        self.author_entry8.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deleteHumidity)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateHumidity)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("1.Saksı Nem % :"), self.author_entry)
        bottom_layout.addRow(QLabel("2.Saksı Nem % :"), self.author_entry2)
        bottom_layout.addRow(QLabel("3.Saksı Nem % :"), self.author_entry3)
        bottom_layout.addRow(QLabel("4.Saksı Nem % :"), self.author_entry4)
        bottom_layout.addRow(QLabel("5.Saksı Nem % :"), self.author_entry5)
        bottom_layout.addRow(QLabel("6.Saksı Nem % :"), self.author_entry6)
        bottom_layout.addRow(QLabel("7.Saksı Nem % :"), self.author_entry7)
        bottom_layout.addRow(QLabel("8.Saksı Nem % :"), self.author_entry8)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def deleteHumidity(self):
        global humidity_id
        mbox = QMessageBox.question(self,"Uyarı","Nem değerini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM humidity WHERE humidity_id =?",(humidity_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Nem değeri silindi")

            except:
                QMessageBox.information(self,"Bilgi","Nem değeri silinemedi")
    def UpdateHumidity(self):
        tarih = self.name_entry.text()
        nem = self.author_entry.text()
        nem2 = self.author_entry2.text()
        nem3 = self.author_entry3.text()
        nem4 = self.author_entry4.text()
        nem5 = self.author_entry5.text()
        nem6 = self.author_entry6.text()
        nem7 = self.author_entry7.text()
        nem8 = self.author_entry8.text()
        global humidity_id
        if (tarih and nem != ""):
            try:
                query = "UPDATE humidity SET tarih=?,nem=?,nem2=?,nem3=?,nem4=?,nem5=?,nem6=?,nem7=?,nem8=? WHERE humidity_id=?"
                cursor.execute(query, (tarih, nem,nem2,nem3,nem4,nem5,nem6,nem7,nem8, humidity_id))
                connection.commit()
                QMessageBox.information(self, "Nem Bilgisi Düzenlendi", "Nem Bilgisi Düzenlendi")

            except:
                QMessageBox.information(self, "Nem Bilgisi Düzenlenemedi", "Nem Bilgisi Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")




class DisplayWater(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Harcanan Su Miktarını Göster")
        self.setWindowIcon(QIcon("icons/water.ico"))
        self.setGeometry(450, 150, 750, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global water_id
        water = cursor.execute("SELECT * FROM harcanansumiktari WHERE harcanansu_id=?",(water_id,)).fetchall()
        print(water)
        self.setStyleSheet("background-color:white")
        main_layout = QVBoxLayout()

        topFrame = QFrame(self)
        topFrame.setStyleSheet("background-color:white")
        top_layout = QHBoxLayout(topFrame)
        bottomFrame = QFrame(self)
        bottom_layout = QFormLayout(bottomFrame)
        bottomFrame.setStyleSheet("font:15pt Times Bold;background-color:#fcc324")

        img_book = QLabel(topFrame)
        img = QPixmap("icons/watertankps.png")
        img_book.setPixmap(img)
        lbl_title = QLabel("Harcanan Su Miktarı Detayı", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(water[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(water[0][2]))
        self.author_entry.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deleteWater)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateWater)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("Mililitre ml:"), self.author_entry)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def deleteWater(self):
        global water_id
        mbox = QMessageBox.question(self,"Uyarı","Nem değerini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM harcanansumiktari WHERE harcanansu_id =?",(water_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Nem değeri silindi")

            except:
                QMessageBox.information(self,"Bilgi","Nem değeri silinemedi")
    def UpdateWater(self):
        tarih = self.name_entry.text()
        mililitre = self.author_entry.text()
        global water_id
        if (tarih and mililitre != ""):
            try:
                query = "UPDATE harcanansumiktari SET tarih=?,harcanan_su=?,toplam_su=?,pH=?,ec=? WHERE harcanansu_id=?"
                cursor.execute(query, (tarih, mililitre, water_id))
                connection.commit()
                QMessageBox.information(self, "Su Bilgisi Düzenlendi", "Su Bilgisi Düzenlendi")

            except:
                QMessageBox.information(self, "Su Bilgisi Düzenlenemedi", "Su Bilgisi Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")



class DisplayLight(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Işık Şiddeti Göster")
        self.setWindowIcon(QIcon("icons/idea.ico"))
        self.setGeometry(450, 150, 650, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):
        #######Getting book details from database#############
        global light_id
        light = cursor.execute("SELECT * FROM isikalmasüresi WHERE isik_id=?",(light_id,)).fetchall()
        print(light)
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
        lbl_title = QLabel("Işık Şiddeti  Detayı", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(light[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(light[0][2]))
        self.author_entry.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deleteLight)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateLight)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("Işık Şiddeti Lux:"), self.author_entry)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def deleteLight(self):
        global light_id
        mbox = QMessageBox.question(self,"Uyarı","Işık Miktarı değerini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM isikalmasüresi WHERE isik_id =?",(light_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Işık Alma değeri silindi")

            except:
                QMessageBox.information(self,"Bilgi","Işık Alma değeri silinemedi")
    def UpdateLight(self):
        tarih = self.name_entry.text()
        isik_alma_süresi = self.author_entry.text()
        global light_id
        if (tarih and isik_alma_süresi != ""):
            try:
                query = "UPDATE isikalmasüresi SET tarih=?,isik_alma_süresi=? WHERE isik_id=?"
                cursor.execute(query, (tarih, isik_alma_süresi, light_id))
                connection.commit()
                QMessageBox.information(self, "Işık Bilgisi Düzenlendi", "Işık Bilgisi Düzenlendi")

            except:
                QMessageBox.information(self, "Işık Bilgisi Düzenlenemedi", "Işık Bilgisi Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")





class DisplayCarbondioksit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Karbondioksit Oranı Miktarını Göster")
        self.setWindowIcon(QIcon("icons/co2.ico"))
        self.setGeometry(450, 150, 650, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global carbondioksit_id
        carbondioksit = cursor.execute("SELECT * FROM carbondioksitmiktari WHERE carbondioksit_id=?",(carbondioksit_id,)).fetchall()
        print(carbondioksit)
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
        lbl_title = QLabel("CO2 Miktarı Detayı", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(carbondioksit[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(carbondioksit[0][2]))
        self.author_entry.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deleteCarbondioksit)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateCarbondioksit)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("Co2 Alma Miktarı % :"), self.author_entry)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def deleteCarbondioksit(self):
        global carbondioksit_id
        mbox = QMessageBox.question(self,"Uyarı","Işık Miktarı değerini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM carbondioksitmiktari WHERE carbondioksit_id =?",(carbondioksit_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Karbondioksit Oranı Miktar değeri silindi")

            except:
                QMessageBox.information(self,"Bilgi","Karbondioksit Oranı Miktar değeri silinemedi")

    def UpdateCarbondioksit(self):
        tarih = self.name_entry.text()
        carbondioksit_alma_miktari = self.author_entry.text()
        global carbondioksit_id
        if (tarih and carbondioksit_alma_miktari != ""):
            try:
                query = "UPDATE carbondioksitmiktari SET tarih=?,carbondioksit_alma_miktari=? WHERE carbondioksit_id=?"
                cursor.execute(query, (tarih, carbondioksit_alma_miktari, carbondioksit_id))
                connection.commit()
                QMessageBox.information(self, "Karbondioksit Oranı Bilgisi Düzenlendi", "Karbondioksit Oranı Bilgisi Düzenlendi")

            except:
                QMessageBox.information(self, "Karbondioksit Oranı Bilgisi Düzenlenemedi", "Karbondioksit Oranı Bilgisi Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")





class DisplayCati(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sera Kapak Durumunu Göster")
        self.setWindowIcon(QIcon("icons/serakapak.ico"))
        self.setGeometry(450, 150, 650, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global cati_id
        cati = cursor.execute("SELECT * FROM seradurum WHERE sera_kapak_id=?",(cati_id,)).fetchall()
        print(cati)
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
        lbl_title = QLabel("Sera Kapak Durumu", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(cati[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(cati[0][2]))
        self.author_entry.setStyleSheet("background-color:white")

        add_button = QPushButton("Delete", bottomFrame)
        add_button.clicked.connect(self.deleteCati)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateCati)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("Çatı Durumu :"), self.author_entry)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def deleteCati(self):
        global cati_id
        mbox = QMessageBox.question(self,"Uyarı","Çatı durumunu silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM seradurum WHERE sera_kapak_id =?",(cati_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Çatı durumunu silindi")

            except:
                QMessageBox.information(self,"Bilgi","Çatı durumunu silinemedi")
    def UpdateCati(self):
        tarih = self.name_entry.text()
        durum= self.author_entry.text()
        global cati_id
        if (tarih and durum != ""):
            try:
                query = "UPDATE seradurum SET tarih=?,durum=? WHERE sera_kapak_id=?"
                cursor.execute(query, (tarih,durum,cati_id))
                connection.commit()
                QMessageBox.information(self, "Çatı Bilgisi Düzenlendi", "Çatı Bilgisi Düzenlendi")

            except:
                QMessageBox.information(self, "Çatı Bilgisi Düzenlenemedi", "Çatı Bilgisi Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")







class DisplayUye(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Üye Bilgisi Göster")
        self.setWindowIcon(QIcon("icons/addperson.ico"))
        self.setGeometry(450, 150, 650, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global uye_id
        uye = cursor.execute("SELECT * FROM üyeler WHERE üye_id=?",(uye_id,)).fetchall()
        print(uye)
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
        lbl_title = QLabel("Üye Bilgisi", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(uye[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(uye[0][2]))
        self.author_entry.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deleteUye)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateUye)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("Telefon :"), self.author_entry)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)
        main_layout.addWidget(bottomFrame)

        self.setLayout(main_layout)

    def deleteUye(self):
        global uye_id
        mbox = QMessageBox.question(self,"Uyarı","Üye bilgisini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM üyeler WHERE üye_id =?",(uye_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Üye Bilgisi silindi")

            except:
                QMessageBox.information(self,"Bilgi","Üye Bilgisi silinemedi")

    def UpdateUye(self):
        isim = self.name_entry.text()
        telefon= self.author_entry.text()
        global uye_id
        if (isim and telefon != ""):
            try:
                query = "UPDATE üyeler SET isim=?,telefon=? WHERE üye_id=?"
                cursor.execute(query, (isim,telefon,uye_id))
                connection.commit()
                QMessageBox.information(self, "Üye Bilgisi Düzenlendi", "Üye BilgisiDüzenlendi")

            except:
                QMessageBox.information(self, "Üye Bilgisi Düzenlenemedi", "Üye Bilgisi Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")







class DisplayParca(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Üye Bilgisi Göster")
        self.setWindowIcon(QIcon("icons/parca.ico"))
        self.setGeometry(450, 150, 650, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global parca_id
        parca = cursor.execute("SELECT * FROM parcadurum WHERE parca_id=?",(parca_id,)).fetchall()
        print(parca)
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
        lbl_title = QLabel("Parça Bilgisi", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(parca[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(parca[0][2]))
        self.author_entry.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deleteParca)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateParca)
        bottom_layout.addRow(QLabel("Parça Adı :"), self.name_entry)
        bottom_layout.addRow(QLabel("Parça Durum :"), self.author_entry)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)



        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def deleteParca(self):
        global parca_id
        mbox = QMessageBox.question(self,"Uyarı","Parça bilgisini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM parcadurum WHERE parca_id =?",(parca_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Parça Bilgisi silindi")

            except:
                QMessageBox.information(self,"Bilgi","Parça Bilgisi silinemedi")


    def UpdateParca(self):
        parca_isim = self.name_entry.text()
        parca_durum= self.author_entry.text()
        global parca_id
        if (parca_isim and parca_durum != ""):
            try:
                query = "UPDATE parcadurum SET parca_isim=?,parca_durum=? WHERE parca_id=?"
                cursor.execute(query, (parca_isim,parca_durum,parca_id))
                connection.commit()
                QMessageBox.information(self, "Parça Düzenlendi", "Parça Düzenlendi")

            except:
                QMessageBox.information(self, "Parça Düzenlenemedi", "Parça Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")



class DisplayFan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fan Bilgisi Göster")
        self.setWindowIcon(QIcon("icons/fan.ico"))
        self.setGeometry(450, 150, 650, 650)
        self.setFixedSize(self.size())  # kullanıcı pencereyi büyültemez küçültemez
        self.UI()
        self.show()

    def UI(self):

        global fan_id
        fan = cursor.execute("SELECT * FROM fandurum WHERE fan_id=?",(fan_id,)).fetchall()
        print(fan)
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
        lbl_title = QLabel("Fan Durum", topFrame)
        lbl_title.setStyleSheet("color:#003f8a;font:25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ###############bottom frame DESİGN##################

        self.name_entry = QLineEdit(bottomFrame)
        self.name_entry.setText(str(fan[0][1]))
        self.name_entry.setStyleSheet("background-color:white")
        self.author_entry = QLineEdit(bottomFrame)
        self.author_entry.setText(str(fan[0][2]))
        self.author_entry.setStyleSheet("background-color:white")

        add_button = QPushButton("Sil", bottomFrame)
        add_button.clicked.connect(self.deleteFan)
        add_button2 = QPushButton("Düzenle", bottomFrame)
        add_button2.clicked.connect(self.UpdateFan)
        bottom_layout.addRow(QLabel("Tarih :"), self.name_entry)
        bottom_layout.addRow(QLabel("Fan Durum :"), self.author_entry)
        bottom_layout.addRow(QLabel(""), add_button)
        bottom_layout.addRow(QLabel(""), add_button2)



        main_layout.addWidget(bottomFrame)
        self.setLayout(main_layout)

    def deleteFan(self):
        global fan_id
        mbox = QMessageBox.question(self,"Uyarı","Fan bilgisini silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cursor.execute("DELETE FROM fandurum WHERE fan_id =?",(fan_id,))
                connection.commit()
                QMessageBox.information(self,"Bilgi","Fan Bilgisi silindi")

            except:
                QMessageBox.information(self,"Bilgi","Fan Bilgisi silinemedi")


    def UpdateFan(self):
        tarih = self.name_entry.text()
        fandurum= self.author_entry.text()
        global fan_id
        if (tarih and fandurum != ""):
            try:
                query = "UPDATE fandurum SET tarih=?,fandurum=? WHERE fan_id=?"
                cursor.execute(query, (tarih, fandurum,fan_id))
                connection.commit()
                QMessageBox.information(self, "Fan Durumu Düzenlendi", "Parça Düzenlendi")

            except:
                QMessageBox.information(self, "Fan Durumu Düzenlenemedi", "Parça Düzenlenemedi")

        else:
            QMessageBox.information(self, "Uyarı!", "Alanlar Boş kalamaz")







def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()














