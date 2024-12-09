import random
import string
import time


import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


from pageObjects.ReceiveItemsPage import ReceiveItems
from pageObjects.LoginPage import LoginPage
from testCases.test_addItem import randomcodegenerator
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from testCases.test_addItem import AddItem
from pageObjects.SelectStoreNamePage import HandleStoreName



#Class for BulkUpdate Test || Created By: Neha Singh
class Test_00_ReceiveItem:
    adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
    username = "admin"
    password = "zapbuild1"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ManagePromotions(self, setup):
        self.logger.info("***************Test_001_BulkUpdate*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()

        # waiting for dashboard content to be 
        
        time.sleep(10)

        self.logger.info("*****Login successful*****")
        self.logger.info("*****Starting  Item menue Test*****")
         # Start Handle Store Name******************************************
        self.selectStoreName=HandleStoreName(self.driver)
        
        #Click On select Store Drop dowan
        self.selectStoreName.clickOnSelectStoreDrpDown()
        
        #Click On To Select Store Name
        self.selectStoreName.clickOnSelectStoreName()
        # End Handle Store Name******************************************
        time.sleep(3)
        
        
        self.receiveItems = ReceiveItems(self.driver)
        self.receiveItems.clickOnItemsMenu()
        time.sleep(2)
        # self.recentList = self.driver.find_elements_by_xpath("//div[@class='_2wP_Y']") 

        # for list in recentList:
        #     self.driver.execute_script("arguments[0].scrollIntoView();", list )
        
        time.sleep(2)
        self.receiveItems.clickOnItemsReceive() 
        print("*********Clicked on Receive Menu done & Receive page will open*********")
        time.sleep(5)
        self.receiveItems.clickOnRefresh() 
        time.sleep(3)
        
        #click On Receive Items Buttton
        self.receiveItems.clickOnReceiveItemsButton()
        print("*******Clicked on Receive Items Button********")
        time.sleep(1)
        
        #Click on close button for "No" option.
        self.receiveItems.clickOnCloseReceiveButton()
        print("********Asking for closing of Receive Items page********")
        time.sleep(2)
        self.receiveItems.clickOnNoButton()
        print("*****Clicked on No option for not closing the receiveItems page******")
        time.sleep(1)
        self.receiveItems.clickOnCloseReceiveButton()
        time.sleep(1)
        self.receiveItems.clickOnYesButton()
        self.receiveItems.clickOnReceiveItemsButton()
        time.sleep(1)
        
        #click on Finalize Button
        self.receiveItems.clickOnFinalize()
        self.receiveItems.clickOnInvoiceDetailsErrorOk()
        
        #click on Save For Later
        self.receiveItems.clickOnSaveForlater()
        self.receiveItems.clickOnInvoiceDetailsErrorOk()
        
        
        #Input of Various Otions
        time.sleep(1)
        self.receiveItems.clickOnDrpDownSelectSupplier()
        self.receiveItems.clickOndrpDownSelectSupplierValue()
        
        #Invoice Number input
        self.invoicenumber=randoInvoiceNumberGenerator()
        self.receiveItems.setInvoiceNumberInput(self.invoicenumber)
        self.receiveItems.setInvoiceTotalInput(1000)
        
        
        #Again Click On Finilize and Save for later
        self.receiveItems.clickOnFinalize()
        self.receiveItems.clickOnInvoiceDetailsErrorOk()
        
        self.receiveItems.clickOnSaveForlater()
        self.receiveItems.clickOnInvoiceDetailsErrorOk()
        
        #Search Product Name
        self.receiveItems.setSearchProductNameInput("Rhythm")
        #Press on Enter Key
        time.sleep(2)
        self.receiveItems.clickOnEnterKey()
        
        #Item Details Dialog Box Closing
        self.receiveItems.clickOnClosingItemDetailDialogBox()
        
        time.sleep(3)
        #Step I******************************************************************
        #Search Product Name
        self.receiveItems.setSearchProductNameInput("Apple")
        #Press on Enter Key
        time.sleep(2)
        self.receiveItems.clickOnEnterKey()
        #Filling Input of Items Details
        self.receiveItems.setReceivedCaseInput(600)    
        self.receiveItems.setUnitPerCaseInput(2000)
        self.receiveItems.setTotalCostInput(5)
        self.receiveItems.setCostPerBottleInput(3)
        self.receiveItems.setPriceInput(5)
        self.receiveItems.setMarginInput(4)
        self.receiveItems.setMarkupInput(500)
         #clicking On Save Button
        self.receiveItems.clickOnSaveItemDetails()
        
        time.sleep(3)
        
        
        
        #Step II***********************************************************************
        #Search Product Name
        self.receiveItems.setSearchProductNameInput("LAPTOP")
        #Press on Enter Key
        time.sleep(2)
        self.receiveItems.clickOnEnterKey()
        #Filling Input of Items Details
        self.receiveItems.setReceivedCaseInput(700)    
        self.receiveItems.setUnitPerCaseInput(3000)
        self.receiveItems.setTotalCostInput(5)
        self.receiveItems.setCostPerBottleInput(4)
        self.receiveItems.setPriceInput(3)
        self.receiveItems.setMarginInput(5)
        self.receiveItems.setMarkupInput(600)
        #clicking On Save Button
        self.receiveItems.clickOnSaveItemDetails()
        
        
        time.sleep(3)
        #Checking Already Added item
        #Search Product Name
        self.receiveItems.setSearchProductNameInput("APPLE")
        #Press on Enter Key
        time.sleep(2)
        self.receiveItems.clickOnEnterKey()
        self.receiveItems.clickOnInvoiceDetailsErrorOk()
        time.sleep(1)
        
        #Invoice Date Input
        self.receiveItems.setInvoiceDatePic()
        time.sleep(1)
        self.receiveItems.setInvoiceDateSelect()
        
        #Due Date Picking
        self.receiveItems.setDueDatePic()
        self.receiveItems.setDueDateSelect() 
        
        #Notes Input
        self.receiveItems.setNotes("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ")       
        
        #Add new Items
        self.receiveItems.clickOnAddNewItem()
        
        #set Sctok Code
        self.setStockcodeInput=randoInvoiceNumberGenerator()
        self.receiveItems.setStockCode(self.setStockcodeInput)
        
        #Set Item Name
        self.setItemName="MacBook Pro" + " " + randomitemname_generator()
        self.receiveItems.setItemName(self.setItemName)
        
        #SET Received Case
        self.receivedCase=randomitemname_generator()
        self.receiveItems.setReceivedCase(self.receivedCase)
        
        #Set Price
        self.setItemPrice=randomitemname_generator()
        self.receiveItems.setPrice(self.setItemPrice)
        
        #set Input Vendor Item No  
        self.inputVendorItemNo=randoInvoiceNumberGenerator()
        self.receiveItems.setInputVendorItemNo(self.inputVendorItemNo)
        
        #Click On
        self.receiveItems.clickOnAddItemPlusIcon()
           
        self.myValue=AddItem()
        print(self.myValue())
        
        #Print Details
        # self.receiveItems.clickOnPrint()
        
        #Print Button to Save File
        time.sleep(3)
        # self.receiveItems.clickOnPrintButtonToSaveFile()
        


        
        
        
        
        
#Rendom Function for Invoice Nu generator
def randoInvoiceNumberGenerator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))
        
#Rendom Items Name generator

def randomitemname_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))

        
        