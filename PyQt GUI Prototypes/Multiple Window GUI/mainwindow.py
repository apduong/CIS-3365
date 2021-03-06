from PyQt6 import QtCore, QtGui, QtWidgets
import tablewindow
import sys
import pyodbc
import time


class Ui_MainWindow(object):
    # Opens the window with the table data when called
    def openWindow(self):
        time.sleep(3)
        self.window = QtWidgets.QMainWindow()
        self.ui = tablewindow.Ui_tablewindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 525))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 520, 34))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(280, 0, 172, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.table_listcomboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.table_listcomboBox.setGeometry(QtCore.QRect(290, 230, 171, 31))
        self.table_listcomboBox.setObjectName("table_listcomboBox")
        # Adds list of table names to drop down menu
        names = self.drop_values(self)
        self.table_listcomboBox.addItems(names)
        self.opentable_pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.opentable_pushButton.setGeometry(QtCore.QRect(480, 230, 93, 28))
        self.opentable_pushButton.setObjectName("opentable_pushButton")
        self.opentable_pushButton.clicked.connect(self.table_selected)
        self.opentable_pushButton.clicked.connect(self.openWindow)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Customer Relationship Management"))
        self.label.setText(_translate("MainWindow", "Hallywell"))
        self.label_3.setText(_translate("MainWindow", "Please Select A Table:"))
        self.opentable_pushButton.setText(_translate("MainWindow", "Open Table"))

    @staticmethod
    # Gets the table names from the SQL Database
    def drop_values(self):
        tables = []
        for row in server_connection(
                'SELECT * FROM CIS3365_Project.INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = \'BASE TABLE\''):
            for i, item in enumerate(row):
                if i == 2:
                    tables.append(item)
        return tables

    # Checks the table selected by the user and outputs it to a txt file called shared.txt
    def table_selected(self):
        shared = self.table_listcomboBox.currentText()
        file = open("shared.txt", "w")
        file.write(shared)
        file.close()

# Enter your information specific to your local server for now
def server_connection(command):
    conn = pyodbc.connect('Driver={SQL Server};'  # Leave this as is
                          'Server=ENTER SERVER NAME;'  # Enter your local Server Name
                          'Database=ENTER DATABASE NAME;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    cursor = conn.cursor()
    cursor.execute(command)
    return cursor


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
