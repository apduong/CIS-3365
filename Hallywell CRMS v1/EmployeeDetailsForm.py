# Form implementation generated from reading ui file 'EmployeeDetailsForm.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EmployeeDetails(object):
    def setupUi(self, EmployeeDetails):
        EmployeeDetails.setObjectName("EmployeeDetails")
        EmployeeDetails.resize(951, 714)
        EmployeeDetails.setStyleSheet("background-color:#D0DBE8;")
        self.centralwidget = QtWidgets.QWidget(EmployeeDetails)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QLineEdit{background-color:white;}\n"
"QPushButton{border:1px solid white; border-radius:10px;color:#F27E14;}\n"
"QPushButton::hover{border: solid black; background-color:white;}\n"
"QLabel{color: #8FA0C9;}\n"
"QComboBox{background-color:white;}\n"
"QScrollBar{background: black;}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 933, 696))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Form_Name_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Form_Name_2.setFont(font)
        self.Form_Name_2.setStyleSheet("color:#6A7AA6")
        self.Form_Name_2.setAlignment(QtCore.Qt.Alignment.AlignLeading|QtCore.Qt.Alignment.AlignLeft|QtCore.Qt.Alignment.AlignVCenter)
        self.Form_Name_2.setObjectName("Form_Name_2")
        self.horizontalLayout_2.addWidget(self.Form_Name_2)
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setMinimumSize(QtCore.QSize(440, 135))
        self.label_title.setMaximumSize(QtCore.QSize(440, 135))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:#FF800C")
        self.label_title.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_title.setWordWrap(True)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setStyleSheet("QPushButton{color:#F27E14; border:2px solid #F17300; border-radius: 10px;padding:2px;background-color:white;}\n"
"QPushButton::hover{border:2px solid white; background-color:#F27E14; color:white;}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_SelectEmployee = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_SelectEmployee.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_SelectEmployee.setMaximumSize(QtCore.QSize(275, 16777215))
        self.comboBox_SelectEmployee.setObjectName("comboBox_SelectEmployee")
        self.gridLayout.addWidget(self.comboBox_SelectEmployee, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#6A7AA6")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.selectButton = QtWidgets.QPushButton(self.frame_3)
        self.selectButton.setMinimumSize(QtCore.QSize(125, 30))
        self.selectButton.setMaximumSize(QtCore.QSize(116, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectButton.setFont(font)
        self.selectButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.selectButton.setObjectName("selectButton")
        self.gridLayout.addWidget(self.selectButton, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setStyleSheet("QLineEdit{background-color:white;}\n"
"QComboBox{background-color:white;}\n"
"QComboBox QAbstractItemView{background-color:#F17300; color:white;}\n"
"QLabel{color:white;background-color:#F17300; border: solid white; border-radius: 0;}\n"
"QDoubleSpinBox{background-color:white;}\n"
"QPlainTextEdit{background-color:white;}\n"
"\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(32)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_7.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_FirstName.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_FirstName.setMaximumSize(QtCore.QSize(260, 16777215))
        self.lineEdit_FirstName.setText("")
        self.lineEdit_FirstName.setMaxLength(70)
        self.lineEdit_FirstName.setAlignment(QtCore.Qt.Alignment.AlignLeading|QtCore.Qt.Alignment.AlignLeft|QtCore.Qt.Alignment.AlignVCenter)
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")
        self.gridLayout_2.addWidget(self.lineEdit_FirstName, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setMinimumSize(QtCore.QSize(220, 0))
        self.label_10.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_10.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMinimumSize(QtCore.QSize(220, 0))
        self.label_9.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_9.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.lineEdit_MiddleName = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_MiddleName.setMaximumSize(QtCore.QSize(115, 16777215))
        self.lineEdit_MiddleName.setMaxLength(70)
        self.lineEdit_MiddleName.setObjectName("lineEdit_MiddleName")
        self.gridLayout_2.addWidget(self.lineEdit_MiddleName, 2, 1, 1, 1)
        self.lineEdit_LastName = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_LastName.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_LastName.setMaxLength(70)
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        self.gridLayout_2.addWidget(self.lineEdit_LastName, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(220, 0))
        self.label_6.setMaximumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_6.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_Address1 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_Address1.setMaximumSize(QtCore.QSize(260, 16777215))
        self.lineEdit_Address1.setMaxLength(150)
        self.lineEdit_Address1.setObjectName("lineEdit_Address1")
        self.gridLayout_2.addWidget(self.lineEdit_Address1, 6, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setMinimumSize(QtCore.QSize(175, 0))
        self.label_12.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 7, 2, 1, 1)
        self.comboBox_EmployeeStatusID = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_EmployeeStatusID.setObjectName("comboBox_EmployeeStatusID")
        self.gridLayout_2.addWidget(self.comboBox_EmployeeStatusID, 7, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setMinimumSize(QtCore.QSize(175, 0))
        self.label_11.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 2, 1, 1)
        self.lineEdit_DateOfBirth = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_DateOfBirth.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_DateOfBirth.setStyleSheet("QLineEdit{(\"yyyy-mm-dd\")}")
        self.lineEdit_DateOfBirth.setInputMask("")
        self.lineEdit_DateOfBirth.setText("")
        self.lineEdit_DateOfBirth.setObjectName("lineEdit_DateOfBirth")
        self.gridLayout_2.addWidget(self.lineEdit_DateOfBirth, 6, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMinimumSize(QtCore.QSize(175, 0))
        self.label_8.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)
        self.lineEdit_PostalCode = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_PostalCode.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_PostalCode.setMaxLength(10)
        self.lineEdit_PostalCode.setObjectName("lineEdit_PostalCode")
        self.gridLayout_2.addWidget(self.lineEdit_PostalCode, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_5.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)
        self.comboBox_Country = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Country.setMaximumSize(QtCore.QSize(140, 16777215))
        self.comboBox_Country.setObjectName("comboBox_Country")
        self.gridLayout_2.addWidget(self.comboBox_Country, 1, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setMinimumSize(QtCore.QSize(130, 0))
        self.label_14.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.comboBox_StateProvince = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_StateProvince.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_StateProvince.setMaximumSize(QtCore.QSize(130, 16777215))
        self.comboBox_StateProvince.setObjectName("comboBox_StateProvince")
        self.gridLayout_2.addWidget(self.comboBox_StateProvince, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setMinimumSize(QtCore.QSize(220, 0))
        self.label_13.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 7, 0, 1, 1)
        self.lineEdit_Address2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_Address2.setMaximumSize(QtCore.QSize(260, 16777215))
        self.lineEdit_Address2.setMaxLength(150)
        self.lineEdit_Address2.setObjectName("lineEdit_Address2")
        self.gridLayout_2.addWidget(self.lineEdit_Address2, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 9, 0, 1, 1)
        self.lineEdit_City = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_City.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_City.setMaxLength(200)
        self.lineEdit_City.setObjectName("lineEdit_City")
        self.gridLayout_2.addWidget(self.lineEdit_City, 9, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("QPushButton{color:#F27E14; border:2px solid #F17300; border-radius: 10px;padding:2px;background-color:white;}\n"
"QPushButton::hover{border:2px solid white; background-color:#F27E14; color:white;}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.save_Button = QtWidgets.QPushButton(self.frame_5)
        self.save_Button.setMinimumSize(QtCore.QSize(125, 30))
        self.save_Button.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_Button.setFont(font)
        self.save_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save_Button.setObjectName("save_Button")
        self.horizontalLayout_4.addWidget(self.save_Button)
        self.delete_Button = QtWidgets.QPushButton(self.frame_5)
        self.delete_Button.setMinimumSize(QtCore.QSize(125, 30))
        self.delete_Button.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delete_Button.setFont(font)
        self.delete_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_Button.setObjectName("delete_Button")
        self.horizontalLayout_4.addWidget(self.delete_Button)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        EmployeeDetails.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeDetails)
        QtCore.QMetaObject.connectSlotsByName(EmployeeDetails)

    def retranslateUi(self, EmployeeDetails):
        _translate = QtCore.QCoreApplication.translate
        EmployeeDetails.setWindowTitle(_translate("EmployeeDetails", "Employee Details"))
        self.Form_Name_2.setText(_translate("EmployeeDetails", "<html><head/><body><p><span style=\" font-weight:600;\">Employee</span> Details</p></body></html>"))
        self.label_title.setText(_translate("EmployeeDetails", "<strong>HallyWell</strong> \n"
"Linen Company"))
        self.label_4.setText(_translate("EmployeeDetails", "Select Employee Name:"))
        self.selectButton.setText(_translate("EmployeeDetails", "Select Employee"))
        self.label_7.setText(_translate("EmployeeDetails", "First Name"))
        self.lineEdit_FirstName.setPlaceholderText(_translate("EmployeeDetails", "Enter First Name"))
        self.label_10.setText(_translate("EmployeeDetails", "Address 1"))
        self.label_9.setText(_translate("EmployeeDetails", "Middle Name"))
        self.lineEdit_MiddleName.setPlaceholderText(_translate("EmployeeDetails", "Enter Middle Name"))
        self.lineEdit_LastName.setPlaceholderText(_translate("EmployeeDetails", "Enter Last Name"))
        self.label_6.setText(_translate("EmployeeDetails", "Last Name"))
        self.lineEdit_Address1.setPlaceholderText(_translate("EmployeeDetails", "Enter Address 1"))
        self.label_12.setText(_translate("EmployeeDetails", "Employee Status ID"))
        self.label_11.setText(_translate("EmployeeDetails", "Date of Birth"))
        self.lineEdit_DateOfBirth.setPlaceholderText(_translate("EmployeeDetails", "Enter Birthdate"))
        self.label_8.setText(_translate("EmployeeDetails", "Postal Code"))
        self.lineEdit_PostalCode.setPlaceholderText(_translate("EmployeeDetails", "Enter Postal"))
        self.label_5.setText(_translate("EmployeeDetails", "Country"))
        self.label_14.setText(_translate("EmployeeDetails", "State Province"))
        self.label_13.setText(_translate("EmployeeDetails", "Address 2"))
        self.lineEdit_Address2.setPlaceholderText(_translate("EmployeeDetails", "Enter Address 1"))
        self.label.setText(_translate("EmployeeDetails", "City"))
        self.lineEdit_City.setPlaceholderText(_translate("EmployeeDetails", "Enter City"))
        self.save_Button.setText(_translate("EmployeeDetails", "Save Changes"))
        self.delete_Button.setText(_translate("EmployeeDetails", "Delete Employee"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeDetails = QtWidgets.QMainWindow()
    ui = Ui_EmployeeDetails()
    ui.setupUi(EmployeeDetails)
    EmployeeDetails.show()
    sys.exit(app.exec())