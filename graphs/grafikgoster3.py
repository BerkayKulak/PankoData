import matplotlib
matplotlib.use("TKAgg")
import sys
# module to save pdf files
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt  # module to plot
import pyqtgraph as pg
import pandas as pd  # module to read csv file


class SaksıNemleri(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(SaksıNemleri, self).__init__(*args, **kwargs)
        self.setGeometry(600, 350, 600, 450)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        filename = "humidity.csv"  # user selected file
        data = pd.read_csv(filename, delimiter=',')

        f1 = plt.figure(figsize=(12, 7))

        ax1 = f1.add_subplot(2, 4, 1)
        ax1.grid(True)
        ax1.plot(data[["nem"]], label='1.Saksı', color="r", marker='^', markevery=10)
        plt.xlabel("1.Saksı-Değeri")
        plt.ylabel("Nem Değeri")

        ax2 = f1.add_subplot(2, 4, 2)
        ax2.grid(True)
        ax2.plot(data[["nem2"]], label='2.Saksı', color="g", marker='^', markevery=10)
        plt.xlabel("2.Saksı-Değeri")


        ax3 = f1.add_subplot(2, 4, 3)
        ax3.grid(True)
        ax3.plot(data[["nem3"]], label='3.Saksı', color="b", marker='^', markevery=10)
        plt.xlabel("3.Saksı-Değeri")


        ax4 = f1.add_subplot(2, 4, 4)
        ax4.grid(True)
        ax4.plot(data[["nem4"]], label='4.Saksı', color="c", marker='^', markevery=10)
        plt.xlabel("4.Saksı-Değeri")


        ax5 = f1.add_subplot(2, 4, 5)
        ax5.grid(True)
        ax5.plot(data[["nem5"]], label='5.Saksı', color="k", marker='^', markevery=10)
        plt.xlabel("5.Saksı-Değeri")
        plt.ylabel("Nem Değeri")

        ax6 = f1.add_subplot(2, 4, 6)
        ax6.grid(True)
        ax6.plot(data[["nem6"]], label='6.Saksı', color="#800080", marker='^', markevery=10)
        plt.xlabel("6.Saksı-Değeri")


        ax7 = f1.add_subplot(2,4,7)
        ax7.grid(True)
        ax7.plot(data[["nem7"]], label='7.Saksı', color="#7CFC00", marker='^', markevery=10)
        plt.xlabel("7.Saksı-Değeri")


        ax8 = f1.add_subplot(2, 4, 8)
        ax8.grid(True)
        ax8.plot(data[["nem8"]], label='8.Saksı', color="#66CDAA", marker='^', markevery=10)
        plt.xlabel("8.Saksı-Değeri")


        plt.show()
        self.graphWidget.plot(kind='line', x="sicaklik", y='tarih', ax=ax1, color='blue')



def ass():
    app = QtWidgets.QApplication(sys.argv)
    ass = SaksıNemleri()
    ass.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ass()




