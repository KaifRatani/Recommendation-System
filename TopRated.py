import os
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUiType
import pandas as pd


#scriptDir = dirname(realpath(__file__))
From_Main, _ = loadUiType(join(dirname(__file__), "Main.ui"))

class MainWindow2(QWidget, From_Main):
    def __init__(self):
        super(MainWindow2, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)

        self.txt_display.setText("Top Rated Movie  ")
        self.BtnDescribe.clicked.connect(self.dataHead)
        self.all_data = pd.read_csv('toprated.csv')

    def dataHead(self):
        numColomn = self.spinBox.value()
        if numColomn == 0:
            NumRows = len(self.all_data.index)
        else:
            NumRows = numColomn
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(NumRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sheet = MainWindow2()
    sheet.show()
    sys.exit(app.exec_())