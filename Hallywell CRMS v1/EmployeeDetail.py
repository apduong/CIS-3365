# Form implementation generated from reading ui file 'EmployeeDetail.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EmployeeStatus(object):
    def setupUi(self, EmployeeStatus):
        EmployeeStatus.setObjectName("EmployeeStatus")
        EmployeeStatus.resize(824, 500)
        EmployeeStatus.setStyleSheet("background-color:#D0DBE8")
        self.centralwidget = QtWidgets.QWidget(EmployeeStatus)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QFrame#frame_2{background-color:white; border-radius: 10px; border: 2px solid #6A7AA6;}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 806, 482))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(300, 50))
        self.label_2.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#6A7AA6")
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setMinimumSize(QtCore.QSize(440, 185))
        self.label_title.setMaximumSize(QtCore.QSize(440, 185))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:#FF800C")
        self.label_title.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_title.setWordWrap(True)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setStyleSheet("QFrame{background-color:white;}\n"
"QComboBox{background-color:white;}\n"
"QComboBox QAbstractItemView{background-color:#F17300; color:white;}\n"
"QLabel{color:white;background-color:#F17300; border: solid white; border-radius: 0;}\n"
"QPushButton{color:#F27E14; border:2px solid #F17300; border-radius: 10px;padding:2px;background-color:white;}\n"
"QPushButton::hover{border:2px solid white; background-color:#F27E14; color:white;}\n"
"QLineEdit{background-color:white; border: 1px solid black; border-radius: 5px;}\n"
"QLineEdit::hover{border-radius: 0;}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(389, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(210, 30))
        self.label.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.frame_3)
        self.addButton.setMinimumSize(QtCore.QSize(210, 30))
        self.addButton.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 5, 0, 1, 1)
        self.lineEdit_EnterNewStatus = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_EnterNewStatus.setMinimumSize(QtCore.QSize(210, 25))
        self.lineEdit_EnterNewStatus.setMaximumSize(QtCore.QSize(210, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.lineEdit_EnterNewStatus.setFont(font)
        self.lineEdit_EnterNewStatus.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.lineEdit_EnterNewStatus.setText("")
        self.lineEdit_EnterNewStatus.setMaxLength(20)
        self.lineEdit_EnterNewStatus.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_EnterNewStatus.setObjectName("lineEdit_EnterNewStatus")
        self.gridLayout.addWidget(self.lineEdit_EnterNewStatus, 3, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(30, 20))
        self.label_3.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:white; color:#FF800C;")
        self.label_3.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(471, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setHorizontalSpacing(40)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMinimumSize(QtCore.QSize(210, 30))
        self.label_5.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMinimumSize(QtCore.QSize(210, 30))
        self.label_4.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_StatusDescription = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_StatusDescription.setMinimumSize(QtCore.QSize(210, 25))
        self.lineEdit_StatusDescription.setMaximumSize(QtCore.QSize(210, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.lineEdit_StatusDescription.setFont(font)
        self.lineEdit_StatusDescription.setMaxLength(20)
        self.lineEdit_StatusDescription.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_StatusDescription.setObjectName("lineEdit_StatusDescription")
        self.gridLayout_2.addWidget(self.lineEdit_StatusDescription, 2, 1, 1, 1)
        self.comboBox_SelectStatus = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_SelectStatus.setMinimumSize(QtCore.QSize(210, 0))
        self.comboBox_SelectStatus.setMaximumSize(QtCore.QSize(210, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.comboBox_SelectStatus.setFont(font)
        self.comboBox_SelectStatus.setObjectName("comboBox_SelectStatus")
        self.gridLayout_2.addWidget(self.comboBox_SelectStatus, 0, 1, 1, 1)
        self.updateButton = QtWidgets.QPushButton(self.frame_4)
        self.updateButton.setMinimumSize(QtCore.QSize(210, 30))
        self.updateButton.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.updateButton.setFont(font)
        self.updateButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.updateButton.setObjectName("updateButton")
        self.gridLayout_2.addWidget(self.updateButton, 4, 0, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(self.frame_4)
        self.deleteButton.setMinimumSize(QtCore.QSize(210, 30))
        self.deleteButton.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.deleteButton.setFont(font)
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout_2.addWidget(self.deleteButton, 4, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        EmployeeStatus.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeStatus)
        QtCore.QMetaObject.connectSlotsByName(EmployeeStatus)

    def retranslateUi(self, EmployeeStatus):
        _translate = QtCore.QCoreApplication.translate
        EmployeeStatus.setWindowTitle(_translate("EmployeeStatus", "Employee Status"))
        self.label_2.setText(_translate("EmployeeStatus", "<html><head/><body><p><span style=\" font-weight:600;\">Employee</span> Status Detail</p></body></html>"))
        self.label_title.setText(_translate("EmployeeStatus", "<strong>HallyWell</strong> \n"
"Linen Company"))
        self.label.setText(_translate("EmployeeStatus", "Add New Status"))
        self.addButton.setText(_translate("EmployeeStatus", "Add Status"))
        self.lineEdit_EnterNewStatus.setPlaceholderText(_translate("EmployeeStatus", "Enter New Status"))
        self.label_3.setText(_translate("EmployeeStatus", "OR"))
        self.label_5.setText(_translate("EmployeeStatus", "Status Description"))
        self.label_4.setText(_translate("EmployeeStatus", "Select Status to Edit"))
        self.lineEdit_StatusDescription.setPlaceholderText(_translate("EmployeeStatus", "Status Description Here"))
        self.updateButton.setText(_translate("EmployeeStatus", "Update Status"))
        self.deleteButton.setText(_translate("EmployeeStatus", "Delete Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeStatus = QtWidgets.QMainWindow()
    ui = Ui_EmployeeStatus()
    ui.setupUi(EmployeeStatus)
    EmployeeStatus.show()
    sys.exit(app.exec())
