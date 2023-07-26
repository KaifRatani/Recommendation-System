import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from MRS import Ui_MainWindow
import pyrebase


firebaseConfig = {
    'apiKey': "AIzaSyBah54QKkjsbvH2FXsxg0m4_q50QgAGJI0",
    'authDomain': "kaifdata.firebaseapp.com",
    'databaseURL': "https://kaifdata-default-rtdb.firebaseio.com",
    'projectId': "kaifdata",
    'storageBucket': "kaifdata.appspot.com",
    'messagingSenderId': "8466814502",
    'appId': "1:8466814502:web:95ea77be671e79ffda38e7",
    'measurementId': "G-YCZDBS4KM8"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
st = firebase.storage()


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("ui\login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.txt_in.setVisible(False)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        try:
            auth.sign_in_with_email_and_password(email,password)
            self.Win = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.Win)
            self.Win.show()
        except:
            self.txt_in.setVisible(True)
            print("invalid Email Or Password")


    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("ui\createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.btn_back.clicked.connect(self.back)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.invalid.setVisible(False)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            try:
                auth.create_user_with_email_and_password(email,password)
                self.back()

            except:

                self.invalid.setVisible(True)
                print("invailed")


    def back(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)



if __name__ == '__main__':

    app=QApplication(sys.argv)
    mainwindow=Login()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(480)
    widget.setFixedHeight(620)
    widget.show()
    app.exec_()
