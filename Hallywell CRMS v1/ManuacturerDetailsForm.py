# Form implementation generated from reading ui file 'ManufacturerDetailsForm.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ManufacturerDetails(object):
    def setupUi(self, ManufacturerDetails):
        ManufacturerDetails.setObjectName("ManufacturerDetails")
        ManufacturerDetails.resize(951, 714)
        ManufacturerDetails.setStyleSheet("background-color:#D0DBE8;")
        self.centralwidget = QtWidgets.QWidget(ManufacturerDetails)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#6A7AA6")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox_SearchManufacturer = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_SearchManufacturer.setMinimumSize(QtCore.QSize(260, 0))
        self.comboBox_SearchManufacturer.setMaximumSize(QtCore.QSize(260, 16777215))
        self.comboBox_SearchManufacturer.setObjectName("comboBox_SearchManufacturer")
        self.horizontalLayout.addWidget(self.comboBox_SearchManufacturer)
        self.selectButton = QtWidgets.QPushButton(self.frame_3)
        self.selectButton.setMinimumSize(QtCore.QSize(125, 30))
        self.selectButton.setMaximumSize(QtCore.QSize(116, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectButton.setFont(font)
        self.selectButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.selectButton.setObjectName("selectButton")
        self.horizontalLayout.addWidget(self.selectButton)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setStyleSheet("QLineEdit{background-color:white;}\n"
"QComboBox{background-color:white;}\n"
"QComboBox QAbstractItemView{background-color:#F17300; color:white;}\n"
"QLabel{color:white;background-color:#F17300; border: solid white; border-radius: 0;}\n"
"QDoubleSpinBox{background-color:white;}\n"
"QPlainTextEdit{background-color:white;}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(32)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setMinimumSize(QtCore.QSize(220, 0))
        self.label_13.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)
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
        self.comboBox_ManufacturerStatusID = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_ManufacturerStatusID.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_ManufacturerStatusID.setObjectName("comboBox_ManufacturerStatusID")
        self.gridLayout_2.addWidget(self.comboBox_ManufacturerStatusID, 4, 2, 1, 1)
        self.lineEdit_ManufacturerName = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_ManufacturerName.setMinimumSize(QtCore.QSize(260, 0))
        self.lineEdit_ManufacturerName.setMaximumSize(QtCore.QSize(260, 16777215))
        self.lineEdit_ManufacturerName.setText("")
        self.lineEdit_ManufacturerName.setMaxLength(60)
        self.lineEdit_ManufacturerName.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_ManufacturerName.setObjectName("lineEdit_ManufacturerName")
        self.gridLayout_2.addWidget(self.lineEdit_ManufacturerName, 0, 2, 1, 1)
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
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
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
        self.lineEdit_ManufacturerAddress = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_ManufacturerAddress.setMinimumSize(QtCore.QSize(440, 0))
        self.lineEdit_ManufacturerAddress.setMaximumSize(QtCore.QSize(440, 16777215))
        self.lineEdit_ManufacturerAddress.setText("")
        self.lineEdit_ManufacturerAddress.setMaxLength(270)
        self.lineEdit_ManufacturerAddress.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_ManufacturerAddress.setObjectName("lineEdit_ManufacturerAddress")
        self.gridLayout_2.addWidget(self.lineEdit_ManufacturerAddress, 1, 2, 1, 1)
        self.lineEdit_ManufacturerEmail = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_ManufacturerEmail.setMinimumSize(QtCore.QSize(170, 0))
        self.lineEdit_ManufacturerEmail.setMaximumSize(QtCore.QSize(170, 16777215))
        self.lineEdit_ManufacturerEmail.setText("")
        self.lineEdit_ManufacturerEmail.setMaxLength(110)
        self.lineEdit_ManufacturerEmail.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_ManufacturerEmail.setObjectName("lineEdit_ManufacturerEmail")
        self.gridLayout_2.addWidget(self.lineEdit_ManufacturerEmail, 2, 2, 1, 1)
        self.lineEdit_ManufacturerPhone = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_ManufacturerPhone.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_ManufacturerPhone.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_ManufacturerPhone.setText("")
        self.lineEdit_ManufacturerPhone.setMaxLength(30)
        self.lineEdit_ManufacturerPhone.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.lineEdit_ManufacturerPhone.setObjectName("lineEdit_ManufacturerPhone")
        self.gridLayout_2.addWidget(self.lineEdit_ManufacturerPhone, 3, 2, 1, 1)
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
        self.delete_Button.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delete_Button.setFont(font)
        self.delete_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_Button.setObjectName("delete_Button")
        self.horizontalLayout_4.addWidget(self.delete_Button)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        ManufacturerDetails.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManufacturerDetails)
        QtCore.QMetaObject.connectSlotsByName(ManufacturerDetails)

    def retranslateUi(self, ManufacturerDetails):
        _translate = QtCore.QCoreApplication.translate
        ManufacturerDetails.setWindowTitle(_translate("ManufacturerDetails", "Manufacturer Details"))
        self.Form_Name_2.setText(_translate("ManufacturerDetails", "<html><head/><body><p><span style=\" font-weight:600;\">Manufacturer</span> Details</p></body></html>"))
        self.label_title.setText(_translate("ManufacturerDetails", "<strong>HallyWell</strong> \n"
"Linen Company"))
        self.label_3.setText(_translate("ManufacturerDetails", "Select Manufacturer Name:"))
        self.selectButton.setText(_translate("ManufacturerDetails", "Select Manufacturer"))
        self.label_13.setText(_translate("ManufacturerDetails", "Manufacturer Status"))
        self.label_6.setText(_translate("ManufacturerDetails", "Manufacturer Address"))
        self.lineEdit_ManufacturerName.setPlaceholderText(_translate("ManufacturerDetails", "Enter Manufacturer Name"))
        self.label_7.setText(_translate("ManufacturerDetails", "Manufacturer Name"))
        self.label_10.setText(_translate("ManufacturerDetails", "Manufacturer Phone"))
        self.label_9.setText(_translate("ManufacturerDetails", "Manufacturer Email"))
        self.lineEdit_ManufacturerAddress.setPlaceholderText(_translate("ManufacturerDetails", "Enter Manufacturer Address"))
        self.lineEdit_ManufacturerEmail.setPlaceholderText(_translate("ManufacturerDetails", "Enter Email"))
        self.lineEdit_ManufacturerPhone.setPlaceholderText(_translate("ManufacturerDetails", "Enter Phone"))
        self.save_Button.setText(_translate("ManufacturerDetails", "Save Changes"))
        self.delete_Button.setText(_translate("ManufacturerDetails", "Delete Manufacturer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManufacturerDetails = QtWidgets.QMainWindow()
    ui = Ui_ManufacturerDetails()
    ui.setupUi(ManufacturerDetails)
    ManufacturerDetails.show()
    sys.exit(app.exec())
