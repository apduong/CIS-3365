# Form implementation generated from reading ui file 'NewPromotionForm.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NewPromotionForm(object):
    def setupUi(self, NewPromotionForm):
        NewPromotionForm.setObjectName("NewPromotionForm")
        NewPromotionForm.resize(913, 625)
        NewPromotionForm.setAutoFillBackground(False)
        NewPromotionForm.setStyleSheet("background-color:#D0DBE8;")
        self.centralwidget = QtWidgets.QWidget(NewPromotionForm)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 219, 232))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.scrollArea.setPalette(palette)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet("QLineEdit{background-color:white;}\n"
"QPushButton{border:1px solid white; border-radius:10px;}\n"
"QLabel{color: #8FA0C9;}\n"
"QComboBox{background-color:white;}\n"
"QScrollBar{background: black;}\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 895, 607))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Form_Name = QtWidgets.QLabel(self.frame)
        self.Form_Name.setMinimumSize(QtCore.QSize(0, 100))
        self.Form_Name.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Form_Name.setFont(font)
        self.Form_Name.setStyleSheet("color:#6A7AA6")
        self.Form_Name.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.Form_Name.setObjectName("Form_Name")
        self.horizontalLayout.addWidget(self.Form_Name)
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
        self.horizontalLayout.addWidget(self.label_title)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#8FA0C9")
        self.label_2.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red")
        self.label.setAlignment(QtCore.Qt.Alignment.AlignRight|QtCore.Qt.Alignment.AlignTrailing|QtCore.Qt.Alignment.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #8FA0C9")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("QLineEdit{background-color:white;}\n"
"QComboBox{background-color:white;}\n"
"QComboBox QAbstractItemView{background-color:#F17300; color:white;}\n"
"QLabel{color:white;background-color:#F17300; border: solid white; border-radius: 0;}\n"
"QDoubleSpinBox{background-color:white;}\n"
"QPlainTextEdit{background-color:white;}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(32)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
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
        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{color:red;background-color:none; border: solid white; border-radius: 0;}\n"
"\n"
"")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.comboBox_SeasonID = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_SeasonID.setMaximumSize(QtCore.QSize(35, 16777215))
        self.comboBox_SeasonID.setObjectName("comboBox_SeasonID")
        self.gridLayout.addWidget(self.comboBox_SeasonID, 5, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{color:red;background-color:none; border: solid white; border-radius: 0;}\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_4.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.lineEdit_PromotionDescription = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_PromotionDescription.setMaximumSize(QtCore.QSize(220, 16777215))
        self.lineEdit_PromotionDescription.setText("")
        self.lineEdit_PromotionDescription.setMaxLength(42)
        self.lineEdit_PromotionDescription.setObjectName("lineEdit_PromotionDescription")
        self.gridLayout.addWidget(self.lineEdit_PromotionDescription, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{color:red;background-color:none; border: solid white; border-radius: 0;}\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
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
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.lineEdit_DiscountAmount = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_DiscountAmount.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_DiscountAmount.setText("")
        self.lineEdit_DiscountAmount.setMaxLength(21)
        self.lineEdit_DiscountAmount.setObjectName("lineEdit_DiscountAmount")
        self.gridLayout.addWidget(self.lineEdit_DiscountAmount, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setStyleSheet("QPushButton{color:#F27E14; border:2px solid #F17300; border-radius: 10px;padding:2px;background-color:white;}\n"
"QPushButton::hover{border:2px solid white; background-color:#F27E14; color:white;}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.submit_Button = QtWidgets.QPushButton(self.frame_4)
        self.submit_Button.setMinimumSize(QtCore.QSize(116, 30))
        self.submit_Button.setMaximumSize(QtCore.QSize(116, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.submit_Button.setFont(font)
        self.submit_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.submit_Button.setFlat(False)
        self.submit_Button.setObjectName("submit_Button")
        self.horizontalLayout_3.addWidget(self.submit_Button)
        self.clear_button = QtWidgets.QPushButton(self.frame_4)
        self.clear_button.setMinimumSize(QtCore.QSize(116, 30))
        self.clear_button.setMaximumSize(QtCore.QSize(116, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clear_button.setFont(font)
        self.clear_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_3.addWidget(self.clear_button)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        NewPromotionForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewPromotionForm)
        QtCore.QMetaObject.connectSlotsByName(NewPromotionForm)

    def retranslateUi(self, NewPromotionForm):
        _translate = QtCore.QCoreApplication.translate
        NewPromotionForm.setWindowTitle(_translate("NewPromotionForm", "NewPromotionForm"))
        self.Form_Name.setText(_translate("NewPromotionForm", "<html><head/><body><p>New <span style=\" font-weight:600;\">Promotion</span></p></body></html>"))
        self.label_title.setText(_translate("NewPromotionForm", "<strong>HallyWell</strong> \n"
"Linen Company"))
        self.label_2.setText(_translate("NewPromotionForm", "Please fill out all required and applicable information."))
        self.label.setText(_translate("NewPromotionForm", "*"))
        self.label_3.setText(_translate("NewPromotionForm", "- required fields"))
        self.label_9.setText(_translate("NewPromotionForm", "Season ID"))
        self.label_8.setText(_translate("NewPromotionForm", "*"))
        self.label_5.setText(_translate("NewPromotionForm", "*"))
        self.label_4.setText(_translate("NewPromotionForm", "Promotion Description"))
        self.lineEdit_PromotionDescription.setPlaceholderText(_translate("NewPromotionForm", "Enter Promotion Description"))
        self.label_7.setText(_translate("NewPromotionForm", "*"))
        self.label_6.setText(_translate("NewPromotionForm", "Discount Amount"))
        self.lineEdit_DiscountAmount.setPlaceholderText(_translate("NewPromotionForm", "Enter Discount Amount"))
        self.submit_Button.setText(_translate("NewPromotionForm", "Submit Form"))
        self.clear_button.setText(_translate("NewPromotionForm", "Clear Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewPromotionForm = QtWidgets.QMainWindow()
    ui = Ui_NewPromotionForm()
    ui.setupUi(NewPromotionForm)
    NewPromotionForm.show()
    sys.exit(app.exec())
