import matplotlib
matplotlib.use("TKAgg")
import sys
# module to save pdf files
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt  # module to plot
import pyqtgraph as pg
import pandas as pd  # module to read csv file


class HarcananSu(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(HarcananSu, self).__init__(*args, **kwargs)
        self.setGeometry(600, 350, 600, 450)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        filename = "harcanansumiktari.csv"  # user selected file
        data = pd.read_csv(filename, delimiter=',')

        f1 = plt.figure(figsize=(12, 7))

        ax1 = f1.add_subplot(1,1,1)
        ax1.grid(True)
        ax1.plot(data[["mililitre"]], label='Mililitre', color="r", marker='^', markevery=10)
        plt.ylabel("Harcanan Su Mililitresi")
        plt.xlabel("DEĞER")


        plt.show()
        self.graphWidget.plot(kind='line', x="sicaklik", y='tarih', ax=ax1, color='blue')



def ass():
    app = QtWidgets.QApplication(sys.argv)
    ass = HarcananSu()
    ass.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ass()




