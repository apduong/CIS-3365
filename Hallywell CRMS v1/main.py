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
from CustomerDetailsForm import Ui_CustomerDetailsForm
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
from NewDistributorForm import Ui_NewDistributorForm
from NewDistributorContact import Ui_NewDistributorContact
from DistributorContactForm import Ui_DistributorContactForm
from DistributorDetailsForm import Ui_DistributorDetails
from DistributorStatusDetail import Ui_DistributorStatusDetail
# ==> Manufacturer Forms
from NewManufacturerForm import Ui_NewManufacturerForm
from NewManufacturerContact import Ui_NewManufacturerContact
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
        # self.ui.addOrdButton.clicked.connect()  # TODO: Create Order Class and Open Function
        self.ui.edit_order_status.clicked.connect(self.open_OrderDetail)
        # ==> Payment Forms
        # self.ui.addPayButton.clicked.connect(self.open_newpayment)
        # self.ui.edit_pay_det.clicked.connect(self.open_paymentdetails)
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
        self.ui.edit_empdet.clicked.connect(self.open_employeedetails)
        self.ui.edit_empstat.clicked.connect(self.open_employeestatusdetail)
        # ==> Distributor Forms
        self.ui.add_dis.clicked.connect(self.open_newdistributorform)
        self.ui.addNewDC.clicked.connect(self.open_newdistributorcontact)
        self.ui.edit_discon.clicked.connect(self.open_DistributorContactForm)
        self.ui.edit_disdet.clicked.connect(self.open_DistributorDetailsForm)
        self.ui.edit_disstat.clicked.connect(self.open_distributorstatusdetail)
        # ==> Manufacturer Forms
        self.ui.new_manuconButton.clicked.connect(self.open_newmanufacturercontactform)
        self.ui.addButton_manu.clicked.connect(self.open_newmanufacturerform)
        self.ui.edit_manucon.clicked.connect(self.open_ManufacturerContactForm)
        self.ui.edit_manudet.clicked.connect(self.open_ManufacturerDetailsForm)
        self.ui.edit_manustat.clicked.connect(self.open_ManufacturerDetail)
        # ==> Promotion Forms
        self.ui.addPromoButton.clicked.connect(self.open_NewPromotionForm)
        self.ui.edit_promodet.clicked.connect(self.open_PromotionDetailsForm)
        # ==> Channel Forms
        self.ui.edit_chandet.clicked.connect(self.open_ChannelDetailsForm)

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
    def open_employeedetails(self):
        self.form = EmployeeDetailsForm()
        self.form.show()

    # EMPLOYEE STATUS DETAILS
    def open_employeestatusdetail(self):
        self.form = EmployeeDetail()
        self.form.show()

    # ==> DISTRIBUTOR FORMS
    # NEW DISTRIBUTOR FORM
    def open_newdistributorform(self):
        self.form = NewDistributorForm()
        self.form.show()

    # NEW DISTRIBUTOR CONTACT
    def open_newdistributorcontact(self):
        self.form = NewDistributorContact()
        self.form.show()

    # DISTRIBUTOR CONTACT FORM
    def open_DistributorContactForm(self):  # FIXME: Make this function name lower case
        self.form = DistributorContactForm()
        self.form.show()


    # FIXME: Duplicate Distributor Details function calls.
    # DISTRIBUTOR DETAILS
    def open_DistributorDetailsForm(self):
        self.form = DistributorDetailsForm()
        self.form.show()

     # DISTRIBUTOR STATUS
    def open_distributorstatusdetail(self):
        self.form = DistributorStatus()
        self.form.show()

    # ==> MANUFACTURER FORMS
    # NEW MANUFACTURER FORM
    def open_newmanufacturerform(self):
        self.form = NewManufacturerForm()
        self.form.show()

    def open_newmanufacturercontactform(self):
        self.form = NewManufacturerContactForm()
        self.form.show()

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

    # NEW CHANNEL FORM
    def open_NewChannelStausForm(self):
        self.form = ChannelDetailsForm()
        self.form.show()


# ===> PLACE DESIGN CLASSES BELOW HERE
# REQ: All form functionality will be added here
# todo: Create classes for all forms
# ==> CUSTOMER FORMS CLASSES
# todo: Test this form
class NewCustomerForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewCustomerForm()
        self.ui.setupUi(self)
        self.country = self.load_data()[0]
        self.state = self.load_data()[1]
        self.status = self.load_data()[2]
        self.display_data()
        self.ui.submit_button.clicked.connect(self.add_data)
        self.ui.clear_button.clicked.connect(self.clear_form)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Country WHERE IS_DELETE = 0')
        country_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM State_Province WHERE IS_DELETE = 0')
        state_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Customer_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]
        return country_data, state_data, status_data

    def display_data(self):
        countries = []
        for country in self.country:
            countries.append(country[1])
        country_list = sorted(countries)
        states = []
        for state in self.state:
            states.append(state[1])
        state_list = sorted(states)
        status_list = []
        for status in self.status:
            status_list.append(status[1])
        self.ui.comboBox_Country.addItems(country_list)
        self.ui.comboBox_StateProvince.addItems(state_list)
        self.ui.comboBox.addItems(status_list)

    def add_data(self):
        last_name = self.ui.lineEdit_LastName.text()
        first_name = self.ui.lineEdit_FirstName.text()
        prim_phone = str(self.ui.lineEdit_primNum.text())
        sec_phone = str(self.ui.lineEdit_secNum.text())
        email = self.ui.lineEdit.text()
        country_id = int()
        for row in self.country:
            if row[1] == self.ui.comboBox_Country.currentText():
                country_id = row[0]
        state_id = int()
        for row in self.state:
            if row[1] == self.ui.comboBox_StateProvince.currentText():
                state_id = row[0]
        status_id = int()
        for row in self.status:
            if row[1] == self.ui.comboBox.currentText():
                status_id = row[0]
        address_1 = self.ui.lineEdit_Address1.text()
        address_2 = self.ui.lineEdit_Address2.text()
        city = self.ui.lineEdit_City.text()
        postal = self.ui.lineEdit_PostalCode.text()
        insta = self.ui.lineEdit_instagram.text()
        facebook = self.ui.lineEdit_facebook.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Customer (CUST_LASTNAME, CUST_FIRSTNAME, CUST_PRIMARYPHONE, CUST_SECONDARYPHONE, "
                       "CUST_EMAIL, COUNTRY_ID, STATE_PROVINCE_ID, CUSTOMER_STATUS_ID, CUST_ADDRESS1, CUST_ADDRESS2,"
                       " CUST_CITY, CUST_POSTALCODE, CUST_INSTAGRAM, CUST_FACEBOOK, IS_DELETE) "
                       "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,0)", last_name, first_name, prim_phone, sec_phone, email,
                       country_id, state_id, status_id, address_1, address_2, city, postal, insta, facebook)
        cnxn.commit()

    def clear_form(self):
        self.ui.lineEdit_LastName.clear()
        self.ui.lineEdit_FirstName.clear()
        self.ui.lineEdit_facebook.clear()
        self.ui.lineEdit_instagram.clear()
        self.ui.lineEdit_City.clear()
        self.ui.lineEdit_secNum.clear()
        self.ui.lineEdit_Address2.clear()
        self.ui.lineEdit_primNum.clear()
        self.ui.lineEdit_Address1.clear()
        self.ui.lineEdit.clear()


# FIXME: Clear input mask from actual data
class CustomerDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_CustomerDetailsForm()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        self.country = self.load_data()[1]
        self.state = self.load_data()[2]
        self.status = self.load_data()[3]
        self.set_cus()
        self.display_data()
        self.ui.selectButton.clicked.connect(self.display_data)
        self.ui.save_button.clicked.connect(self.update_data)
        self.ui.delete_button.clicked.connect(self.delete_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Customer WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Country WHERE IS_DELETE = 0')
        country_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM State_Province WHERE IS_DELETE = 0')
        state_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Customer_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]
        return table_data, country_data, state_data, status_data

    def set_cus(self):
        cus_names = []
        for row in self.table_data:
            print(row)
            for i, name in enumerate(row):
                print(name)
                if i == 1:
                    cus_names.append(f"{row[2]} {name}")
        self.ui.comboBox_cusname.addItems(cus_names)
        countries = []
        for country in self.country:
            countries.append(country[1])
        country_list = sorted(countries)
        states = []
        for state in self.state:
            states.append(state[1])
        state_list = sorted(states)
        status_list = []
        for status in self.status:
            status_list.append(status[1])
        self.ui.comboBox_Country.addItems(country_list)
        self.ui.comboBox_StateProvince.addItems(state_list)
        self.ui.comboBox.addItems(status_list)

    def get_data(self):
        selected_name = self.ui.comboBox_cusname.currentText()
        name = selected_name.split()
        customer_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == name[1]:
                customer_details.append(row)
        return customer_details

    def display_data(self):
        customer_details = self.get_data()
        for row in customer_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_LastName.setText(item)
                elif i == 2:
                    self.ui.lineEdit_FirstName.setText(item)
                elif i == 3:
                    self.ui.lineEdit_primNum.setText(item)
                elif i == 4:
                    self.ui.lineEdit_secNum.setText(item)
                elif i == 5:
                    self.ui.lineEdit.setText(item)
                elif i == 6:
                    for country in self.country:
                        if country[0] == item:
                            self.ui.comboBox_Country.setCurrentIndex(item-1)
                elif i == 7:
                    for state in self.state:
                        if state[0] == item:
                            self.ui.comboBox_StateProvince.setCurrentIndex(item-1)
                elif i == 8:
                    for status in self.status:
                        if status[0] == item:
                            self.ui.comboBox.setCurrentIndex(item-1)
                elif i == 9:
                    self.ui.lineEdit_Address1.setText(item)
                elif i == 10:
                    self.ui.lineEdit_Address2.setText(item)
                elif i == 11:
                    self.ui.lineEdit_City.setText(item)
                elif i == 12:
                    self.ui.lineEdit_PostalCode.setText(item)
                elif i == 13:
                    self.ui.lineEdit_instagram.setText(item)
                elif i == 14:
                    self.ui.lineEdit_facebook.setText(item)

    def update_data(self):
        customer_details = self.get_data()
        last_name = self.ui.lineEdit_LastName.text()
        first_name = self.ui.lineEdit_FirstName.text()
        prim_phone = str(self.ui.lineEdit_primNum.text())
        sec_phone = str(self.ui.lineEdit_secNum.text())
        email = self.ui.lineEdit.text()
        country_id = int()
        for row in self.country:
            if row[1] == self.ui.comboBox_Country.currentText():
                country_id = row[0]
        state_id = int()
        for row in self.state:
            if row[1] == self.ui.comboBox_StateProvince.currentText():
                state_id = row[0]
        status_id = int()
        for row in self.status:
            if row[1] == self.ui.comboBox.currentText():
                status_id = row[0]
        address_1 = self.ui.lineEdit_Address1.text()
        address_2 = self.ui.lineEdit_Address2.text()
        city = self.ui.lineEdit_City.text()
        postal = self.ui.lineEdit_PostalCode.text()
        insta = self.ui.lineEdit_instagram.text()
        facebook = self.ui.lineEdit_facebook.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Customer SET CUST_LASTNAME = ?, CUST_FIRSTNAME = ?, CUST_PRIMARYPHONE =?, "
                       "CUST_SECONDARYPHONE =?,CUST_EMAIL = ?, COUNTRY_ID = ?, STATE_PROVINCE_ID = ?, "
                       "CUSTOMER_STATUS_ID = ?, CUST_ADDRESS1 = ?, CUST_ADDRESS2 = ?, CUST_CITY = ?, "
                       "CUST_POSTALCODE = ?, CUST_INSTAGRAM = ?, CUST_FACEBOOK = ?, IS_DELETE = 0 "
                       "WHERE CUSTOMER_ID = ?", last_name, first_name, prim_phone, sec_phone, email,
                       country_id, state_id, status_id, address_1, address_2, city, postal, insta, facebook,
                       customer_details[0][0])
        cnxn.commit()
        # Re-query Table Data
        self.ui.comboBox_cusname.clear()
        self.table_data = self.load_data()[0]
        self.set_cus()

    def delete_data(self):
        customer_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Customer SET IS_DELETE = 1 WHERE CUSTOMER_ID = ?", customer_details[0][0])
        cnxn.commit()
        # Re-query Table Data
        self.ui.comboBox_cusname.clear()
        self.table_data = self.load_data()[0]
        self.set_cus()


# ==> ORDER FORMS CLASSES
# ORDER STATUS
class OrderDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_OrderStatus()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_order_detail_list()
        self.ui.comboBox_SelectStatus.currentIndexChanged.connect(self.display_details)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.updateButton.clicked.connect(self.update_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data =  cursor.execute('SELECT * FROM Order_Status WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_order_detail_list(self):
        statuses = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    statuses.append(name)
        self.ui.comboBox_SelectStatus.addItems(statuses)

    def get_data(self):
        selected_name = self.ui.comboBox_SelectStatus.currentText()
        status_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                status_details.append(row)
        return status_details

    def display_details(self):
        status_details = self.get_data()
        for row in status_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_StatusDescription.setText(item)

    def update_data(self):
        status_details = self.get_data()
        status_details[0][1] = self.ui.lineEdit_StatusDescription.text()
        ordercnxn = server_connection()
        cursor = ordercnxn.cursor()
        cursor.execute("UPDATE Order_Status SET ORDER_STATUS_DESCRIPTION = ? WHERE ORDER_STATUS_ID = ?",
                       status_details[0][1], status_details[0][0])
        ordercnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_order_detail_list()

    def delete_data(self):
        status_details = self.get_data()
        ordercnxn = server_connection()
        cursor = ordercnxn.cursor()
        cursor.execute("UPDATE Order_Status SET IS_DELETE = 1 WHERE ORDER_STATUS_ID = ?",
                       status_details[0][0])
        ordercnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_order_detail_list()

    def add_data(self):
        insert_data = self.ui.lineEdit_EnterNewStatus.text()
        ordercnxn = server_connection()
        cursor = ordercnxn.cursor()
        cursor.execute("INSERT INTO Order_Status (ORDER_STATUS_DESCRIPTION, IS_DELETE) VALUES (?,0)", insert_data)
        ordercnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_order_detail_list()
        self.ui.lineEdit_EnterNewStatus.clear()


# ==> PRODUCT FORMS CLASSES
# Fully Functional
class NewProductForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewProductForm()
        self.ui.setupUi(self)
        self.product_status_data = self.load_data()[0]
        self.product_type_data = self.load_data()[1]
        self.product_size_data = self.load_data()[2]
        self.product_history_data = self.load_data()[3]
        self.product_thread_data = self.load_data()[4]
        self.product_material_data = self.load_data()[5]
        self.manufacturer_data = self.load_data()[6]
        self.color_data = self.load_data()[7]
        self.display_data()
        self.ui.submit_Button.clicked.connect(self.add_data)
        self.ui.clear_button.clicked.connect(self.clear_form)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Product_Status WHERE IS_DELETE = 0')
        product_status_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Product_Type WHERE IS_DELETE = 0')
        product_type_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Size WHERE IS_DELETE = 0')
        product_size_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Product_History WHERE IS_DELETE = 0')
        product_history_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Thread WHERE IS_DELETE = 0')
        product_thread_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Material WHERE IS_DELETE = 0')
        product_material_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Color WHERE IS_DELETE = 0')
        color_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Manufacturer WHERE IS_DELETE = 0')
        manufacturer_data = [[item for item in row] for row in data]
        return product_status_data, product_type_data, product_size_data, product_history_data, \
            product_thread_data, product_material_data, manufacturer_data, color_data

    def display_data(self):
        status_list = []
        for status in self.product_status_data:
            status_list.append(status[1])
        type_list = []
        for types in self.product_type_data:
            type_list.append(types[1])
        size_list = []
        for size in self.product_size_data:
            size_list.append(size[1])
        history_list = []
        for history in self.product_history_data:
            history_list.append(history[1])
        thread_list = []
        for thread in self.product_thread_data:
            thread_list.append(thread[1])
        material_list = []
        for material in self.product_material_data:
            material_list.append(material[1])
        manufacturer_list = []
        for manufacturer in self.manufacturer_data:
            manufacturer_list.append(manufacturer[1])
        color_list = []
        for color in self.color_data:
            color_list.append(color[1])
        self.ui.comboBox.addItems(status_list)
        self.ui.comboBox_Type.addItems(type_list)
        self.ui.comboBox_Color.addItems(color_list)
        self.ui.comboBox_Material.addItems(material_list)
        self.ui.comboBox_Manu.addItems(manufacturer_list)
        self.ui.comboBox_Thread.addItems(thread_list)
        self.ui.comboBox_History.addItems(history_list)
        self.ui.comboBox_Size.addItems(size_list)

    def add_data(self):
        product_name = self.ui.prod_name.toPlainText()
        product_desc = self.ui.description_box.toPlainText()
        product_price = self.ui.Product_Price.value()
        status_code = int()
        type_code = int()
        size_code = int()
        history_code = int()
        thread_code = int()
        material_code = int()
        color_code = int()
        manu_code = int()
        for row in self.product_status_data:
            if row[1] == self.ui.comboBox.currentText():
                status_code = row[0]
        for row in self.product_type_data:
            if row[1] == self.ui.comboBox_Type.currentText():
                type_code = row[0]
        for row in self.product_size_data:
            if row[1] == self.ui.comboBox_Size.currentText():
                size_code = row[0]
        for row in self.product_history_data:
            if row[1] == self.ui.comboBox_History.currentText():
                history_code = row[0]
        for row in self.product_thread_data:
            if row[1] == self.ui.comboBox_Thread.currentText():
                thread_code = row[0]
        for row in self.product_material_data:
            if row[1] == self.ui.comboBox_Material.currentText():
                material_code = row[0]
        for row in self.color_data:
            if row[1] == self.ui.comboBox_Color.currentText():
                color_code = row[0]
        for row in self.manufacturer_data:
            if row[1] == self.ui.comboBox_Manu.currentText():
                manu_code = row[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Product (PRODUCT_NAME, PRODUCT_DESCRIPTION, PRICE, PRODUCT_STATUS_CODE, "
                       "PRODUCT_TYPE_CODE, SIZE_CODE, PRODUCT_HISTORY_CODE, THREAD_CODE, MATERIAL_CODE, COLOR_CODE, "
                       "MANUFACTURER_ID, IS_DELETE) "
                       "VALUES (?,?,?,?,?,?,?,?,?,?,?,0)", product_name, product_desc, product_price, status_code,
                       type_code, size_code, history_code, thread_code, material_code, color_code, manu_code)
        cnxn.commit()

    def clear_form(self):
        self.ui.prod_name.clear()
        self.ui.Product_Price.setValue(0.00)
        self.ui.description_box.clear()


# Fully Functional
class ProductDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductDetails()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        self.product_status_data = self.load_data()[1]
        self.product_type_data = self.load_data()[2]
        self.product_size_data = self.load_data()[3]
        self.product_history_data = self.load_data()[4]
        self.product_thread_data = self.load_data()[5]
        self.product_material_data = self.load_data()[6]
        self.manufacturer_data = self.load_data()[7]
        self.color_data = self.load_data()[8]
        self.set_prodlist()
        self.display_data()
        self.ui.selectButton.clicked.connect(self.display_data)
        self.ui.save_Button.clicked.connect(self.update_data)
        self.ui.delete_Button.clicked.connect(self.delete_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Product WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Product_Status WHERE IS_DELETE = 0')
        product_status_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Product_Type WHERE IS_DELETE = 0')
        product_type_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Size WHERE IS_DELETE = 0')
        product_size_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Product_History WHERE IS_DELETE = 0')
        product_history_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Thread WHERE IS_DELETE = 0')
        product_thread_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Material WHERE IS_DELETE = 0')
        product_material_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Color WHERE IS_DELETE = 0')
        color_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Manufacturer WHERE IS_DELETE = 0')
        manufacturer_data = [[item for item in row] for row in data]
        return table_data, product_status_data, product_type_data, product_size_data, product_history_data, \
            product_thread_data, product_material_data, manufacturer_data, color_data

    def set_prodlist(self):
        product_names = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    product_names.append(name)
        self.ui.comboBox_selectProd.addItems(product_names)
        status_list = []
        for status in self.product_status_data:
            status_list.append(status[1])
        type_list = []
        for types in self.product_type_data:
            type_list.append(types[1])
        size_list = []
        for size in self.product_size_data:
            size_list.append(size[1])
        history_list = []
        for history in self.product_history_data:
            history_list.append(history[1])
        thread_list = []
        for thread in self.product_thread_data:
            thread_list.append(thread[1])
        material_list = []
        for material in self.product_material_data:
            material_list.append(material[1])
        manufacturer_list = []
        for manufacturer in self.manufacturer_data:
            manufacturer_list.append(manufacturer[1])
        color_list = []
        for color in self.color_data:
            color_list.append(color[1])
        self.ui.comboBox.addItems(status_list)
        self.ui.comboBox_Type.addItems(type_list)
        self.ui.comboBox_Color.addItems(color_list)
        self.ui.comboBox_Material.addItems(material_list)
        self.ui.comboBox_Manu.addItems(manufacturer_list)
        self.ui.comboBox_Thread.addItems(thread_list)
        self.ui.comboBox_History.addItems(history_list)
        self.ui.comboBox_Size.addItems(size_list)

    def get_data(self):
        selected_name = self.ui.comboBox_selectProd.currentText()
        product_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                product_details.append(row)
        return product_details

    def display_data(self):
        product_details = self.get_data()
        for row in product_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.prod_name.setPlainText(item)
                elif i == 2:
                    self.ui.description_box.setPlainText(item)
                elif i == 3:
                    self.ui.Product_Price.setValue(item)
                elif i == 4:
                    for status in self.product_status_data:
                        if status[0] == item:
                            self.ui.comboBox.setCurrentIndex(item-1)
                elif i == 5:
                    for types in self.product_type_data:
                        if types[0] == item:
                            self.ui.comboBox_Type.setCurrentIndex(item-1)
                elif i == 6:
                    for size in self.product_size_data:
                        if size[0] == item:
                            self.ui.comboBox_Size.setCurrentIndex(item-1)
                elif i == 7:
                    for history in self.product_history_data:
                        if history[0] == item:
                            self.ui.comboBox_History.setCurrentIndex(item-1)
                elif i == 8:
                    for thread in self.product_thread_data:
                        if thread[0] == item:
                            self.ui.comboBox_Thread.setCurrentIndex(item-1)
                elif i == 9:
                    for material in self.product_material_data:
                        if material[0] == item:
                            self.ui.comboBox_Material.setCurrentIndex(item-1)
                elif i == 10:
                    for x, color in enumerate(self.color_data):
                        if color[0] == item:
                            self.ui.comboBox_Color.setCurrentIndex(item - 1)

    def update_data(self):
        product_details = self.get_data()
        product_name = self.ui.prod_name.toPlainText()
        product_desc = self.ui.description_box.toPlainText()
        product_price = self.ui.Product_Price.value()
        status_code = int()
        type_code = int()
        size_code = int()
        history_code = int()
        thread_code = int()
        material_code = int()
        color_code = int()
        manu_code = int()
        for row in self.product_status_data:
            if row[1] == self.ui.comboBox.currentText():
                status_code = row[0]
        for row in self.product_type_data:
            if row[1] == self.ui.comboBox_Type.currentText():
                type_code = row[0]
        for row in self.product_size_data:
            if row[1] == self.ui.comboBox_Size.currentText():
                size_code = row[0]
        for row in self.product_history_data:
            if row[1] == self.ui.comboBox_History.currentText():
                history_code = row[0]
        for row in self.product_thread_data:
            if row[1] == self.ui.comboBox_Thread.currentText():
                thread_code = row[0]
        for row in self.product_material_data:
            if row[1] == self.ui.comboBox_Material.currentText():
                material_code = row[0]
        for row in self.color_data:
            if row[1] == self.ui.comboBox_Color.currentText():
                color_code = row[0]
        for row in self.manufacturer_data:
            if row[1] == self.ui.comboBox_Manu.currentText():
                manu_code = row[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE PRODUCT SET PRODUCT_NAME = ?, PRODUCT_DESCRIPTION = ?, PRICE = ?,"
                       " PRODUCT_STATUS_CODE = ?, PRODUCT_TYPE_CODE = ?, SIZE_CODE = ?, PRODUCT_HISTORY_CODE = ?, "
                       "THREAD_CODE = ?, MATERIAL_CODE = ?, COLOR_CODE = ?, MANUFACTURER_ID = ?, IS_DELETE = 0 "
                       "WHERE PRODUCT_ID = ?", product_name, product_desc, product_price, status_code,
                       type_code, size_code, history_code, thread_code, material_code, color_code, manu_code,
                       product_details[0][0])
        cnxn.commit()
        # Re-query Table Data
        self.ui.comboBox_selectProd.clear()
        self.table_data = self.load_data()[0]
        self.set_prodlist()

    def delete_data(self):
        product_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Product SET IS_DELETE = 1 WHERE PRODUCT_ID = ?", product_details[0][0])
        cnxn.commit()
        # Re-query Table Data
        self.ui.comboBox_selectProd.clear()
        self.table_data = self.load_data()[0]
        self.set_prodlist()


# todo: Test this form
class ProductColorDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductColorDetail()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_colorlist()
        self.ui.comboBox_select.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Color WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_colorlist(self):
        colors = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    colors.append(name)
        self.ui.comboBox_select.addItems(colors)

    def get_data(self):
        selected_name = self.ui.comboBox_select.currentText()
        color_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                color_details.append(row)
        return color_details

    def display_data(self):
        color_details = self.get_data()
        for row in color_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_desc.setText(item)

    def update_data(self):
        color_details = self.get_data()
        color_details[0][1] = self.ui.lineEdit_desc.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Color SET COLOR_DESCRIPTION = ? WHERE COLOR_CODE = ?",
                       color_details[0][1], color_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_colorlist()

    def delete_data(self):  # Logical Delete Only
        color_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Color SET IS_DELETE = 1 WHERE COLOR_CODE = ?", color_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_colorlist()

    def add_data(self):
        insert_data = self.ui.lineEdit_new.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Color (COLOR_DESCRIPTION, IS_DELETE) VALUES (?, 0)", insert_data)
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_colorlist()
        self.ui.lineEdit_new.clear()


# Fully Functional
class ProductRatingDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductRatingDetail()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_ratinglist()
        self.ui.comboBox_select.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Rating_Scale WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_ratinglist(self):
        ratings = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    ratings.append(name)
        self.ui.comboBox_select.addItems(ratings)

    def get_data(self):
        selected_name = self.ui.comboBox_select.currentText()
        rating_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                rating_details.append(row)
        return rating_details

    def display_data(self):
        rating_details = self.get_data()
        for row in rating_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_desc.setText(item)

    def update_data(self):
        rating_details = self.get_data()
        rating_details[0][1] = self.ui.lineEdit_desc.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Rating_Scale SET PRODUCT_RATING_DESC = ? WHERE PRODUCT_RATING_CODE = ?",
                       rating_details[0][1], rating_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_ratinglist()

    def delete_data(self):  # Logical Delete Only
        rating_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Rating_Scale SET IS_DELETE = 1 WHERE PRODUCT_RATING_CODE = ?", rating_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_ratinglist()

    def add_data(self):
        insert_data = self.ui.lineEdit_new.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Rating_Scale (PRODUCT_RATING_DESC, IS_DELETE) VALUES (?, 0)", insert_data)
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_ratinglist()
        self.ui.lineEdit_new.clear()


# Fully Functional
class ProductStatusDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductStatusDetail()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_statuslist()
        self.ui.comboBox_select.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Product_Status WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_statuslist(self):
        statuses = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    statuses.append(name)
        self.ui.comboBox_select.addItems(statuses)

    def get_data(self):
        selected_name = self.ui.comboBox_select.currentText()
        status_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                status_details.append(row)
        return status_details

    def display_data(self):
        status_details = self.get_data()
        for row in status_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_desc.setText(item)

    def update_data(self):
        status_details = self.get_data()
        print(status_details)
        status_details[0][1] = self.ui.lineEdit_desc.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Product_Status SET PRODUCT_STATUS_DES = ? WHERE PRODUCT_STATUS_CODE = ?",
                       status_details[0][1], status_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_statuslist()

    def delete_data(self):  # Logical Delete Only
        status_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Product_Status SET IS_DELETE = 1 WHERE PRODUCT_STATUS_CODE = ?", status_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_statuslist()

    def add_data(self):
        insert_data = self.ui.lineEdit_new.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Product_Status (PRODUCT_STATUS_DES, IS_DELETE) VALUES (?, 0)", insert_data)
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_statuslist()
        self.ui.lineEdit_new.clear()


# todo: Test this form
class ProductThreadDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductThreadDetail()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_threadlist()
        self.ui.comboBox_select.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Thread WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_threadlist(self):
        threads = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    threads.append(name)
        self.ui.comboBox_select.addItems(threads)

    def get_data(self):
        selected_name = self.ui.comboBox_select.currentText()
        thread_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                thread_details.append(row)
        return thread_details

    def display_data(self):
        thread_details = self.get_data()
        for row in thread_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_desc.setText(item)


    def delete_data(self):  # Logical Delete Only
        thread_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Thread SET IS_DELETE = 1 WHERE THREAD_CODE = ?", thread_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_threadlist()

    def add_data(self):
        insert_data = self.ui.lineEdit_new.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Thread (THREAD_DESCRIPTION, IS_DELETE) VALUES (?, 0)", insert_data)
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_threadlist()
        self.ui.lineEdit_new.clear()


# todo: Test this form
class ProductHistoryDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductHistoryDetail()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_historylist()
        self.ui.comboBox_select.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Product_History WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_historylist(self):
        history = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    history.append(name)
        self.ui.comboBox_select.addItems(history)

    def get_data(self):
        selected_name = self.ui.comboBox_select.currentText()
        history_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                history_details.append(row)
        return history_details

    def display_data(self):
        history_details = self.get_data()
        for row in history_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_desc.setText(item)


    def delete_data(self):  # Logical Delete Only
        history_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Product_History SET IS_DELETE = 1 WHERE PRODUCT_HISTORY_CODE = ?", history_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_historylist()

    def add_data(self):
        insert_data = self.ui.lineEdit_new.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Product_History (PRODUCT_HISTORY_DESCRIPTION, IS_DELETE) VALUES (?, 0)", insert_data)
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_historylist()
        self.ui.lineEdit_new.clear()


# todo: Test this form
class ProductMaterialDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductMaterialDetail()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_materiallist()
        self.ui.comboBox_select.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Material WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_materiallist(self):
        materials = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    materials.append(name)
        self.ui.comboBox_select.addItems(materials)

    def get_data(self):
        selected_name = self.ui.comboBox_select.currentText()
        material_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                material_details.append(row)
        return material_details

    def display_data(self):
        material_details = self.get_data()
        for row in material_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_desc.setText(item)


    def delete_data(self):  # Logical Delete Only
        material_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Material SET IS_DELETE = 1 WHERE MATERIAL_CODE = ?", material_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_materiallist()

    def add_data(self):
        insert_data = self.ui.lineEdit_new.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Material (MATERIAL_DESCRIPTION, IS_DELETE) VALUES (?, 0)", insert_data)
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_materiallist()
        self.ui.lineEdit_new.clear()


# todo: Test this form
class ProductTypeDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductTypeDetail()
        self.ui.setupUi(self)

    def update_data(self):
        thread_details = self.get_data()
        thread_details[0][1] = self.ui.lineEdit_desc.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Thread SET THREAD_DESCRIPTION = ? WHERE THREAD_CODE = ?",
                       thread_details[0][1], thread_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_threadlist()

    def delete_data(self):  # Logical Delete Only
        type_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Product_Type SET IS_DELETE = 1 WHERE PRODUCT_TYPE_CODE = ?", type_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_typelist()

    def add_data(self):
        insert_data = self.ui.lineEdit_new.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Product_Type (PRODUCT_TYPE_DESCRIPTION, IS_DELETE) VALUES (?, 0)", insert_data)
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_typelist()
        self.ui.lineEdit_new.clear()


# todo: Test this form
class ProductSizeDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductSizeDetail()
        self.ui.setupUi(self)

    def update_data(self):
        history_details = self.get_data()
        history_details[0][1] = self.ui.lineEdit_desc.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Product_History SET PRODUCT_HISTORY_DESCRIPTION = ? WHERE PRODUCT_HISTORY_CODE = ?",
                       history_details[0][1], history_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_historylist()


# ==> SHIPMENT FORMS CLASSES
# FIXME: Class name on NewShipmentForm and ShipmentDetails is the same
class NewShipmentForm(QMainWindow):  # FIXME: Capitalize the F in form :)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewShipmentForm()
        self.ui.setupUi(self)

    def update_data(self):
        type_details = self.get_data()
        type_details[0][1] = self.ui.lineEdit_desc.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Product_Type SET PRODUCT_TYPE_DESCRIPTION = ? WHERE PRODUCT_TYPE_CODE = ?",
                       type_details[0][1], type_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_typelist()


class ShipmentDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ShipmentDetails()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_typelist()
        self.ui.comboBox_select.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Product_Type WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_typelist(self):
        types = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    types.append(name)
        self.ui.comboBox_select.addItems(types)

    def get_data(self):
        selected_name = self.ui.comboBox_select.currentText()
        type_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                type_details.append(row)
        return type_details

    def display_data(self):
        type_details = self.get_data()
        for row in type_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_desc.setText(item)

# FIXME: Try not to commit changes that breaks the entire program


# ==> EMPLOYEE FORMS CLASSES
#todo: test this form
class NewEmployeeForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewEmployeeForm()
        self.ui.setupUi(self)
        self.country_data = self.load_data()[0]
        self.state_data = self.load_data()[1]
        self.status_data = self.load_data()[2]
        self.display_data()
        self.ui.save_Button.clicked.connect(self.add_data)
        self.ui.delete_Button.clicked.connect(self.clear_form)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Country WHERE IS_DELETE = 0')
        country_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM State_Province WHERE IS_DELETE = 0')
        state_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Employee_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]
        return country_data, state_data, status_data

    def display_data(self):
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

    def add_data(self):
        first_name = self.ui.lineEdit_FirstName.text()
        lastname = self.ui.lineEdit_LastName.text()
        middle = self.ui.lineEdit_MiddleName.text()
        address_1 = self.ui.lineEdit_Address1.text()
        address_2 = self.ui.lineEdit_Address2.text()
        city = self.ui.lineEdit_City.text()
        state_code = int()
        for row in self.state_data:
            if row[1] == self.ui.comboBox_StateProvince.currentText():
                state_code = row[0]
        country = int()
        for row in self.country_data:
            if row[1] == self.ui.comboBox_Country.currentText():
                country = row[0]
        postal_code = self.ui.lineEdit_PostalCode.text()
        dob = self.ui.lineEdit_DateOfBirth.text()
        status = int()
        for row in self.status_data:
            if row[1] == self.ui.comboBox_EmployeeStatusID.currentText():
                status = row[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Employee (FIRST_NAME, MIDDLE_NAME, LAST_NAME, ADDRESS_1, ADDRESS_2,"
                       " CITY, STATE_PROVINCE_ID, POSTAL_CODE, COUNTRY_ID, DATE_OF_BIRTH, EMPLOYEE_STATUS_ID,"
                       " IS_DELETE) VALUES (?,?,?,?,?,?,?,?,?,?,?,0)", first_name, lastname, address_1, address_2, city,
                       state_code, postal_code, country, dob, status)
        cnxn.commit()

    def clear_form(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setStyleSheet("QMessageBox{background-color:white;}")
        message = msgbox.question(self, 'Clear Form', 'Are you sure you want to clear this form?',
                                  msgbox.StandardButtons.Yes | msgbox.StandardButtons.No)
        if message == msgbox.StandardButtons.Yes:
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
        else:
            msgbox.close()


# STATUS
class EmployeeDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_EmployeeStatus()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_employee_detail_list()
        self.ui.comboBox_SelectStatus.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data())

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Employee_Status WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_employee_detail_list(self):
        statuses = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    statuses.append(name)
        self.ui.comboBox_SelectStatus.addItems(statuses)

    def get_data(self):
        selected_name = self.ui.comboBox_SelectStatus.currentText()
        status_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                status_details.append(row)
        return status_details

    def display_data(self):
        status_details = self.get_data()
        for row in status_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_StatusDescription.setText(item)

    def update_data(self):
        status_details = self.get_data()
        status_details[0][1] = self.ui.lineEdit_StatusDescription.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Employee_Status SET DESCRIPTION = ? WHERE EMPLOYEE_STATUS_ID = ?",
                       status_details[0][1], status_details[0][0])
        cnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_employee_detail_list()

    def delete_data(self):
        status_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Employee_Status SET IS_DELETE = 1 WHERE EMPLOYEE_STATUS_ID = ?",
                       status_details[0][0])
        cnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_employee_detail_list()

    def add_data(self):
        insert_data = self.ui.lineEdit_EnterNewStatus.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Employee_Status (DESCRIPTION, IS_DELETE) VALUES (?, 0)",
                       insert_data)
        cnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_employee_detail_list()
        self.ui.lineEdit_EnterNewStatus.clear()


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
        employee_names = []
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


# ==> DISTRIBUTOR FORMS CLASSES
# todo: Test this form
class NewDistributorForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewDistributorForm()
        self.ui.setupUi(self)
        self.status_data = self.load_data()[0]
        self.state_data = self.load_data()[1]
        self.display_data()
        self.ui.save_Button.clicked.connect(self.add_data)
        self.ui.delete_Button.clicked.connect(self.clear_form)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Distributor_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM State_Province WHERE IS_DELETE = 0')
        state_data = [[item for item in row] for row in data]
        return status_data, state_data

    def display_data(self):
        status_list = []
        for status in self.status_data:
            status_list.append(status[1])
        states = []
        for state in self.state_data:
            states.append(state[1])
        state_list = sorted(states)
        self.ui.comboBox_state.addItems(state_list)
        self.ui.comboBox_disstat.addItems(status_list)

    def add_data(self):
        dis_name = self.ui.lineEdit_DisName.text()
        address = self.ui.lineEdit_DisAddress.text()
        city = self.ui.lineEdit_DisCity.text()
        postal_code = self.ui.lineEdit_postalcode.text()
        state_code = int()
        status_code = int()
        for row in self.state_data:
            if row[1] == self.ui.comboBox_state.currentText():
                state_code = row[0]
        for row in self.status_data:
            if row[1] == self.ui.comboBox_disstat.currentText():
                status_code = row[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Distributor (DIS_NAME, WAREHOUSE_ADDRESS, CITY, STATE_PROVINCE_ID, POSTAL_CODE, "
                       "DIS_STATUS_ID, IS_DELETE) VALUES (?,?,?,?,?,?,0)", dis_name, address, city, int(postal_code),
                       state_code, status_code)
        cnxn.commit()

    def clear_form(self):
        self.ui.lineEdit_DisName.clear()
        self.ui.lineEdit_postalcode.clear()
        self.ui.lineEdit_DisCity.clear()
        self.ui.lineEdit_DisAddress.clear()


class NewDistributorContact(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewDistributorContact()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.man_data = self.load_data()
        self.display_data()

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Distributor WHERE IS_DELETE = 0')
        manufacturer_data = [[item for item in row] for row in data]
        return manufacturer_data

    def display_data(self):
        manu_names = []
        for name in self.man_data:
            manu_names.append(name[1])
        self.ui.comboBox_manu.addItems(manu_names)

    def add_data(self):
        mc_name = self.ui.lineEdit_DisName.text()
        mc_number = self.ui.lineEdit_DisCN.text()
        mc_email = self.ui.lineEdit_email.text()
        manu_id = int()
        for row in self.man_data:
            if row[1] == self.ui.comboBox_manu.currentText():
                manu_id = row[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Distributor_Contact (DC_NAME, CONTACT_NUMBER, EMAIL, DISTRIBUTOR_ID, IS_DELETE)"
                       " VALUES (?,?,?,?,0)", mc_name, mc_number, mc_email, manu_id)
        cnxn.commit()

    def clear_form(self):
        self.ui.lineEdit_DisName.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_DisCN.clear()

# Fully Functional
class DistributorContactForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorContactForm()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        self.dis_data = self.load_data()[1]
        self.set_dislist()
        self.ui.selectButton_SelectDis.clicked.connect(self.set_discon)
        self.ui.comboBox_contact.currentIndexChanged.connect(self.display_data)
        self.ui.save_Button_DC.clicked.connect(self.update_data)
        self.ui.delete_Button_DC.clicked.connect(self.delete_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Distributor_Contact WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Distributor WHERE IS_DELETE = 0 ')
        dis_data = [[item for item in row] for row in data]
        return table_data, dis_data

    def set_dislist(self):
        dis_names = []
        for row in self.dis_data:
            for i, name in enumerate(row):
                if i == 1:
                    dis_names.append(name)
        self.ui.comboBox_selectDis.addItems(dis_names)

    def set_discon(self):
        self.ui.comboBox_contact.clear()
        selected_dis = self.ui.comboBox_selectDis.currentText()
        dis_details = []
        for i, row in enumerate(self.dis_data):
            if row[1] == selected_dis:
                dis_details.append(row)
        discon_names = []
        for i, row in enumerate(self.table_data):
            if row[4] == dis_details[0][0]:
                discon_names.append(row[1])
        self.ui.comboBox_contact.addItems(discon_names)

    def get_data(self):
        selected_con = self.ui.comboBox_contact.currentText()
        contact_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_con:
                contact_details.append(row)
        return contact_details

    def display_data(self):
        contact_details = self.get_data()
        for row in contact_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_DisName.setText(item)
                elif i == 2:
                    self.ui.lineEdit_DisCN.setText(item)
                elif i == 3:
                    self.ui.lineEdit_email.setText(item)

    def update_data(self):
        contact_details = self.get_data()
        contact_name = self.ui.lineEdit_DisName.text()
        contact_number = self.ui.lineEdit_DisCN.text()
        contact_email = self.ui.lineEdit_email.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Distributor_Contact SET DC_NAME = ?, CONTACT_NUMBER = ?, EMAIL = ?, DISTRIBUTOR_ID = ?,"
                       " IS_DELETE = 0 WHERE DIS_CONTACT_ID = ?", contact_name, contact_number, contact_email,
                       contact_details[0][4], contact_details[0][0])
        cnxn.commit()
        self.table_data = self.load_data()[0]

    def delete_data(self):
        contact_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Distributor_Contact SET IS_DELETE = 1 WHERE DIS_CONTACT_ID = ?", contact_details[0][0])
        cnxn.commit()
        self.table_data = self.load_data()[0]


# Fully Functional
# idea: change the warehouse address line edit to a Plain Text
class DistributorDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorDetails()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        self.status_data = self.load_data()[1]
        self.state_data = self.load_data()[2]
        self.set_dislist()
        self.display_data()
        self.ui.selectButton.clicked.connect(self.display_data)
        self.ui.save_Button.clicked.connect(self.update_data)
        self.ui.delete_Button.clicked.connect(self.delete_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Distributor WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Distributor_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM State_Province WHERE IS_DELETE = 0')
        state_data = [[item for item in row] for row in data]
        return table_data, status_data, state_data

    def set_dislist(self):
        dis_names = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    dis_names.append(name)
        self.ui.comboBox_disname.addItems(dis_names)
        status_list = []
        for status in self.status_data:
            status_list.append(status[1])
        states = []
        for state in self.state_data:
            states.append(state[1])
        state_list = sorted(states)
        self.ui.comboBox_state.addItems(state_list)
        self.ui.comboBox_disstat.addItems(status_list)

    def get_data(self):
        selected_name = self.ui.comboBox_disname.currentText()
        dis_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                dis_details.append(row)
        return dis_details

    def display_data(self):
        dis_details = self.get_data()
        for row in dis_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_DisName.setText(item)
                elif i == 2:
                    self.ui.lineEdit_DisAddress.setText(item)
                elif i == 3:
                    self.ui.lineEdit_DisCity.setText(item)
                elif i == 4:
                    for state in self.state_data:
                        if state[0] == item:
                            self.ui.comboBox_state.setCurrentIndex(item-1)
                elif i == 5:
                    self.ui.lineEdit_postalcode.setText(str(item))
                elif i == 6:
                    for status in self.status_data:
                        if status[0] == item:
                            self.ui.comboBox_disstat.setCurrentIndex(item-1)

    def delete_data(self):
        dis_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Distributor SET IS_DELETE = 1 WHERE DISTRIBUTOR_ID = ?", dis_details[0][0])
        cnxn.commit()
        # Re-query Table Data
        self.ui.comboBox_disname.clear()
        self.table_data = self.load_data()[0]
        self.set_dislist()

    def update_data(self):
        dis_details = self.get_data()
        dis_name = self.ui.lineEdit_DisName.text()
        dis_addr = self.ui.lineEdit_DisAddress.text()
        dis_city = self.ui.lineEdit_DisCity.text()
        state_code = int()
        postal_code = self.ui.lineEdit_postalcode.text()
        status_id = int()
        for state in self.state_data:
            if state[1] == self.ui.comboBox_state.currentText():
                state_code = state[0]
        for status in self.status_data:
            if status[1] == self.ui.comboBox_disstat.currentText():
                status_id = status[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Distributor SET DIS_NAME = ?, WAREHOUSE_ADDRESS = ?, CITY = ?, STATE_PROVINCE_ID = ?, "
                       "POSTAL_CODE = ?, DIS_STATUS_ID = ?, IS_DELETE = 0 WHERE DISTRIBUTOR_ID = ?", dis_name, dis_addr,
                       dis_city, state_code, int(postal_code), status_id, dis_details[0][0])
        cnxn.commit()
        # Re-query Table Data
        self.ui.comboBox_disname.clear()
        self.table_data = self.load_data()[0]
        self.set_dislist()


# Fully Functional
class DistributorStatus(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorStatusDetail()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_dis_status_list()
        self.ui.comboBox_select.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Distributor_Status WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_dis_status_list(self):
        statuses = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    statuses.append(name)
        self.ui.comboBox_select.addItems(statuses)

    def get_data(self):
        selected_name = self.ui.comboBox_select.currentText()
        status_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                status_details.append(row)
        return status_details

    def display_data(self):
        status_details = self.get_data()
        for row in status_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_desc.setText(item)

    def update_data(self):
        status_details = self.get_data()
        status_details[0][1] = self.ui.lineEdit_desc.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Distributor_Status SET DIS_DESC = ? WHERE DIS_STATUS_ID = ?",
                       status_details[0][1], status_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_dis_status_list()

    def delete_data(self):  # Logical Delete Only
        status_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Distributor_Status SET IS_DELETE = 1 WHERE DIS_STATUS_ID = ?", status_details[0][0])
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_dis_status_list()

    def add_data(self):
        insert_data = self.ui.lineEdit_new.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Distributor_Status (DIS_DESC, IS_DELETE) VALUES (?, 0)", insert_data)
        cnxn.commit()
        self.ui.comboBox_select.clear()
        self.table_data = self.load_data()
        self.set_dis_status_list()
        self.ui.lineEdit_new.clear()


# ==> MANUFACTURER FORMS CLASSES
# Fully Functional
class NewManufacturerForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewManufacturerForm()
        self.ui.setupUi(self)
        self.status_data = self.load_data()
        self.display_data()
        self.ui.save_Button.clicked.connect(self.add_data)
        self.ui.clear_Button.clicked.connect(self.clear_form)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Manufacturer_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]
        return status_data

    def display_data(self):
        status_list = []
        for status in self.status_data:
            status_list.append(status[1])
        self.ui.comboBox_status.addItems(status_list)

    def add_data(self):
        manu_name = self.ui.lineEdit_man_name.text()
        address = self.ui.lineEdit_man_address.text()
        email = self.ui.lineEdit_email.text()
        number = self.ui.lineEdit_number.text()
        status_code = int()
        for row in self.status_data:
            if row[1] == self.ui.comboBox_status.currentText():
                status_code = row[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Manufacturer (M_NAME, M_ADDRESS, M_EMAIL, M_PHONE, MANUFACTURER_STATUS_ID,"
                       " IS_DELETE) VALUES (?,?,?,?,?,0)", manu_name, address, email, number, status_code)
        cnxn.commit()

    def clear_form(self):
        self.ui.lineEdit_man_name.clear()
        self.ui.lineEdit_man_address.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_number.clear()

# todo: Test this form
class NewManufacturerContactForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewManufacturerContact()
        self.ui.setupUi(self)
        self.man_data = self.load_data()
        self.display_data()

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Manufacturer WHERE IS_DELETE = 0')
        manufacturer_data = [[item for item in row] for row in data]
        return manufacturer_data

    def display_data(self):
        manu_names = []
        for name in self.man_data:
            manu_names.append(name[1])
        self.ui.comboBox_manu.addItems(manu_names)

    def add_data(self):
        mc_name = self.ui.lineEdit_DisName.text()
        mc_number = self.ui.lineEdit_DisCN.text()
        mc_email = self.ui.lineEdit_email.text()
        manu_id = int()
        for row in self.man_data:
            if row[1] == self.ui.comboBox_manu.currentText():
                manu_id = row[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Manufacturer_Contact (MC_NAME, MC_NUMBER, MC_EMAIL, MANUFACTURER_ID, IS_DELETE)"
                       " VALUES (?,?,?,?,0)", mc_name, mc_number, mc_email, manu_id)
        cnxn.commit()

    def clear_form(self):
        self.ui.lineEdit_DisName.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_DisCN.clear()


# todo: Test this form
class ManufacturerContactForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerContactForm()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        self.dis_data = self.load_data()[1]
        self.set_dislist()
        self.ui.selectButton_SelectDis.clicked.connect(self.set_discon)
        self.ui.comboBox_contact.currentIndexChanged.connect(self.display_data)
        self.ui.save_Button_DC.clicked.connect(self.update_data)
        self.ui.delete_Button_DC.clicked.connect(self.delete_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Manufacturer_Contact WHERE IS_DELETE = 0 ')
        table_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Manufacturer WHERE IS_DELETE = 0 ')
        dis_data = [[item for item in row] for row in data]
        return table_data, dis_data

    def set_dislist(self):
        dis_names = []
        for row in self.dis_data:
            for i, name in enumerate(row):
                if i == 1:
                    dis_names.append(name)
        self.ui.comboBox_selectDis.addItems(dis_names)

    def set_discon(self):
        self.ui.comboBox_contact.clear()
        selected_dis = self.ui.comboBox_selectDis.currentText()
        dis_details = []
        for i, row in enumerate(self.dis_data):
            if row[1] == selected_dis:
                dis_details.append(row)
        discon_names = []
        for i, row in enumerate(self.table_data):
            if row[4] == dis_details[0][0]:
                discon_names.append(row[1])
        self.ui.comboBox_contact.addItems(discon_names)

    def get_data(self):
        selected_con = self.ui.comboBox_contact.currentText()
        contact_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_con:
                contact_details.append(row)
        return contact_details

    def display_data(self):
        contact_details = self.get_data()
        for row in contact_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_DisName.setText(item)
                elif i == 2:
                    self.ui.lineEdit_DisCN.setText(item)
                elif i == 3:
                    self.ui.lineEdit_email.setText(item)

    def update_data(self):
        contact_details = self.get_data()
        contact_name = self.ui.lineEdit_DisName.text()
        contact_number = self.ui.lineEdit_DisCN.text()
        contact_email = self.ui.lineEdit_email.text()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Manufacturer_Contact SET MC_NAME = ?, MC_NUMBER = ?, MC_EMAIL = ?, MANUFACTURER_ID = ?,"
                       " IS_DELETE = 0 WHERE MANUFCONTACT_ID = ?", contact_name, contact_number, contact_email,
                       contact_details[0][4], contact_details[0][0])
        cnxn.commit()
        self.table_data = self.load_data()[0]

    def delete_data(self):
        contact_details = self.get_data()
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("UPDATE Manufacturer_Contact SET IS_DELETE = 1 WHERE MANUFCONTACT_ID = ?", contact_details[0][0])
        cnxn.commit()
        self.table_data = self.load_data()[0]


class ManufacturerDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerDetails()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        print(self.table_data)
        self.set_manufacturerlist()
        self.ui.selectButton.clicked.connect(self.display_data())
        self.ui.selectButton.clicked.connect(self.save_data())
        self.ui.selectButton.clicked.connect(self.delete_data())

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
                if i == 1:
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
        selected_name = self.ui.comboBox_SearchManufacturer.currentText()
        manufacturer_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                manufacturer_details.append(row)
        return manufacturer_details

    def save_data(self):
        manufacturer_details = self.get_data()
        manufacturer_details[0][1] = self.ui.lineEdit_ManufacturerName.text()
        manufacturer_details[0][2] = self.ui.lineEdit_ManufacturerAddress.text()
        manufacturer_details[0][3] = self.ui.lineEdit_ManufacturerEmail.text()
        manufacturer_details[0][4] = self.ui.lineEdit_ManufacturerPhone.text()
        manufacturer_details[0][5] = int()
        for row in self.status_data:
            if row[1] == self.ui.comboBox_ManufacturerStatusID.currentText():
                manufacturer_details[0][5] = row[0]
        manufacturerconnection = server_connection()
        cursor = manufacturerconnection.cursor()
        cursor.execute("UPDATE Manufacturer SET M_NAME = ?, M_ADDRESS = ?, M_EMAIL = ?, M_PHONE, MANUFACTURER_STATUS_ID = ? "
                       "WHERE MANUFACTURER_ID = ?", manufacturer_details[0][1], manufacturer_details[0][2], manufacturer_details[0][3],
                       manufacturer_details[0][4], manufacturer_details[0][5],
                       manufacturer_details[0][0])
        manufacturerconnection.commit()
        self.ui.lineEdit_ManufacturerName.clear()
        self.ui.lineEdit_ManufacturerAddress.clear()
        self.ui.lineEdit_ManufacturerEmail.clear()
        self.ui.comboBox_ManufacturerStatusID.clear()
        self.table_data = self.load_data()
        self.set_manufacturerlist()

    def delete_data(self):
        manufacturer_details = self.get_data()
        manufacturerconnection = server_connection()
        cursor = manufacturerconnection.cursor()
        manufacturerconnection.commit()
        self.ui.lineEdit_ManufacturerName.clear()
        self.ui.lineEdit_ManufacturerAddress.clear()
        self.ui.lineEdit_ManufacturerEmail.clear()
        self.ui.comboBox_ManufacturerStatusID.clear()
        self.table_data = self.load_data()[0]
        self.set_manufacturerlist()


class ManufacturerDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerStatus()
        self.ui.setupUi(self)
        self.table_data = self.load_data()[0]
        self.set_manufacturer_status_list()
        self.ui.comboBox_SelectStatus.currentIndexChanged.connect(self.display_data())
        self.ui.addButton.clicked.connect(self.delete_data())
        self.ui.updateButton.clicked.connect(self.update_data())

    @staticmethod
    def load_data(self):
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Manufacturer_Status WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_manufacturer_status_list(self):
        statuses = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    statuses.append(name)
        self.ui.comboBox_SelectStatus.addItems(statuses)

    def get_data(self):
        selected_name = self.ui.comboBox_SelectStatus.currentText()
        status_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                status_details.append(row)
        return status_details

    def display_data(self):
        status_details = self.get_data()
        for row in status_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_StatusDescription.setText(item)

    def update_data(self):
        status_details = self.get_data()
        status_details[0][1] = self.ui.lineEdit_StatusDescription.text()
        manufacturercnxn = server_connection()
        cursor = manufacturercnxn.cursor()
        cursor.execute("UPDATE Manufacturer_Status SET DESCRIPTION = ?, MANUFACTURER_STATUS_ID = ?",
                       status_details[0][1], status_details[0][0])
        manufacturercnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_manufacturer_status_list()

    def delete_data(self):
        status_details = self.get_data()
        manufacturercnxn = server_connection()
        cursor = manufacturercnxn.cursor()
        cursor.execute("UPDATE Manufacturer_Status SET IS_DELETE = 1 WHERE MANUFACTURER_STATUS_ID = ?",
                       status_details[0][0])
        manufacturercnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_manufacturer_status_list()

    def add_data(self):
        insert_data = self.ui.lineEdit_EnterNewStatus.text()
        manufacturercnxn = server_connection()
        cursor = manufacturercnxn.cursor()
        cursor.execute("INSERT INTO Manufacturer_Status (DESCRIPTION, IS_DELETE) VALUES (?, 0)", insert_data)
        manufacturercnxn.commit()
        self.ui.comboBox_SelectStatus.clear()
        self.table_data = self.load_data()
        self.set_manufacturer_status_list()
        self.ui.lineEdit_EnterNewStatus.clear()


# ==> PROMOTION FORMS CLASSES
class NewPromotionForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui =  Ui_NewPromotionForm()
        self.ui.setupUi(self)
        self.season_data = self.load_data()[0]
        self.display_data()
        self.ui.submit_Button.clicked.connect(self.add_data)
        self.ui.clear_button.clicked.connect(self.clear_form)

    def load_data(self):
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Promo_Season WHERE IS_DELETE = 0')
        season_data = [[item for item in row] for row in data]
        return season_data

    def display_data(self):
        season_list = []
        for season in self.season_data:
            season_list.append(season[1])
        self.ui.comboBox_SeasonID.addItems(season_list)

    def add_data(self):
        description = self.ui.lineEdit_PromotionDescription.text()
        discount_amount = self.ui.lineEdit_DiscountAmount.text()
        season_id_code = int()
        for row in self.season_data:
            if row[1] == self.ui.comboBox_SeasonID.currentText():
                season_id_code = row[0]
        cnxn = server_connection()
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO Promotion (DESCRIPTION, DISCOUNT_AMOUNT, SEASON_ID, IS_DELETE)"
                       "VALUES (?, ?, ?, 0)", description, discount_amount, season_id_code)
        cnxn.commit()

    def clear_form(self):
        self.ui.lineEdit_PromotionDescription.clear()
        self.ui.lineEdit_DiscountAmount.clear()



# Promotion
class PromotionDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_PromotionDetails()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        print(self.table_data)
        self.season_data = self.load_data()
        self.set_promotionlist()
        self.ui.selectButton.clicked.connect(self.display_data())
        self.ui.save_Button.clicked.connect(self.save_data())
        self.ui.delete_Button.clicked.connect(self.delete_data())


    @staticmethod
    def load_data():
        cursor = server_connection().cursor

        data = cursor.execute('SELECT * FROM Promotion WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]

        data = cursor.execute('SELECT * FROM Seasonal_ID WHERE IS_DELETE = 0')
        season_data = [[item for item in row] for row in data]

        return table_data, season_data

    def set_promotionlist(self):
        promotion_names = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    promotion_names.append(name)
        self.ui.comboBox_SelectPromotion.addItems(promotion_names)

    def display_data(self):
        selected_names = self.ui.comboBox_SelectPromotion.currentText()
        promotion_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_names:
                promotion_details.append(row)
        for row in promotion_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_PromotionDescription.setText(item)
                elif i == 2:
                    self.ui.lineEdit_DiscountAmount(item)
                elif i == 3:
                    for x, season in enumerate(self.season_data):
                        if season[0] == item:
                            self.ui.comboBox_SeasonID.setCurrentIndex(item-1)
    def get_data(self):
        selected_name = self.ui.comboBox_SelectPromotion.currentText()
        promotion_details = []
        for i, row in enumerate(self.season_data):
            if row[1] == selected_name:
                promotion_details.append(row)
            return promotion_details

    def save_data(self):
        promotion_details = self.get_data()
        promotion_details[0][1] = self.ui.lineEdit_PromotionDescription.text()
        promotion_details[0][1] = self.ui.lineEdit_DiscountAmount.text()
        promotion_details[0][2] = int()
        for row in self.season_data:
            if row[1] == self.ui.comboBox_SeasonID.currentText():
                promotion_details[0][2] = row[0]
        promotionconnection = server_connection()
        cursor = promotionconnection.cursor()
        cursor.execute("UPDATE Promotions SET DESCRIPTION = ?, DISCOUNT_AMOUNT = ?, SEASON_ID = ? WHERE CUSTOMER_PROMO_CODE = ? ",
                       promotion_details[0][1], promotion_details[0][2], promotion_details[0][3], promotion_details[0][0])
        promotionconnection.commit()
        self.ui.lineEdit_PromotionDescription.clear()
        self.ui.lineEdit_DiscountAmount.clear()
        self.ui.comboBox_SeasonID.clear()
        self.table_data = self.load_data()
        self.set_promotionlist()


    def delete_data(self):
        promotion_details = self.get_data()
        promotionconnection = server_connection()
        cursor = promotionconnection.cursor()
        cursor.execute("UPDATE Promotion SET IS_DELETE = 1 WHERE CUSTOMER_PROMO_CODE = ?", promotion_details[0][0])
        promotionconnection.commit()
        self.ui.lineEdit_PromotionDescription.clear()
        self.ui.lineEdit_DiscountAmount.clear()
        self.ui.comboBox_SeasonID.clear()
        self.table_data = self.load_data()[0]
        self.set_promotionlist()


# ==> CHANNEL FORMS CLASSES
class ChannelDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ChannelDetails()
        self.ui.setupUi(self)

# NEW CHANNEL FORM
class ChannelDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewChannelStatusForm()
        self.ui.setupUi(self)
        self.status_data = self.load_data()[0]
        self.display_data()
        self.ui.submit_Button.clicked.connect(self.add_data)
        self.ui.clear_button.clicked.connect(self.clear_form)


    @staticmethod
    def load_data(self):
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Channel_Status WHERE IS_DELETE = 0')
        status_data = [[item for item in row] for row in data]
        return status_data

    def display_data(self):
        status_list = []
        for status in self.status_data:
            status_list.append(status[1])
        self.ui.comboBox_StatusCode.addItems(status_list)

    def add_data(self):
        description = self.ui.lineEdit_ChannelDescription.text()
        status_code = int()
        for row in self.status_data:
            if row[1] == self.ui.comboBox_StatusCode.currentText():
                status_code = row[0]
        cnxn = server.connection()
        cursor = cnxn.cursor(0)
        cursor.execute("INSERT INTO Channel (CHANNEL_DESCRIPTION, CHA_STATUS_CODE,"
                       "IS_DELETE) VALUES (?, ?, 0)", description, status_code)
        cnxn.commit()

    def clear_form(self):
        self.ui.lineEdit_ChannelDescription.clear()

# ==> RETURN CODE
class ReturnCodeDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ReturnCodeStatus()
        self.ui.setupUi(self)
        self.table_data = self.load_data()
        self.set_return_code_list()
        self.ui.comboBox_SelectID.currentIndexChanged.connect(self.display_data)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.deleteButton.clicked.connect(self.delete_data)
        self.ui.updateButton.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Return_Code WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]
        return table_data

    def set_return_code_list(self):
        statuses = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    statuses.append(name)
        self.ui.comboBox_SelectID.addItems(statuses)

    def get_data(self):
        selected_name = self.ui.comboBox_SelectID.currentText()
        status_details = []
        for i, row in enumerate(self.table_data):
            if row[1] == selected_name:
                status_details.append(row)
        return status_details

    def display_data(self):
        status_details = self.get_data()
        for row in status_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_IDDescription.setText(item)

    def update_data(self):
        status_details = self.get_data()
        status_details[0][1] = self.ui.lineEdit_IDDescription.text()
        returncnxn = server_connection()
        cursor = returncnxn.cursor()
        cursor.execute("UPDATE Return_Code SET DESCRIPTION = ? WHERE RETURN_CODE_ID = ?",
                       status_details[0][1], status_details[0][0])
        returncnxn.commit()
        self.ui.comboBox_SelectID.clear()
        self.table_data = self.load_data()
        self.set_return_code_list()

    def delete_data(self):
        status_details = self.get_data()
        returncnxn = server_connection()
        cursor = returncnxn.cursor()
        cursor.execute("UPDATE Return_Code SET IS_DELETE = 1 WHERE RETURN_CODE_ID = ?",
                       status_details[0][0])
        returncnxn.commit()
        self.ui.comboBox_SelectID.clear()
        self.table_data = self.load_data()
        self.set_return_code_list()

    def add_data(self):
        insert_data = self.ui.lineEdit_EnterNewID.text()
        returncnxn = server_connection()
        cursor = returncnxn.cursor()
        cursor.execute("INSERT INTO Return_Code (DESCRIPTION, IS_DELETE) VALUES (?,0)", insert_data)
        returncnxn.commit()
        self.ui.comboBox_SelectID.clear()
        self.table_data = self.load_data()
        self.set_return_code_list()
        self.ui.lineEdit_EnterNewID.clear()



# ==> RESOURCES
def server_connection():
    conn = pyodbc.connect('Driver={SQL Server};'  # Leave this as is
                          'Server=LAPTOP-S6PL64NB;'  # Enter your local Server Name
                          'Database=CIS3365_Local;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    return conn


if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    app.exec()
