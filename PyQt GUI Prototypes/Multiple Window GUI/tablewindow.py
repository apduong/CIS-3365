from PyQt6 import QtCore, QtGui, QtWidgets
import pyodbc


class UiTableWindow(object):
    def __init__(self, table):
        self.selected_table = table
        self.table_attributes = self.create_attributes()
        super(UiTableWindow, self).__init__()
        self.table_window = QtWidgets.QMainWindow()
        self.central_widget = QtWidgets.QWidget(self.table_window)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.scrollArea = QtWidgets.QScrollArea(self.central_widget)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.label_names, self.lineEdit_names = [], []
        self.ID_Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ID_Input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.dimension_label = QtCore.QRect(20, 180, 200, 20)
        self.dimension_input = QtCore.QRect(230, 180, 151, 21)
        self.next_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.prev_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.display_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.showdata_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.update_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.delete_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.statuslabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)

    def setup_ui(self):
        self.table_window.setObjectName("TableWindow")
        self.table_window.resize(1024, 768)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1088, 784))
        self.label.setGeometry(QtCore.QRect(470, 10, 172, 45))
        self.label.setFont(self.set_font("Arial", 24, 75, True))
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(290, 60, 520, 34))
        self.label_2.setFont(self.set_font("Arial", 18, 75, True))
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget.setGeometry(QtCore.QRect(390, 180, 671, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.create()
        self.ID_Label.setGeometry(QtCore.QRect(10, 80, 100, 20))
        self.ID_Label.setObjectName("ID_Label")
        self.ID_Input.setGeometry(QtCore.QRect(80, 80, 100, 20))
        self.ID_Input.setObjectName("ID_Input")
        self.next_button.setGeometry(QtCore.QRect(280, 610, 93, 28))
        self.next_button.setObjectName("next_button")
        self.prev_button.setGeometry(QtCore.QRect(20, 610, 93, 28))
        self.prev_button.setObjectName("prev_button")
        self.display_button.setGeometry(QtCore.QRect(150, 610, 101, 28))
        self.display_button.setObjectName("display_button")
        self.display_button.clicked.connect(self.scroll_rows)
        self.showdata_button.setGeometry(QtCore.QRect(700, 670, 101, 28))
        self.showdata_button.setObjectName("showdata_button")
        self.showdata_button.clicked.connect(self.show_data)
        self.create_button.setGeometry(QtCore.QRect(20, 680, 93, 28))
        self.create_button.setObjectName("create_button")
        self.update_button.setGeometry(QtCore.QRect(160, 680, 93, 28))
        self.update_button.setObjectName("update_button")
        self.update_button.clicked.connect(self.update)
        self.delete_button.setGeometry(QtCore.QRect(280, 680, 93, 28))
        self.delete_button.setObjectName("delete_button")
        self.statuslabel.setGeometry(QtCore.QRect(500, 680, 200, 16))
        self.statuslabel.setObjectName("statuslabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.table_window.setCentralWidget(self.scrollArea)
        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.table_window)
        self.table_window.show()

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.table_window.setWindowTitle(_translate("TableWindow", f"{self.selected_table} Table Data"))
        self.label.setText(_translate("TableWindow", "Hallywell"))
        self.label_2.setText(_translate("TableWindow", "Customer Relationship Management"))
        self.ID_Label.setText(_translate("TableWindow", f"{self.selected_table} ID:"))
        for i, name in enumerate(self.label_names):
            name.setText(_translate("TableWindow", f"Enter {self.table_attributes[1][i][0]}:"))
        for name in self.lineEdit_names:
            name.setPlaceholderText(_translate("TableWindow", "Please enter attribute"))
        self.next_button.setText(_translate("TableWindow", "Next"))
        self.prev_button.setText(_translate("TableWindow", "Previous"))
        self.display_button.setText(_translate("TableWindow", "Display Current"))
        self.showdata_button.setText(_translate("TableWindow", "Show ALL Data"))
        self.create_button.setText(_translate("TableWindow", "Create New"))
        self.update_button.setText(_translate("TableWindow", "Update"))
        self.delete_button.setText(_translate("TableWindow", "Delete"))
        self.statuslabel.setText(_translate("TableWindow", "Please Click To Load Data"))

    # Create the correct amount of input and labels depending on the amount of attributes
    def create(self):
        for i in range(self.table_attributes[0]):
            attribute = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            attribute.setGeometry(self.dimension_label)
            font = QtGui.QFont()
            font.setPointSize(10)
            attribute.setFont(font)
            self.dimension_label.translate(0, 40)
            self.label_names.append(attribute)
            line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            line_edit.setGeometry(self.dimension_input)
            self.dimension_input.translate(0, 40)
            self.lineEdit_names.append(line_edit)

    def show_data(self):
        column_total = 0
        row_total = 1  # This takes into consideration the row for the attributes
        # Change database name in SQL code here as well
        data = self.load_data()
        records = data[0]
        headers = data[1]
        for i, _ in enumerate(records):
            row_total += 1
        for i, _ in enumerate(headers):
            column_total += 1
        self.tableWidget.setColumnCount(column_total)
        self.tableWidget.setRowCount(row_total)
        col = 0  # Sets attribute column number
        for row_data in headers:
            for data in row_data:
                self.tableWidget.setItem(0, col, QtWidgets.QTableWidgetItem(str(data)))
                col += 1
        for row_number, row_data in enumerate(records):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number + 1, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.statuslabel.setText("Data has been loaded successfully")

    def load_data(self):
        table_data = [[item for item in row] for row in
                      (server_connection(f"SELECT * FROM Project_Data.dbo.{self.selected_table}"))]
        table_headers = [[item for item in row] for row in (server_connection(
            ("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='%s'" % self.selected_table)))]
        print(table_data)
        return table_data, table_headers

    def scroll_rows(self):
        row_ID = int((self.ID_Input.text()))
        table_data = self.load_data()
        row_data = table_data[0]
        for i, data in enumerate(row_data):
            if row_data[i][0] == row_ID:
                for x, names in enumerate(self.lineEdit_names):
                    names.setText(str(row_data[i][x]))

    def update(self):
        row_ID = int((self.ID_Input.text()))
        table_data = self.load_data()
        headers = table_data[1]
        edits = []
        conn = pyodbc.connect('Driver={SQL Server};'  # Leave this as is
                              'Server=LAPTOP-S6PL64NB;'  # Enter your local Server Name
                              'Database=Project_Data;'  # Enter your Database Name
                              'Trusted_Connection=yes;')  # Leave this as is
        cursor = conn.cursor()
        for x, names in enumerate(self.lineEdit_names):
            edits.append(names.text())
        print(edits)
        for i, data in enumerate(edits):
            cursor.execute(f"UPDATE {self.selected_table} SET ? = ? WHERE ? = ?", headers[i][0], edits[i], headers[0][0], row_ID)


    def set_font(self, family, size, weight, bold=True):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        font.setWeight(weight)
        font.setBold(bold)
        return font

    # Returns the amount of attributes and attribute names from a table
    def create_attributes(self):
        column_total = 0
        table_headers = [[item for item in row] for row in (server_connection(
            ("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='%s'" % self.selected_table)))]
        for i, _ in enumerate(table_headers):
            column_total += 1
        return column_total, table_headers


# Enter your information specific to your local server for now
def server_connection(command):
    conn = pyodbc.connect('Driver={SQL Server};'  # Leave this as is
                          'Server=LAPTOP-S6PL64NB;'  # Enter your local Server Name
                          'Database=Project_Data;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    cursor = conn.cursor()
    cursor.execute(command)
    return cursor
