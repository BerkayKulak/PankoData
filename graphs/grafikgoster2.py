import matplotlib
matplotlib.use("TKAgg")
import sys
# module to save pdf files
from matplotlib.backends.backend_pdf import PdfPages  
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt  # module to plot
import pyqtgraph as pg
import pandas as pd  # module to read csv file


class SıcaklıkC1C2C3C4(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):

        super(SıcaklıkC1C2C3C4, self).__init__(*args, **kwargs)
        self.setGeometry(600, 350, 600, 450)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        filename = "temperature.csv"  # user selected file
        data = pd.read_csv(filename, delimiter=',')

        f1 = plt.figure(figsize=(12, 7))

        ax1 = f1.add_subplot(2, 2, 1)
        ax1.grid(True)
        ax1.plot(data[["sicaklik"]], label='Cº-1-SAĞ', color="r", marker='^', markevery=10)
        plt.ylabel("Cº-ÖN-SOL")
        plt.xlabel("DEĞER")

        ax2 = f1.add_subplot(2, 2, 2)
        ax2.grid(True)
        ax2.plot(data[["sicaklik2"]], label='Cº-2-SAĞ', color="g", marker='^', markevery=10)
        plt.ylabel("Cº-ÖN-SAĞ")
        plt.xlabel("DEĞER")

        ax3 = f1.add_subplot(2, 2, 3)
        ax3.grid(True)
        ax3.plot(data[["sicaklik3"]], label='Cº-3-SAĞ', color="b", marker='^', markevery=10)
        plt.ylabel("Cº-ARKA-SOL")
        plt.xlabel("DEĞER")

        ax4 = f1.add_subplot(2, 2, 4)
        ax4.grid(True)
        ax4.plot(data[["sicaklik4"]], label='Cº-4-SAĞ', color="#800080", marker='^', markevery=10)
        plt.ylabel("Cº-ARKA-SAĞ")
        plt.xlabel("DEĞER")


        plt.show()
        self.graphWidget.plot(kind='line', x="sicaklik", y='tarih', ax=ax1, color='blue')



def ass():
    app = QtWidgets.QApplication(sys.argv)
    ass = SıcaklıkC1C2C3C4()
    ass.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ass()




