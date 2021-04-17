from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import *
from loadingscreen import Ui_LoadingScreen
from mainscreen import Ui_MainScreen
import pyodbc
# todo: import all form classes here
# ==> Customer Forms
from NewCustomerForm import Ui_NewCustomerForm
from CustomerDetailsForm import Ui_CustomerDetails
# ==> Order Forms
from OrderDetail import Ui_OrderStatus  # FIXME: Class name does not match the form name
# ==> ReturnCode Forms
from ReturnCodeDetail import Ui_ReturnCodeStatus
# ==> Product Forms
from NewProductForm import Ui_NewProductForm
from ProductColorDetail import Ui_ProductColorDetail
from ProductDetailForm import Ui_ProductDetails
from ProductRatingDetail import Ui_ProductRatingDetail
from ProductStatusDetail import Ui_ProductStatusDetail
from ProductTypeDetail import Ui_ProductTypeDetail
from ProductMaterialDetail import Ui_ProductMaterialDetail
from ProductHistoryDetail import Ui_ProductHistoryDetail
from ProductThreadDetail import Ui_ProductThreadDetail
from ProductSizeDetail import Ui_ProductSizeDetail
# ==> Shipment Forms
from NewShipmentForm import Ui_NewShipmentForm
from ShipmentDetailsForm import Ui_ShipmentDetails
# ==> Employee Forms
from NewEmployeeForm import Ui_NewEmployeeForm
from EmployeeDetail import Ui_EmployeeStatus
from EmployeeDetailsForm import Ui_EmployeeDetails
# ==> Distributor Forms
from DistributorContactForm import Ui_DistributorContactForm
from DistributorDetailsForm import Ui_DistributorDetails
from DistributorDetailsForm import Ui_DistributorDetails
# ==> Manufacturer Forms
from ManufacturerContactForm import Ui_ManufacturerContactForm
from ManufacturerDetail import Ui_ManufacturerStatus
from ManufacturerDetailsForm import Ui_ManufacturerDetails
# ==> Promotion Forms
from PromotionDetailsForm import Ui_PromotionDetails  # FIXME: Class name and form name should be more descriptive.. Eg, 'NewPromotion'
from NewPromotionForm import Ui_NewPromotionForm
# ==> Channel Forms
from ChannelDetailsForm import Ui_ChannelDetails
from NewChannelStatusForm import Ui_NewChannelStatusForm

counter = 0


# Loading Screen - DO NOT TOUCH
class LoadingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowFlags.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(30)
        self.ui.dropshadowframe.setGraphicsEffect(self.shadow)
        self.ui.label_description.setText("<strong>WELCOME</strong> To Our Customer Relationship Management System")
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.open_mainscreen()
            self.close()
        counter += 1

    def open_mainscreen(self):
        self.ui = MainScreen()
        self.ui.show()


class MainScreen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)
        # ===> ASSIGN ALL BUTTONS TO OPEN FORMS
        # ==> Customer Forms
        self.ui.addCusButton.clicked.connect(self.open_NewCustomerForm)
        self.ui.edit_cus.clicked.connect(self.open_CustomerDetailsForm)
        # ==> Order Forms
        # self.ui.addOrdButton.clicked.connect(open_OrderDetail)  # TODO: Create Order Class and Open Function
        # self.ui.edit_order_status.clicked.connect(self.open_orderstatus)
        # ==> Product Forms
        self.ui.addButton.clicked.connect(self.open_productform)
        self.ui.edit_color.clicked.connect(self.open_productcolordetail)
        self.ui.edit_proddet.clicked.connect(self.open_productdetail)
        self.ui.edit_type.clicked.connect(self.open_producttypedetail)
        self.ui.edit_hist.clicked.connect(self.open_producthistorydetail)
        self.ui.edit_rate.clicked.connect(self.open_productratingdetail)
        self.ui.edit_mat.clicked.connect(self.open_productmaterialdetail)
        self.ui.edit_prodsize.clicked.connect(self.open_productsizedetail)
        self.ui.edit_thread.clicked.connect(self.open_productthreaddetail)
        self.ui.edit_stat.clicked.connect(self.open_productstatusdetail)
        # ==> Shipment Forms
        self.ui.addShip.clicked.connect(self.open_NewShipmentForm)
        self.ui.edit_shipdet.clicked.connect(self.open_ShipmentDetailsForm)
        # ==> Employee Forms
        self.ui.addEmploy.clicked.connect(self.open_NewEmployeeForm)
        self.ui.edit_empdet.clicked.connect(self.open_EmployeeDetailsForm)
        self.ui.edit_empstat.clicked.connect(self.open_EmployeeDetails)
        # ==> Distributor Forms
        self.ui.edit_discon.clicked.connect(self.open_DistributorContactForm)
        self.ui.edit_disdet.clicked.connect(self.open_DistributorDetailsForm)
        # self.ui.edit_disstat.clicked.connect()  # TODO: Create Distributor Status Form
        # ==> Manufacturer Forms
        self.ui.edit_manucon.clicked.connect(self.open_ManufacturerContactForm)
        self.ui.edit_manudet.clicked.connect(self.open_ManufacturerDetailsForm)
        self.ui.edit_manustat.clicked.connect(self.open_ManufacturerDetail)
        # ==> Promotion Forms
        self.ui.addPromoButton.clicked.connect(self.open_NewPromotionForm)
        self.ui.edit_promodet.clicked.connect(self.open_PromotionDetailsForm)
        # ==> Channel Forms
        self.ui.edit_chandet.clicked.connect(self.open_ChannelDetailsForm)
        self.ui.edit_chandet.clicked.connect(self.open_NewChannelStausForm)
        # ==> Return Code Forms
        # self.ui.edit_returnstat.clicked.connect(self.open_ReturnCodeDetail)

# ===> PLACE FORM DISPLAY FUNCTIONS BELOW HERE
# todo: add functions to open all forms
# ==> CUSTOMER FORMS
    # NEW CUSTOMER FORM
    def open_NewCustomerForm(self):  # FIXME: Make this function name lower case
        self.form = NewCustomerForm()
        self.form.show()

    # CUSTOMER DETAILS FORM
    def open_CustomerDetailsForm(self):  # FIXME: Make this function name lower case
        self.form = CustomerDetailsForm()
        self.form.show()

# ==> ORDER FORMS
    # ORDER STATUS DETAILS
    def open_OrderDetail(self):
        self.form = OrderDetail()
        self.form.show()

# ==> RETURN CODE FORMS
    # Return code status
    def open_ReturnCodeDetail(self):
        self.form = ReturnCodeDetail()
        self.form.show()

# ==> PRODUCT FORMS
    # NEW PRODUCT FORM
    def open_productform(self):
        self.form = NewProductForm()
        self.form.show()

    # PRODUCT DETAIL FORM
    def open_productdetail(self):
        self.form = ProductDetail()
        self.form.show()

    # PRODUCT COLOR DETAIL
    def open_productcolordetail(self):
        self.form = ProductColorDetail()
        self.form.show()

    # PRODUCT RATING DETAIL
    def open_productratingdetail(self):
        self.form = ProductRatingDetail()
        self.form.show()

    # PRODUCT STATUS DETAIL
    def open_productstatusdetail(self):
        self.form = ProductStatusDetail()
        self.form.show()

    # PRODUCT TYPE DETAIL
    def open_producttypedetail(self):
        self.form = ProductTypeDetail()
        self.form.show()

    # PRODUCT THREAD DETAIL
    def open_productthreaddetail(self):
        self.form = ProductThreadDetail()
        self.form.show()

    # PRODUCT SIZE DETAIL
    def open_productsizedetail(self):
        self.form = ProductSizeDetail()
        self.form.show()

    # PRODUCT MATERIAL DETAIL
    def open_productmaterialdetail(self):
        self.form = ProductMaterialDetail()
        self.form.show()

    # PRODUCT HISTORY DETAIL
    def open_producthistorydetail(self):
        self.form = ProductHistoryDetail()
        self.form.show()

# ==> SHIPMENT FORMS
    # NEW SHIPMENT
    def open_NewShipmentForm(self):
        self.form = NewShipmentForm()
        self.form.show()

    # SHIPMENT DETAILS
    def open_ShipmentDetailsForm(self):
        self.form = ShipmentDetailsForm()
        self.form.show()

# ==> EMPLOYEE FORMS
    # NEW EMPLOYEE FORM
    def open_NewEmployeeForm(self):
        self.form = NewEmployeeForm()
        self.form.show()

    # EMPLOYEE DETAILS
    def open_EmployeeDetailsForm(self):
        self.form = EmployeeDetailsForm()
        self.form.show()

    # EMPLOYEE STATUS DETAILS
    def open_EmployeeDetails(self):
        self.form = EmployeeDetails()
        self.form.show()

# ==> DISTRIBUTOR FORMS
    # DISTRIBUTOR CONTACT FORM
    def open_DistributorContactForm(self):  # FIXME: Make this function name lower case
        self.form = DistributorContactForm()
        self.form.show()

# FIXME: Duplicate Distributor Details function calls.
    # DISTRIBUTOR DETAILS
    def open_DistributorDetailsForm(self):
        self.form = DistributorDetailsForm()
        self.form.show()

# ==> MANUFACTURER FORMS
    # MANUFACTURER CONTACT FORM
    def open_ManufacturerContactForm(self):  # FIXME: Make this function name lower case
        self.form = ManufacturerContactForm()
        self.form.show()

    # MANUFACTURER DETAILS
    def open_ManufacturerDetailsForm(self):
        self.form = ManufacturerDetailsForm()
        self.form.show()

    # MANUFACTURER STATUS DETAILS
    def open_ManufacturerDetail(self):
        self.form = ManufacturerDetail()
        self.form.show()

# ==> PROMOTION FORMS
    # PROMOTION
    def open_NewPromotionForm(self):
        self.form = NewPromotionForm()
        self.form.show()

    # PROMOTION DETAILS
    def open_PromotionDetailsForm(self):
        self.form = PromotionDetailsForm()
        self.form.show()

# ==> Channel FORMS
    # CHANNEL DETAILS FORM
    def open_ChannelDetailsForm(self):  # FIXME: Make this function name lower case
        self.form = ChannelDetailsForm()
        self.form.show()

    # CHANNEL
    def open_NewChannelStausForm(self):
        self.form = NewChannelStausForm()
        self.form.show()


# ===> PLACE DESIGN CLASSES BELOW HERE
# REQ: All form functionality will be added here
# todo: Create classes for all forms
# ==> CUSTOMER FORMS CLASSES
class NewCustomerForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewCustomerForm()
        self.ui.setupUi(self)


class CustomerDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_CustomerDetails()
        self.ui.setupUi(self)


# ==> ORDER FORMS CLASSES
class OrderDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_OrderStatus()
        self.ui.setupUi(self)


# ==> PRODUCT FORMS CLASSES
class NewProductForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewProductForm()
        self.ui.setupUi(self)


class ProductDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductDetails()
        self.ui.setupUi(self)


class ProductColorDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductColorDetail()
        self.ui.setupUi(self)


class ProductRatingDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductRatingDetail()
        self.ui.setupUi(self)


class ProductStatusDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductStatusDetail()
        self.ui.setupUi(self)


class ProductThreadDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductThreadDetail()
        self.ui.setupUi(self)


class ProductHistoryDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductHistoryDetail()
        self.ui.setupUi(self)


class ProductMaterialDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductMaterialDetail()
        self.ui.setupUi(self)


class ProductTypeDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductTypeDetail()
        self.ui.setupUi(self)


class ProductSizeDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductSizeDetail()
        self.ui.setupUi(self)


# ==> PROMOTION FORMS CLASSES
class NewPromotionForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewPromotionForm()
        self.ui.setupUi(self)


class PromotionDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_PromotionDetails()
        self.ui.setupUi(self)


# ==> EMPLOYEE FORMS CLASSES
class EmployeeDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_EmployeeStatus()
        self.ui.setupUi(self)


class EmployeeDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_EmployeeDetails()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        print(self.table_data)
        self.country_data = self.load_data()[1]
        self.state_data = self.load_data()[2]
        self.status_data = self.load_data()[3]
        self.set_employeelist()
        self.ui.selectButton.clicked.connect(self.display_data)
        self.ui.save_Button.clicked.connect(self.save_data)
        self.ui.delete_Button.clicked.connect(self.delete_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()

        data = cursor.execute('SELECT * FROM Employee WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]

        data = cursor.execute('SELECT * FROM Country WHERE IS_DELETE = 0')
        country_data = [[item for item in row] for row in data]

        data = cursor.execute('SELECT * FROM State_Province WHERE IS_DELETE = 0')
        state_data = [[item for item in row] for row in data]

        data = cursor.execute('SELECT * FROM Employee_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]

        return table_data, country_data, state_data, status_data

    def set_employeelist(self):
        employee_names =[]
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    employee_names.append(name)
        self.ui.comboBox_SelectEmployee.addItems(employee_names)

        country_list = []
        for i, item in enumerate(self.country_data):
            country_list.append(item[1])
        self.ui.comboBox_Country.addItems(country_list)

        state_data = []
        for i, item in enumerate(self.state_data):
            state_data.append(item[1])
        self.ui.comboBox_StateProvince.addItems(state_data)

        status_data = []
        for i, item in enumerate(self.status_data):
            status_data.append(item[1])
        self.ui.comboBox_EmployeeStatusID.addItems(status_data)

    def display_data(self):
        selected_name = self.ui.comboBox_SelectEmployee.currentText()
        employee_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                employee_details.append(row)
        for row in employee_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_FirstName.setText(item)
                elif i == 2:
                    self.ui.lineEdit_LastName.setText(item)
                elif i == 3:
                    self.ui.lineEdit_MiddleName.setText(item)
                elif i == 4:
                    self.ui.lineEdit_Address1.setText(item)
                elif i == 5:
                    self.ui.lineEdit_Address2.setText(item)
                elif i == 6:
                    self.ui.lineEdit_City.setText(item)
                elif i == 7:
                    for x, state in enumerate(self.state_data):
                        if state[0] == item:
                            self.ui.comboBox_StateProvince.setCurrentIndex(item-1)
                elif i == 8:
                    for x, country in enumerate(self.country_data):
                        if country[0] == item:
                            self.ui.comboBox_Country.setCurrentIndex(item-1)
                elif i == 9:
                    self.ui.lineEdit_PostalCode.setText(str(item))
                elif i == 10:
                    self.ui.lineEdit_DateOfBirth.setText(item)
                elif i == 11:
                    for x, status in enumerate(self.status_data):
                        if status[0] == item:
                            self.ui.comboBox_EmployeeStatusID.setCurrentIndex(item-1)
    def get_data(self):
        selected_name = self.ui.comboBox_SelectEmployee.currentText()
        employee_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                employee_details.append(row)
        return employee_details

    def save_data(self):
        employee_details = self.get_data()
        employee_details[0][1] = self.ui.lineEdit_FirstName.text()
        employee_details[0][2] = self.ui.lineEdit_LastName.text()
        employee_details[0][3] = self.ui.lineEdit_MiddleName.text()
        employee_details[0][4] = self.ui.lineEdit_Address1.text()
        employee_details[0][5] = self.ui.lineEdit_Address2.text()
        employee_details[0][6] = self.ui.lineEdit_City.text()
        employee_details[0][7] = int()
        for row in self.state_data:
            if row[1] == self.ui.comboBox_StateProvince.currentText():
                employee_details[0][7] = row[0]
        employee_details[0][8] = int()
        for row in self.country_data:
            if row[1] == self.ui.comboBox_Country.currentText():
                employee_details[0][8] = row[0]
        employee_details[0][9] = self.ui.lineEdit_PostalCode.text()
        employee_details[0][10] = self.ui.lineEdit_DateOfBirth.text()
        employee_details[0][11] = int()
        for row in self.status_data:
            if row[1] == self.ui.comboBox_EmployeeStatusID.currentText():
                employee_details[0][11] = row[0]
        employeeconnection = server_connection()
        cursor = employeeconnection.cursor()
        cursor.execute("UPDATE Employee SET FIRST_NAME = ?, LAST_NAME = ?, MIDDLE_NAME = ?, ADDRESS_1 = ?, ADDRESS_2 = ?, CITY = ?, STATE_PROVINCE_ID = ?, COUNTRY_ID = ?, POSTAL_CODE = ?,"
                       "DATE_OF_BIRTH = ?, EMPLOYEE_STATUS_ID = ? WHERE EMP_ID = ?", employee_details[0][1], employee_details[0][2],employee_details[0][3], employee_details[0][4],
                       employee_details[0][5], employee_details[0][6], employee_details[0][7], employee_details[0][8], employee_details[0][9], employee_details[0][10],
                       employee_details[0][11], employee_details[0][0])
        employeeconnection.commit()
        self.ui.lineEdit_FirstName.clear()
        self.ui.lineEdit_LastName.clear()
        self.ui.lineEdit_MiddleName.clear()
        self.ui.lineEdit_Address1.clear()
        self.ui.lineEdit_Address2.clear()
        self.ui.lineEdit_City.clear()
        self.ui.comboBox_StateProvince.clear()
        self.ui.comboBox_Country.clear()
        self.ui.lineEdit_PostalCode.clear()
        self.ui.lineEdit_DateOfBirth.clear()
        self.ui.comboBox_EmployeeStatusID.clear()
        self.table_data = self.load_data()
        self.set_employeelist()

    def delete_data(self):
        employee_details = self.get_data()
        employeeconnection = server_connection()
        cursor = employeeconnection.cursor()
        cursor.execute("UPDATE Employee SET IS_DELETE = 1 WHERE EMP_ID = ?", employee_details[0][0])
        employeeconnection.commit()
        self.ui.lineEdit_FirstName.clear()
        self.ui.lineEdit_LastName.clear()
        self.ui.lineEdit_MiddleName.clear()
        self.ui.lineEdit_Address1.clear()
        self.ui.lineEdit_Address2.clear()
        self.ui.lineEdit_City.clear()
        self.ui.comboBox_StateProvince.clear()
        self.ui.comboBox_Country.clear()
        self.ui.lineEdit_PostalCode.clear()
        self.ui.lineEdit_DateOfBirth.clear()
        self.ui.comboBox_EmployeeStatusID.clear()
        self.table_data = self.load_data()[0]
        self.set_employeelist()


# ==> SHIPMENT FORMS CLASSES
# FIXME: Class name on NewShipmentForm and ShipmentDetails is the same
class NewShipmentForm(QMainWindow):  # FIXME: Capitalize the F in form :)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewShipmentForm()
        self.ui.setupUi(self)


class ShipmentDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ShipmentDetails()
        self.ui.setupUi(self)


# ==> EMPLOYEE FORMS CLASSES
class NewEmployeeForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewEmployeeForm()
        self.ui.setupUi(self)


class EmployeeDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_EmployeeDetails()
        self.ui.setupUi(self)


class EmployeeStatusDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_EmployeeStatusDetails()
        self.ui.setupUi(self)


# ==> DISTRIBUTOR FORMS CLASSES
class DistributorContactForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorContactForm()
        self.ui.setupUi(self)


class DistributorDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorDetails()
        self.ui.setupUi(self)


class DistributorStatus(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorStatus()
        self.ui.setupUi(self)


# ==> MANUFACTURER FORMS CLASSES
class ManufacturerContactForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerContactForm()
        self.ui.setupUi(self)


class ManufacturerDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerDetails()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        print(self.table_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()

        data = cursor.execute('SELECT * FROM Manufacturer WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]

        data = cursor.execute('SELECT * FROM Manufacturer_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]

        return table_data, status_data

    def set_manufacturerlist(self):
        manufacturer_names = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i ==1:
                    manufacturer_names.append(name)
        self.ui.comboBox_SearchManufacturer.addItems(manufacturer_names)

    def display_data(self):
        selected_name = self.ui.comboBox_SearchManufacturer.currentText()
        manufacturer_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                manufacturer_details.append(row)
        for row in manufacturer_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_ManufacturerName.setText(item)
                elif i == 2:
                    self.ui.lineEdit_ManufacturerAddress.setText(item)
                elif i == 3:
                    self.ui.lineEdit_ManufacturerEmail.setText(item)
                elif i == 4:
                    self.ui.lineEdit_ManufacturerPhone.setText(item)
                elif i == 5:
                    for x, status in enumerate(self.status_data):
                        if status[0] == item:
                            self.ui.comboBox_ManufacturerStatusID.setCurrentIndex(item-1)

    def get_data(self):
        seleceted_name =

class ManufacturerDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerStatus()
        self.ui.setupUi(self)


# ==> PROMOTION FORMS CLASSES
class Promotion(QMainWindow):  # FIXME: Class name and form name should be more descriptive.. Eg, 'NewPromotion'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Promotion()
        self.ui.setupUi(self)


class PromotionDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_PromotionDetails()
        self.ui.setupUi(self)


# ==> CHANNEL FORMS CLASSES
class ChannelDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ChannelDetails()
        self.ui.setupUi(self)    


# ==> RESOURCES
def server_connection():
    conn = pyodbc.connect('Driver={SQL Server};'  # Leave this as is
                          'Server=FAITH;'  # Enter your local Server Name
                          'Database=cis3365db;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    return conn


if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    app.exec()
