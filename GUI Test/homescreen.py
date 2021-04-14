from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import resources as src
import tablescreen


class UiMainWindow(object):
    def __init__(self, tables):
        self.table_names = tables
        super(UiMainWindow, self).__init__()
        self.main_window = QtWidgets.QMainWindow()
        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.scrollArea = QtWidgets.QScrollArea(self.central_widget)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.label = QtWidgets.QLabel(self.frame)
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.Table_List = QtWidgets.QComboBox(self.frame_2)
        self.open_table_button = QtWidgets.QPushButton(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.label_4 = QtWidgets.QLabel(self.frame_3)

    def setup_ui(self):
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(974, 497)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Rectangle 1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.main_window.setWindowIcon(icon)
        self.main_window.setStyleSheet("QMainWindow{background-color:#D0DBE8;}\n" 
                                       "QScrollArea { background: transparent; }\n"
                                       "QScrollArea > QWidget > QWidget { background: transparent; }\n"
                                       "QScrollArea > QWidget > QScrollBar { background: palette(base);}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 952, 424))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label.setMaximumSize(QtCore.QSize(500, 200))
        self.label.setPixmap(QtGui.QPixmap('images/Hallywell-White Vector.png'))
        self.label.setScaledContents(True)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(5)
        self.frame_2.setMidLineWidth(2)
        self.horizontalLayout_2.setContentsMargins(0, -1, 54, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.label_2.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{color: qlineargradient(spread:pad, x1:0.909811, y1:0.483, x2:0.05, "
                                   "y2:0.170455, stop:0 rgba(143, 160, 201, 255), stop:1 rgba(255, 255, 255, 255)); "
                                   "; font-weight: bold;}\n""")
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_2.setLineWidth(5)
        self.label_2.setMidLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{color:rgba(242, 126, 20, 1);}")
        self.label_3.setAlignment(QtCore.Qt.Alignment.AlignRight)
        self.label_3.setAlignment(QtCore.Qt.Alignment.AlignTrailing)
        self.label_3.setAlignment(QtCore.Qt.Alignment.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_List.sizePolicy().hasHeightForWidth())
        self.Table_List.setSizePolicy(sizePolicy)
        self.Table_List.setMaximumSize(QtCore.QSize(150, 30))
        self.Table_List.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Table_List.setStyleSheet("QComboBox{background-color: transparent; border: 2px solid black;}")
        self.Table_List.setObjectName("Table_List")
        self.Table_List.addItems(self.table_names)
        self.horizontalLayout_2.addWidget(self.Table_List)
        self.open_table_button.setMaximumSize(QtCore.QSize(100, 30))
        self.open_table_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.open_table_button.setStyleSheet(
            "QPushButton{color:rgba(242, 126, 20, 1); background-color:rgba(143, 160, 201, 90); "
            "font-weight:bold; border: 1px solid black; border-radius: 10px;}")
        self.open_table_button.setObjectName("open_table_button")
        self.open_table_button.clicked.connect(self.open_window)
        self.horizontalLayout_2.addWidget(self.open_table_button)
        self.verticalLayout_2.addWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.verticalLayout_3.setContentsMargins(0, 0, 800, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4.setMaximumSize(QtCore.QSize(100, 60))
        self.label_4.setStyleSheet("QLabel{border-radius: 90px;}")
        self.label_4.setPixmap(QtGui.QPixmap("images/VintageCreativeConsulting-Vector.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.main_window.setCentralWidget(self.central_widget)
        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)
        self.main_window.show()

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "Hallywell CRMS"))
        self.label_2.setText(_translate("MainWindow", "Customer Relationship \n"
                                                      "Management System"))
        self.label_3.setText(_translate("MainWindow", "Choose Table:"))
        self.open_table_button.setText(_translate("MainWindow", "Open Table"))

    def open_window(self):
        selected_table = self.Table_List.currentText()
        self.ui = tablescreen.UiTableWindow(selected_table)
        self.ui.setup_ui()


def get_table_names():
    table_names = []
    cursor = src.server_connection().cursor()
    data = cursor.execute('SELECT * FROM Project_Data.INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = \'BASE TABLE\'')
    for row in data:
        for i, name in enumerate(row):
            if i == 2:
                table_names.append(name)
    return table_names


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = UiMainWindow(get_table_names())
    gui.setup_ui()
    sys.exit(app.exec())
