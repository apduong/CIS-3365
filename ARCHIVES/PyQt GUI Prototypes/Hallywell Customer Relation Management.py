from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
import sys

# FIXME: Figure out the best way to integrate the CRUD functions
# FIXME: Learn what most of the lines of code do so we can better manipulate it
# FIXME: Restructure code for more readability and less warnings


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 0, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 80, 801, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 180, 1000, 571))
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 760, 93, 28))
        self.pushButton.setObjectName("pushButton")
        # Connects load data button to function
        self.pushButton.clicked.connect(self.onclick)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(750, 760, 181, 20))
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 26))
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
        self.label.setText(_translate("MainWindow", "Hallywell "))
        self.label_2.setText(_translate("MainWindow", "Customer Relationship Management System"))
        self.pushButton.setText(_translate("MainWindow", "Load Data"))
        self.label_3.setText(_translate("MainWindow", "Data has not been loaded"))

    # Gets data from SQL Server and displays it onto the GUI when load data is pressed
    # NB. Before running code make sure the enter the missing data such as table and database names
    def onclick(self):
        table_data = [[item for item in row] for row in server_connection('SELECT * FROM CIS3365_Project.dbo.Orders')]
        table_headers = [[item for item in row] for row in server_connection('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = \'Orders\'')]
        col = 0
        for row_data in table_headers:
            for data in row_data:
                self.tableWidget.setItem(0, col, QtWidgets.QTableWidgetItem(str(data)))
                col += 1
        for row_number, row_data in enumerate(table_data):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number+1, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.label_3.setText("Data has been loaded successfully")

# Connects GUI to SQL Server
# NB. Before running code make sure the enter the missing data such as database and server names
def server_connection(command):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-S6PL64NB;'
                          'Database=CIS3365_Project;'
                          'Trusted_Connection=yes;')
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
