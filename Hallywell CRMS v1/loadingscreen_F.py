from loadingscreen import Ui_LoadingScreen
from mainscreen import Ui_MainScreen
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import *

counter = 0


class LoadingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowFlags.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(70)
        self.ui.dropshadowframe.setGraphicsEffect(self.shadow)
        self.ui.label_description.setText("<strong>WELCOME</strong> To Our Customer Relationship Management System")
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(6000,
                                 lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainScreen()
            self.main.show()
            self.close()
        counter += 1


class MainScreen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    app.exec()
