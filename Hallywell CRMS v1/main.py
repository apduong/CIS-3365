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
from NewPaymentForm import Ui_NewShipmentForm   # FIXME: Class name does not match the form name
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
from DistributorDetailsForm import Ui_DistributorDetails
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
        # self.ui.edit_disstat.clicked.connect()  # TODO: Create Distributor Status Form
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


class ManufacturerDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerDetails()
        self.ui.setupUi(self)


class ManufacturerStatusDetails(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ManufacturerStatusDetails()
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
                          'Server=SUMMER\MSSQLSERVER01;'  # Enter your local Server Name
                          'Database=CIS3365_Project;'  # Enter your Database Name
                          'Trusted_Connection=yes;')  # Leave this as is
    return conn


if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    app.exec()
