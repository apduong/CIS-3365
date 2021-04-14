from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import tablewindow
import pyodbc


class UiMainWindow(object):
    def __init__(self, tables):
        self.table_names = tables
        super(UiMainWindow, self).__init__()
        self.main_window = QtWidgets.QMainWindow()
        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.scrollArea = QtWidgets.QScrollArea(self.central_widget)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.table_listComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.openTable_pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)

    def setup_ui(self):
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(800, 600)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 525))
        self.label_2.setGeometry(QtCore.QRect(100, 50, 520, 34))
        self.label_2.setFont(self.set_font("Arial", 18, 75, True))
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label.setGeometry(QtCore.QRect(280, 0, 172, 45))
        self.label.setFont(self.set_font("Arial", 24, 75, True))
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.label_3.setGeometry(QtCore.QRect(60, 230, 231, 31))
        self.label_3.setFont(self.set_font(None, 14, 75, False))
        self.label_3.setObjectName("label_3")
        self.table_listComboBox.setGeometry(QtCore.QRect(290, 230, 171, 31))
        self.table_listComboBox.setObjectName("table_listComboBox")
        self.table_listComboBox.addItems(self.table_names)
        self.openTable_pushButton.setGeometry(QtCore.QRect(480, 230, 93, 28))
        self.openTable_pushButton.setObjectName("openTable_pushButton")
        self.openTable_pushButton.clicked.connect(self.open_window)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.main_window.setCentralWidget(self.central_widget)
        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)
        self.main_window.show()

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "Hallywell"))
        self.label_2.setText(_translate("MainWindow", "Customer Relationship Management"))
        self.label_3.setText(_translate("MainWindow", "Please Select A Table:"))
        self.label.setText(_translate("MainWindow", "Hallywell"))
        self.openTable_pushButton.setText(_translate("MainWindow", "Open Table"))

    def set_font(self, family, size, weight, bold=True):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        font.setWeight(weight)
        font.setBold(bold)
        return font

    def open_window(self):
        selected_table = self.table_listComboBox.currentText()
        self.ui = tablewindow.UiTableWindow(selected_table)
        self.ui.setup_ui()


# Enter your information specific to your local server for now
def server_connection(command):
    conn = pyodbc.connect('Driver={SQL Server};'  # Leave this as is
                          'Server=LAPTOP-S6PL64NB;'  # Enter your local Server Name
                          'Database=Project_Data;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    cursor = conn.cursor()
    cursor.execute(command)
    return cursor


# Stores all table names from the database
def table_data():
    tables = []
    # Change database name in SQL code as well
    for row in server_connection(
            'SELECT * FROM Project_Data.INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = \'BASE TABLE\''):
        for i, item in enumerate(row):
            if i == 2:
                tables.append(item)
    return tables


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = UiMainWindow(table_data())
    gui.setup_ui()
    sys.exit(app.exec())

