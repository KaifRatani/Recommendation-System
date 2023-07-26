import sys
from PyQt5 import QtCore, QtWidgets as qtw
from itertools import chain
import csv
import traceback
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
from PyQt5.uic import loadUiType
from os.path import dirname, realpath, join

From_Main, _ = loadUiType(join(dirname(__file__), "Main.ui"))


class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)


class Worker(QtCore.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../../../Downloads/icons8-search-account-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(30, 20, 691, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.MainLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.MainLabel.setFont(font)
        self.MainLabel.setAutoFillBackground(False)
        self.MainLabel.setStyleSheet("background-color: rgb(0, 255, 255);\n""")
        self.MainLabel.setTextFormat(QtCore.Qt.RichText)
        self.MainLabel.setScaledContents(False)
        self.MainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabel.setWordWrap(True)
        self.MainLabel.setObjectName("MainLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 150, 331, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        self.txtmovie = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txtmovie.setClearButtonEnabled(True)
        self.txtmovie.setObjectName("txtmovie")


        path = r"movie_title.csv"
        with open(path, "r") as f:
            self.data = list(chain.from_iterable(csv.reader(f)))

        self.data.sort()
        self.threadpool = QtCore.QThreadPool()
        # can't have completer on another thread
        # self.worker_fn(self.create_completer)
        self.create_completer()


        self.horizontalLayout.addWidget(self.txtmovie)
        self.btn_movie = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_movie.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.btn_movie.setIcon(icon)
        self.btn_movie.setCheckable(False)
        self.btn_movie.setObjectName("btn_movie")
        self.btn_movie.clicked.connect(lambda : self.searchmov())


        self.horizontalLayout.addWidget(self.btn_movie)
        self.SearchLebal = QtWidgets.QLabel(self.centralwidget)
        self.SearchLebal.setGeometry(QtCore.QRect(30, 99, 331, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.SearchLebal.setFont(font)
        self.SearchLebal.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.SearchLebal.setAlignment(QtCore.Qt.AlignCenter)
        self.SearchLebal.setObjectName("SearchLebal")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(390, 150, 331, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.txtgenre = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.txtgenre.setClearButtonEnabled(True)
        self.txtgenre.setObjectName("txtgenre")
        self.horizontalLayout_2.addWidget(self.txtgenre)
        self.btn_genre = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_genre.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.btn_genre.setIcon(icon)
        self.btn_genre.setCheckable(False)
        self.btn_genre.setObjectName("btn_genre")
        self.btn_genre.clicked.connect(lambda : self.genremov() )

        path1 = r"genre_name.csv"
        with open(path1, "r") as f:
            self.data1 = list(chain.from_iterable(csv.reader(f)))

        self.data1.sort()
        self.threadpool = QtCore.QThreadPool()
        # can't have completer on another thread
        # self.worker_fn(self.create_completer)
        self.create_completer1()

        self.horizontalLayout_2.addWidget(self.btn_genre)
        self.GenreLabel = QtWidgets.QLabel(self.centralwidget)
        self.GenreLabel.setGeometry(QtCore.QRect(390, 100, 331, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.GenreLabel.setFont(font)
        self.GenreLabel.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.GenreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GenreLabel.setObjectName("GenreLabel")
        self.btn_tr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tr.setGeometry(QtCore.QRect(280, 370, 201, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)


        self.btn_tr.setFont(font)
        self.btn_tr.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.btn_tr.setObjectName("btn_tr")
        self.btn_tr.clicked.connect(lambda : self.tp())


        self.btn_recommend = QtWidgets.QPushButton(self.centralwidget)
        self.btn_recommend.setGeometry(QtCore.QRect(230, 290, 291, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_recommend.setFont(font)
        self.btn_recommend.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.btn_recommend.setObjectName("btn_recommend")
        self.btn_recommend.clicked.connect(lambda : self.movie_recommend())


        self.btn_analysis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analysis.setGeometry(QtCore.QRect(310, 460, 151, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_analysis.setFont(font)
        self.btn_analysis.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.btn_analysis.setObjectName("btn_analysis")
        self.btn_analysis.clicked.connect(lambda : self.Analysis())


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def worker_fn(self, fn):
        worker = Worker(fn)
        self.threadpool.start(worker)

    def create_completer(self):
        completer = qtw.QCompleter(self.data)
        # case sensitive by default
        completer.setModelSorting(qtw.QCompleter.CaseSensitivelySortedModel)
        self.txtmovie.setCompleter(completer)

    def create_completer1(self):
        completer = qtw.QCompleter(self.data1)
        # case sensitive by default
        completer.setModelSorting(qtw.QCompleter.CaseSensitivelySortedModel)
        self.txtgenre.setCompleter(completer)

    def searchmov(self):
        moviename = self.txtmovie.text()
        print(moviename)

    def genremov(self):
        genre = self.txtgenre.text()
        print(genre)

    def tp(self):
        print('tp')


    def movie_recommend(self):
        print('Recommend MOvies')

    def Analysis(self):
        print('analysis Page')



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MRS"))
        self.MainLabel.setText(_translate("MainWindow", "MOVIE RECOMMENDATION SYSTEM"))
        self.txtmovie.setText(_translate("MainWindow", "Enter Movie Name"))
        self.btn_movie.setText(_translate("MainWindow", "Search"))
        self.SearchLebal.setText(_translate("MainWindow", "Enter Movie Name To Recommend"))
        self.txtgenre.setText(_translate("MainWindow", "Enter Genre To Go"))
        self.btn_genre.setText(_translate("MainWindow", "Search"))
        self.GenreLabel.setText(_translate("MainWindow", "Enter Genre To Recommend"))
        self.btn_tr.setText(_translate("MainWindow", "Click to Get Top Rated Movies"))
        self.btn_recommend.setText(_translate("MainWindow", "Click to Get Recommend Movie For You "))
        self.btn_analysis.setText(_translate("MainWindow", "Get Analysis Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
