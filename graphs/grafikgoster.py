
import matplotlib
matplotlib.use("TKAgg")
import sys
# module to save pdf files
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt  # module to plot
import pyqtgraph as pg
import pandas as pd  # module to read csv file


class SicaklikToprakNemGrafigiLinear(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(SicaklikToprakNemGrafigiLinear, self).__init__(*args, **kwargs)
        self.setGeometry(600, 350, 600, 450)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        dataframe = pd.read_csv("temperature.csv", index_col=0)
        dataframe2 = pd.read_csv("humidity.csv", index_col=0)
        f1 = plt.figure(figsize=(12, 7))
        ax = f1.add_subplot(2, 1, 1)
        ax2 = f1.add_subplot(2, 1, 2)

        ax.plot(dataframe.index, dataframe["sicaklik"])
        ax2.plot(dataframe2.index, dataframe2["nem"], color="red")

        plt.show()


        self.graphWidget.plot(kind='line', x="sicaklik", y='tarih', ax=ax, color='blue')



def ass():
    app = QtWidgets.QApplication(sys.argv)
    ass = SicaklikToprakNemGrafigiLinear()
    ass.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ass()






