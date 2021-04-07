from PyQt6 import QtCore, QtGui, QtWidgets
import resources as src

# Ensure that you fill out the necessary information in the resources file
# and your local database name in some SQL codes


class UiTableWindow(object):
    def __init__(self, table):
        self.selected_table = table
        self.table_attributes = self.retrieve_data()
        super(UiTableWindow, self).__init__()
        self.table_window = QtWidgets.QMainWindow()
        self.central_widget = QtWidgets.QWidget(self.table_window)
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.scrollArea = QtWidgets.QScrollArea(self.central_widget)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label = QtWidgets.QLabel(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.Search_Button = QtWidgets.QPushButton(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_3)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.label_names, self.lineEdit_names = [], []
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.add_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.update_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.del_pushButton = QtWidgets.QPushButton(self.frame_4)

    def setup_ui(self):
        self.table_window.setObjectName("TableWindow")
        self.table_window.resize(1026, 598)
        self.table_window.setStyleSheet("QMainWindow{background-color:#D0DBE8;}\n"
                                        "QScrollArea { background: transparent; }\n"
                                        "QScrollArea > QWidget > QWidget { background: transparent; }\n"
                                        "QScrollArea > QWidget > QScrollBar { background: palette(base); }")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1004, 525))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_2.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{color: qlineargradient(spread:pad, x1:0.909811, "
                                   "y1:0.483, x2:0.05, y2:0.170455, stop:0 rgba(143, 160, 201, 255), "
                                   "stop:1 rgba(255, 255, 255, 255)); ; font-weight: bold;}\n""")
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_2.setLineWidth(5)
        self.label_2.setMidLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.horizontalLayout.addWidget(self.label_2)
        self.label.setMaximumSize(QtCore.QSize(500, 200))
        self.label.setPixmap(QtGui.QPixmap("images/Hallywell-White Vector.png"))
        self.label.setScaledContents(True)
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 700, -1)
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{color: qlineargradient(spread:pad, x1:0.909811, "
                                   "y1:0.483, x2:0.05, y2:0.170455, stop:0 rgba(143, 160, 201, 255), "
                                   "stop:1 rgba(255, 255, 255, 255)); ; font-weight: bold;}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.Search_Button.setMinimumSize(QtCore.QSize(60, 0))
        self.Search_Button.setMaximumSize(QtCore.QSize(60, 20))
        self.Search_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Search_Button.setStyleSheet(
            "QPushButton{color:rgba(242, 126, 20, 1); background-color:rgba(143, 160, 201, 90); font-weight:bold; "
            "border: 1px solid black; border-radius: 10px;}")
        self.horizontalLayout_2.addWidget(self.Search_Button)
        self.Search_Button.clicked.connect(self.current_data)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 476, 134))
        self.create_fields()
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.add_pushButton.setMinimumSize(QtCore.QSize(10, 30))
        self.add_pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_pushButton.setStyleSheet("QPushButton{color:rgba(242, 126, 20, 1); "
                                          "background-color:rgba(143, 160, 201, 90); font-weight:bold; "
                                          "border: 1px solid black; border-radius: 10px;}")
        self.add_pushButton.setObjectName("add_pushButton")
        self.horizontalLayout_3.addWidget(self.add_pushButton)
        self.update_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.update_pushButton.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.update_pushButton.setFont(font)
        self.update_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.update_pushButton.setStyleSheet("QPushButton{color:rgba(242, 126, 20, 1); "
                                             "background-color:rgba(143, 160, 201, 90); font-weight:bold; "
                                             "border: 1px solid black; border-radius: 10px;}")
        self.update_pushButton.setObjectName("update_pushButton")
        self.horizontalLayout_3.addWidget(self.update_pushButton)
        self.del_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.del_pushButton.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.del_pushButton.setFont(font)
        self.del_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.del_pushButton.setStyleSheet("QPushButton{color:rgba(242, 126, 20, 1); "
                                          "background-color:rgba(143, 160, 201, 90); font-weight:bold; "
                                          "border: 1px solid black; border-radius: 10px;}")
        self.del_pushButton.setObjectName("del_pushButton")
        self.horizontalLayout_3.addWidget(self.del_pushButton)
        self.verticalLayout.addWidget(self.frame_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.table_window.setCentralWidget(self.central_widget)
        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.table_window)
        self.display_data()
        self.table_window.show()

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.table_window.setWindowTitle(_translate("TableWindow", f"{self.selected_table} Table Data"))
        self.label_2.setText(_translate("TableWindow", "Customer Relationship \n"
                                                       "Management System"))
        self.label_3.setText(_translate("TableWindow", f"Enter {self.table_attributes[0][0]}:"))
        self.Search_Button.setText(_translate("TableWindow", "Search"))
        for i, name in enumerate(self.label_names):
            name.setText(_translate("TableWindow", f"Enter {self.table_attributes[0][i]}"))
        for i, name in enumerate(self.lineEdit_names):
            name.setPlaceholderText(_translate("TableWindow", f"Enter {self.table_attributes[0][i]}"))
        self.add_pushButton.setText(_translate("TableWindow", "Add Record"))
        self.update_pushButton.setText(_translate("TableWindow", "Update Record"))
        self.del_pushButton.setText(_translate("TableWindow", "Delete Record"))

    # This method dynamically creates the required labels and text boxes needed for each table
    def create_fields(self):
        for i in range(self.table_attributes[2]):
            attribute = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
            font = QtGui.QFont()
            font.setPointSize(13)
            font.setBold(True)
            font.setWeight(75)
            attribute.setFont(font)
            attribute.setStyleSheet("QLabel{color: qlineargradient(spread:pad, x1:0.909811, y1:0.483, "
                                    "x2:0.05, y2:0.170455, stop:0 rgba(143, 160, 201, 255), "
                                    "stop:1 rgba(255, 255, 255, 255)); ; font-weight: bold;}")
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.ItemRole.LabelRole, attribute)
            self.label_names.append(attribute)
            line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
            line_edit.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(12)
            line_edit.setFont(font)
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.ItemRole.FieldRole, line_edit)
            self.lineEdit_names.append(line_edit)

    # This method retrieves table data and table attributes from SQL Sever
    def retrieve_data(self):
        table_attributes = []
        column_total = 0
        cursor = src.server_connection().cursor()
        data = cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='%s'" %
                              self.selected_table)
        for row in data:
            for i, name in enumerate(row):
                table_attributes.append(name.replace("_", " ").title())
                column_total += 1
        cursor = src.server_connection().cursor()
        data = cursor.execute(f"SELECT * FROM Project_Data.dbo.{self.selected_table}")
        table_data = [[item for item in row] for row in data]
        return table_attributes, table_data, column_total

    # This method displays the data onto the QTableWidget
    def display_data(self):
        column_total = 0
        row_total = 1  # This takes into consideration the row for the attributes
        # Change database name in SQL code here as well
        data = self.retrieve_data()
        records = data[1]
        attributes = data[0]
        for i, _ in enumerate(records):
            row_total += 1
        for i, _ in enumerate(attributes):
            column_total += 1
        self.tableWidget.setColumnCount(column_total)
        self.tableWidget.setRowCount(row_total)
        col = 0  # Sets attribute column number
        for data in attributes:
            self.tableWidget.setItem(0, col, QtWidgets.QTableWidgetItem(str(data)))
            col += 1
        for row_number, row_data in enumerate(records):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number + 1, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def current_data(self):
        row_ID = int((self.lineEdit.text()))
        table_data = self.retrieve_data()
        row_data = table_data[1]
        for i, data in enumerate(row_data):
            if row_data[i][0] == row_ID:
                for x, names in enumerate(self.lineEdit_names):
                    names.setText(str(row_data[i][x]))
