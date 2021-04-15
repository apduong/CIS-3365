from loadingscreen import Ui_LoadingScreen
from mainscreen import Ui_MainScreen
from NewProductForm import Ui_NewProductForm
from ProductColorDetail import Ui_ProductColorDetail
from ProductDetailForm import Ui_ProductDetails
from ProductRatingDetail import Ui_ProductRatingDetail
from ProductStatusDetail import Ui_ProductStatusDetail
from ProductTypeDetail import Ui_ProductTypeDetail
from Manufacturer import Ui_Manufacturer
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
        self.timer.start(35)
        self.ui.dropshadowframe.setGraphicsEffect(self.shadow)
        self.ui.label_description.setText("<strong>WELCOME</strong> To Our Customer Relationship Management System")
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.open_mainscreen()
            self.close()
        counter += 1

    def open_mainscreen(self):
        self.ui = MainScreen()
        self.ui.show()
        self.ui.load_forms()


class MainScreen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)
        self.ui.openform_button.clicked.connect(self.open_forms)

    def load_forms(self):
        self.ui.comboBox_form.addItems(["New Product Form", "Product Color Detail"])

    def open_forms(self):
        selected = self.ui.comboBox_form.currentText()
        if selected == "New Product Form":
            self.open_productform()

    def open_productform(self):
        self.form = NewProductForm()
        self.form.show()


class ManufacturerForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Manufacturer()
        self.ui.setupUi(self)


class NewProductForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewProductForm()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    app.exec()
