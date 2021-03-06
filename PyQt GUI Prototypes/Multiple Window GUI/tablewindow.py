from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc
import sys


class Ui_tablewindow(object):
    def setupUi(self, tablewindow):
        # Stores selected table from text file
        self.table = trans_data('shared.txt')
        tablewindow.setObjectName("tablewindow")
        tablewindow.resize(1112, 808)
        self.centralwidget = QtWidgets.QWidget(tablewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QMainWindow{background-color: rgb(170, 255, 255);}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1088, 784))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(470, 10, 172, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(290, 60, 520, 34))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(390, 180, 671, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.attribute1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.attribute1.setGeometry(QtCore.QRect(20, 180, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.attribute1.setFont(font)
        self.attribute1.setObjectName("attribute1")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(160, 180, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.next_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.next_button.setGeometry(QtCore.QRect(280, 610, 93, 28))
        self.next_button.setObjectName("next_button")
        self.prev_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.prev_button.setGeometry(QtCore.QRect(20, 610, 93, 28))
        self.prev_button.setObjectName("prev_button")
        self.display_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.display_button.setGeometry(QtCore.QRect(150, 610, 101, 28))
        self.display_button.setObjectName("display_button")
        self.showdata_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.showdata_button.setGeometry(QtCore.QRect(700, 670, 101, 28))
        self.showdata_button.setObjectName("showdata_button")
        self.showdata_button.clicked.connect(self.load_data)
        self.create_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_button.setGeometry(QtCore.QRect(20, 680, 93, 28))
        self.create_button.setObjectName("create_button")
        self.update_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.update_button.setGeometry(QtCore.QRect(160, 680, 93, 28))
        self.update_button.setObjectName("update_button")
        self.delete_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.delete_button.setGeometry(QtCore.QRect(280, 680, 93, 28))
        self.delete_button.setObjectName("delete_button")
        self.statuslabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.statuslabel.setGeometry(QtCore.QRect(500, 680, 200, 16))
        self.statuslabel.setObjectName("statuslabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        tablewindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(tablewindow)
        QtCore.QMetaObject.connectSlotsByName(tablewindow)

    def retranslateUi(self, tablewindow):
        _translate = QtCore.QCoreApplication.translate
        tablewindow.setWindowTitle(_translate("tablewindow", "MainWindow"))
        self.label.setText(_translate("tablewindow", "Hallywell"))
        self.label_2.setText(_translate("tablewindow", "Customer Relationship Management"))
        self.attribute1.setText(_translate("tablewindow", "Enter attribute:"))
        self.lineEdit.setPlaceholderText(_translate("tablewindow", "Please enter attribute"))
        self.next_button.setText(_translate("tablewindow", "Next"))
        self.prev_button.setText(_translate("tablewindow", "Previous"))
        self.display_button.setText(_translate("tablewindow", "Display Current"))
        self.showdata_button.setText(_translate("tablewindow", "Show ALL Data"))
        self.create_button.setText(_translate("tablewindow", "Create New"))
        self.update_button.setText(_translate("tablewindow", "Update"))
        self.delete_button.setText(_translate("tablewindow", "Delete"))
        self.statuslabel.setText(_translate("tablewindow", "Please Click To Load Data"))

    def load_data(self):
        column_total = 0
        row_total = 0
        table_data = [[item for item in row] for row in
                      (server_connection(f"SELECT * FROM CIS3365_Project.dbo.{self.table}"))]
        table_headers = [[item for item in row] for row in (server_connection(
            ("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='%s'" % self.table)))]
        for i, _ in enumerate(table_data):
            row_total += 1
        for i, _ in enumerate(table_headers):
            column_total += 1
        self.tableWidget.setColumnCount(column_total)
        self.tableWidget.setRowCount(row_total)
        col = 0  # Sets attribute column number
        for row_data in table_headers:
            for data in row_data:
                self.tableWidget.setItem(0, col, QtWidgets.QTableWidgetItem(str(data)))
                col += 1
        for row_number, row_data in enumerate(table_data):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number + 1, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.statuslabel.setText("Data has been loaded successfully")


# Enter your information specific to your local server for now
def server_connection(command):
    conn = pyodbc.connect('Driver={SQL Server};'  # Leave this as is
                          'Server=ENTER SERVER NAME;'  # Enter your local Server Name
                          'Database=ENTER DATABASE NAME;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    cursor = conn.cursor()
    cursor.execute(command)
    return cursor


# Reads selected table from text file
def trans_data(file_name):
    data = open(file_name, 'r')
    choice = data.read()
    return choice


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tablewindow = QtWidgets.QMainWindow()
    ui = Ui_tablewindow()
    ui.setupUi(tablewindow)
    tablewindow.show()
    sys.exit(app.exec())
