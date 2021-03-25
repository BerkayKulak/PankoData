import matplotlib
matplotlib.use("TKAgg")
import sys
# module to save pdf files
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt  # module to plot
import pyqtgraph as pg
import pandas as pd  # module to read csv file


class HavaKalitesi(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(HavaKalitesi, self).__init__(*args, **kwargs)
        self.setGeometry(600, 350, 600, 450)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        filename = "carbondioksitmiktari1.csv"  # user selected file
        data = pd.read_csv(filename, delimiter=',')

        f1 = plt.figure(figsize=(12, 7))

        ax1 = f1.add_subplot(1,1,1)
        ax1.grid(True)
        ax1.plot(data[["carbondioksit_alma_miktari"]], label='lux', color="r", marker='^', markevery=10)
        plt.ylabel("Lux")
        plt.xlabel("DEĞER")


        plt.show()
        self.graphWidget.plot(kind='line', x="sicaklik", y='tarih', ax=ax1, color='blue')



def ass():
    app = QtWidgets.QApplication(sys.argv)
    ass = HavaKalitesi()
    ass.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ass()




