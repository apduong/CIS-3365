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
from OrderStatusDetails import Ui_PaymentDetails  # FIXME: Class name does not match the form name
# ==> Payment Forms
from NewPaymentForm import Ui_NewShipmentForm  # FIXME: Class name does not match the form name
from PaymentDetails import Ui_PaymentDetails
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
from EmployeeDetails import Ui_EmployeeDetails
from EmployeeStatusDetails import Ui_EmployeeStatusDetails
# ==> Distributor Forms
from DistributorContactForm import Ui_DistributorContactForm
from DistributorDetailsForm import Ui_DistributorDetails
from DistributorStatusDetail import Ui_DistributorStatusDetail
# ==> Manufacturer Forms
from ManufacturerContactForm import Ui_ManufacturerContactForm
from ManufacturerDetails import Ui_ManufacturerDetails
from ManufacturerStatusDetails import Ui_ManufacturerStatusDetails
# ==> Promotion Forms
from Promotion import Ui_Promotion  # FIXME: Class name and form name should be more descriptive.. Eg, 'NewPromotion'
from PromotionDetails import Ui_PromotionDetails
# ==> Channel Forms
from ChannelDetailsForm import Ui_ChannelDetails

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
        self.ui.edit_order_status.clicked.connect(self.open_orderstatus)
        # ==> Payment Forms
        self.ui.addPayButton.clicked.connect(self.open_newpayment)
        self.ui.edit_pay_det.clicked.connect(self.open_paymentdetails)
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
        self.ui.edit_empstat.clicked.connect(self.open_employeestatusdetails)
        # ==> Distributor Forms
        self.ui.edit_discon.clicked.connect(self.open_DistributorContactForm)
        self.ui.edit_disdet.clicked.connect(self.open_DistributorDetailsForm)
        self.ui.edit_disstat.clicked.connect(self.open_distributorstatusdetail)
        # ==> Manufacturer Forms
        self.ui.edit_manucon.clicked.connect(self.open_ManufacturerContactForm)
        self.ui.edit_manudet.clicked.connect(self.open_manufacturerdetails)
        self.ui.edit_manustat.clicked.connect(self.open_manufacturerstatusdetails)
        # ==> Promotion Forms
        self.ui.addPromoButton.clicked.connect(self.open_promotion)
        self.ui.edit_promodet.clicked.connect(self.open_promotiondetails)
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
    def open_orderstatus(self):
        self.form = OrderStatusDetails()
        self.form.show()

    # ==> PAYMENT FORMS
    # NEW PAYMENT
    def open_newpayment(self):
        self.form = NewPaymentForm()
        self.form.show()

    # PAYMENT DETAILS
    def open_paymentdetails(self):
        self.form = PaymentDetails()
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
        self.form = EmployeeDetails()
        self.form.show()

    # EMPLOYEE STATUS DETAILS
    def open_employeestatusdetails(self):
        self.form = EmployeeStatusDetails()
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

    def open_distributorstatusdetail(self):
        self.form = DistributorStatus()
        self.form.show()

    # ==> MANUFACTURER FORMS
    # MANUFACTURER CONTACT FORM
    def open_ManufacturerContactForm(self):  # FIXME: Make this function name lower case
        self.form = ManufacturerContactForm()
        self.form.show()

    # MANUFACTURER DETAILS
    def open_manufacturerdetails(self):
        self.form = ManufacturerDetails()
        self.form.show()

    # MANUFACTURER STATUS DETAILS
    def open_manufacturerstatusdetails(self):
        self.form = ManufacturerStatusDetails()
        self.form.show()

    # ==> PROMOTION FORMS
    # PROMOTION
    def open_promotion(self):
        self.form = Promotion()  # FIXME: Class name and form name should be more descriptive.. Eg, 'NewPromotion'
        self.form.show()

    # PROMOTION DETAILS
    def open_promotiondetails(self):
        self.form = PromotionDetails()
        self.form.show()

    # ==> Channel FORMS
    # CHANNEL DETAILS FORM
    def open_ChannelDetailsForm(self):  # FIXME: Make this function name lower case
        self.form = ChannelDetailsForm()
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
class OrderStatusDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_PaymentDetails()
        self.ui.setupUi(self)


# ==> PAYMENT FORMS CLASSES
class NewPaymentForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewShipmentForm()
        self.ui.setupUi(self)


class PaymentDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_PaymentDetails()
        self.ui.setupUi(self)


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


class ProductColorDetail(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ProductColorDetail()
        self.ui.setupUi(self)


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

# FIXME: Try not to commit changes that breaks the entire program
"""""
# ==> EMPLOYEE FORMS CLASSES
class NewEmployeeForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_NewEmployeeForm()
        self.ui.setupUi(self)
        self.load = self.load_data()
        self.table_data = self.load[0]
        self.dis_contactname = self.load[1]
        self.dis_list()
        self.ui.submit_Button_NE.clicked.connect(self.add_data)
        #self.ui.clear_Button_NE.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Employee WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]
        state = cursor.execute('SELECT * FROM State_Province WHERE IS_DELETE = 0')
        state_data = [[item for item in row] for row in state]
        country = cursor.execute('SELECT * FROM Country WHERE IS_DELETE = 0')
        country_data = [[item for item in row]] for row in country]
        edesc = cursor.execute('SELECT * FROM Employee_Status WHERE IS_DELETE = 0')
        e_desc = [[item for item in row]] for row in edesc]
        return table_data , state_data, country_data, e_desc
    
    def display_data(self):
        selected_name = self.ui.comboBox_EState.currentText()
        new_state = []
        for i, row in  enumerate(self.table_data):
            if row[1] == selected_name:
                new_state.append(row)
       # for row in dis_details: 
           #for i, item in enumerate(row):
               # if i == 1:
                   # self.ui.lineEdit_DisName.setText(item)
               # elif i == 2:
                    #self.ui.lineEdit_DisCN.setText(item)
    def add_data(self):
        insert_data =self.lineEdit_EFN.text()
        insert_data1 =self.lineEdit_EMN.text()
        insert_data2=self.lineEdit_ELN.text()
        insert_data3 = self.lineEdit_EAddress1.text()
        insert_data4 = self.lineEdit_EAddress2.text()
        insert_data5 = self.lineEdit_ECity.text()
        insert_data6 = self.comboBox_EState.currentText()
        insert_data7 = self.lineEdit_EPostalCode.text()
        insert_data8 = self.comboBox_ECountry.currentText())
        insert_data9 = self.dateEdit_DOB
        insert_data10 = self.comboBox_EDesc.currentText()
        inser_data11 = 

"""
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
# FIXME: NEEDS TO BE FIXED BASED ON ID
class DistributorContactForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorContactForm()
        self.ui.setupUi(self)
        self.load = self.load_data()
        self.table_data = self.load[0]
        self.dis_contactname = self.load[1]
        self.dis_list()
        self.ui.selectButton_SelectDis.clicked.connect(self.display_data)
        self.ui.save_Button_DC.clicked.connect(self.update_data)

    @staticmethod
    def load_data():
        cursor = server_connection().cursor()
        data = cursor.execute('SELECT * FROM Distributor_Contact WHERE IS_DELETE = 0')
        table_data = [[item for item in row] for row in data]
        data = cursor.execute('SELECT * FROM Distributor WHERE IS_DELETE = 0')
        dis_contactname = [[item for item in row] for row in data]
        return table_data, dis_contactname

    def dis_list(self):
        dis_contact = []
        for row in self.table_data:
            for i, name in enumerate(row):
                if i == 1:
                    dis_contact.append(name)
        self.ui.comboBox_selectDis.addItems(dis_contact)

    def display_data(self):
        selected_name = self.ui.comboBox_selectDis.currentText()
        dis_details = []
        for i, row in  enumerate(self.table_data):
            if row[1] == selected_name:
                dis_details.append(row)
        for row in dis_details:
            for i, item in enumerate(row):
                if i == 1:
                    self.ui.lineEdit_DisName.setText(item)
                elif i == 2:
                    self.ui.lineEdit_DisCN.setText(item)

    def update_data(self):
        selected_name = self.ui.comboBox_selectDis.currentText()
        dis_details = self.ui.lineEdit_DisName.text()
        conn = server_connection()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Distributor_Contact SET DC_NAME = ? WHERE DC_NAME = ?", dis_details, selected_name)
        conn.commit()


class DistributorDetailsForm(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DistributorDetails()
        self.ui.setupUi(self)


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
                          'Server=LAPTOP-S6PL64NB;'  # Enter your local Server Name
                          'Database=CIS3365_Local;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    return conn


if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    app.exec()
