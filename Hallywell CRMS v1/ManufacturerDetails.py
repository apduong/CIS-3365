# Form implementation generated from reading ui file 'ManufacturerDetails.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ManufacturerDetails(object):
    def setupUi(self, ManufacturerDetails):
        ManufacturerDetails.setObjectName("ManufacturerDetails")
        ManufacturerDetails.resize(596, 481)
        ManufacturerDetails.setStyleSheet("background-color:#D0DBE8")
        self.centralwidget = QtWidgets.QWidget(ManufacturerDetails)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QLineEdit{background-color:white;}\n"
"\n"
"\n"
"QLabel{color: #8FA0C9;}\n"
"\n"
"QComboBox{background-color:white;}\n"
"\n"
"QPushButton{border:1px solid white; border-radius:10px;}\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 576, 461))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(300, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/MicrosoftTeams-image.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setStyleSheet("QPushButton{color:#F27E14;}\n"
"\n"
"QPushButton::hover{border: solid black; background-color:white;}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(115, 30))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_ManufacturerD = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_ManufacturerD.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_ManufacturerD.setObjectName("comboBox_ManufacturerD")
        self.horizontalLayout_2.addWidget(self.comboBox_ManufacturerD)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setStyleSheet("QLineEdit{background-color:white;}\n"
"\n"
"QPushButton{background-color:white;border: 2px solid black; border-radius:10px;}\n"
"\n"
"QLabel{color: #8FA0C9;}\n"
"\n"
"QComboBox{background-color:white;}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.lineEdit_ManufacurerName = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_ManufacurerName.setMaximumSize(QtCore.QSize(260, 16777215))
        self.lineEdit_ManufacurerName.setText("")
        self.lineEdit_ManufacurerName.setMaxLength(55)
        self.lineEdit_ManufacurerName.setObjectName("lineEdit_ManufacurerName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_ManufacurerName)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.lineEdit_ManufacturerPhone = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_ManufacturerPhone.setMaximumSize(QtCore.QSize(135, 16777215))
        self.lineEdit_ManufacturerPhone.setText("")
        self.lineEdit_ManufacturerPhone.setMaxLength(15)
        self.lineEdit_ManufacturerPhone.setObjectName("lineEdit_ManufacturerPhone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_ManufacturerPhone)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.comboBox_ManufacturerStatusID = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_ManufacturerStatusID.setMaximumSize(QtCore.QSize(55, 16777215))
        self.comboBox_ManufacturerStatusID.setObjectName("comboBox_ManufacturerStatusID")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_ManufacturerStatusID)
        self.lineEdit_ManufacturerAddress = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_ManufacturerAddress.setMaximumSize(QtCore.QSize(410, 16777215))
        self.lineEdit_ManufacturerAddress.setText("")
        self.lineEdit_ManufacturerAddress.setMaxLength(200)
        self.lineEdit_ManufacturerAddress.setObjectName("lineEdit_ManufacturerAddress")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_ManufacturerAddress)
        self.lineEdit_ManufacturerEmail = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_ManufacturerEmail.setMaximumSize(QtCore.QSize(145, 16777215))
        self.lineEdit_ManufacturerEmail.setText("")
        self.lineEdit_ManufacturerEmail.setMaxLength(200)
        self.lineEdit_ManufacturerEmail.setObjectName("lineEdit_ManufacturerEmail")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_ManufacturerEmail)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setStyleSheet("QPushButton{color:#F27E14;}\n"
"\n"
"QPushButton::hover{border: solid black; background-color:white;}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        ManufacturerDetails.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManufacturerDetails)
        QtCore.QMetaObject.connectSlotsByName(ManufacturerDetails)

    def retranslateUi(self, ManufacturerDetails):
        _translate = QtCore.QCoreApplication.translate
        ManufacturerDetails.setWindowTitle(_translate("ManufacturerDetails", "ManufacturerDetails"))
        self.label.setText(_translate("ManufacturerDetails", "Manufacturer Details"))
        self.label_3.setText(_translate("ManufacturerDetails", "Select Manufacturer ID:"))
        self.pushButton_3.setText(_translate("ManufacturerDetails", "Select Manufacturer ID"))
        self.label_4.setText(_translate("ManufacturerDetails", "Manufacturer Name:"))
        self.label_8.setText(_translate("ManufacturerDetails", "Manufacturer Address:"))
        self.label_5.setText(_translate("ManufacturerDetails", "Manufacturer Email:"))
        self.label_6.setText(_translate("ManufacturerDetails", "Manufacturer Phone:"))
        self.label_7.setText(_translate("ManufacturerDetails", "Manufacturer Status ID:"))
        self.pushButton.setText(_translate("ManufacturerDetails", "Save Changes"))
        self.pushButton_2.setText(_translate("ManufacturerDetails", "Delete Manufacturer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManufacturerDetails = QtWidgets.QMainWindow()
    ui = Ui_ManufacturerDetails()
    ui.setupUi(ManufacturerDetails)
    ManufacturerDetails.show()
    sys.exit(app.exec())
