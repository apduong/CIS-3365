# Form implementation generated from reading ui file 'loadingscreen.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        LoadingScreen.setObjectName("LoadingScreen")
        LoadingScreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(LoadingScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropshadowframe = QtWidgets.QFrame(self.centralwidget)
        self.dropshadowframe.setStyleSheet("QFrame{background-color:#D0DBE8;border-radius:10px;}\n"
"")
        self.dropshadowframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dropshadowframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dropshadowframe.setObjectName("dropshadowframe")
        self.label_title = QtWidgets.QLabel(self.dropshadowframe)
        self.label_title.setGeometry(QtCore.QRect(0, 70, 660, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:#F27E14")
        self.label_title.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.dropshadowframe)
        self.label_description.setGeometry(QtCore.QRect(0, 160, 660, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color:rgb(154, 162, 171)")
        self.label_description.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropshadowframe)
        self.progressBar.setGeometry(QtCore.QRect(60, 270, 541, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(154, 162, 171);\n"
"    color:rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.357727, x2:0.99005, y2:0.341, stop:0 rgba(255, 122, 0, 255), stop:1 rgba(193, 131, 255, 255))\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropshadowframe)
        self.label_loading.setGeometry(QtCore.QRect(0, 300, 660, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color:rgb(154, 162, 171)")
        self.label_loading.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.dropshadowframe)
        self.label_credits.setGeometry(QtCore.QRect(0, 340, 651, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color:rgb(154, 162, 171)")
        self.label_credits.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout.addWidget(self.dropshadowframe)
        LoadingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingScreen)
        QtCore.QMetaObject.connectSlotsByName(LoadingScreen)

    def retranslateUi(self, LoadingScreen):
        _translate = QtCore.QCoreApplication.translate
        LoadingScreen.setWindowTitle(_translate("LoadingScreen", "MainWindow"))
        self.label_title.setText(_translate("LoadingScreen", "<strong>HallyWell</strong> Linen"))
        self.label_description.setText(_translate("LoadingScreen", "<strong>Customer</strong> Relationship Management System"))
        self.label_loading.setText(_translate("LoadingScreen", "loading..."))
        self.label_credits.setText(_translate("LoadingScreen", "<strong>Created:</strong> Vintage Creative Consulting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadingScreen = QtWidgets.QMainWindow()
    ui = Ui_LoadingScreen()
    ui.setupUi(LoadingScreen)
    LoadingScreen.show()
    sys.exit(app.exec())
