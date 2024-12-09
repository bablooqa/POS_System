import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.DeleteItemPage import DeleteItem
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen



#Class for Delete Item Test || Created By: Neha Singh
class Test_00_DeleteItem:
    adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
    username = "admin"
    password = "zapbuild1"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_DeleteItem_CleckOn_Yes(self, setup):
        self.logger.info("***************Test_001_Delete Item Yes*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()

        # waiting for dashboard content to be displayed
        time.sleep(10)

        self.logger.info("*****Login successful*****")
        self.logger.info("*****Starting  Item menue Test*****")
        self.deleteItemYes = DeleteItem(self.driver)
        self.deleteItemYes.clickOnItemsMenu()
        self.deleteItemYes.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        time.sleep(10)
        self.logger.info("*****Starting Delete Item Test*****")
        self.deleteItemYes.clickOnDeleteItem()
        print("*********Clicked on Delete Items Button done*********")
        time.sleep(3)
        self.deleteItemYes.clickOnDeleteConfirmation_Yes()
        time.sleep(7)
        print("*********Clicked on Delete Confirmation Yes!*********")
        self.driver.close()
        self.logger.info("***************Delete Item Clecked On Yes Passed*************")
        time.sleep(3)
        
        
        
        
    #Function to delete Item Confirmation No || Created By: Neha Singh    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_DeleteItem_CleckOn_No(self, setup):
        self.logger.info("***************Test_002_Delete Item No*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()

        # waiting for dashboard content to be displayed
        time.sleep(10)

        self.logger.info("*****Login successful*****")
        self.logger.info("*****Starting  Item menue Test*****")
        self.deleteItemNo = DeleteItem(self.driver)
        self.deleteItemNo.clickOnItemsMenu()
        
        self.deleteItemNo.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        time.sleep(10)
        self.logger.info("*****Starting Delete Item Test*****")
        self.deleteItemNo.clickOnDeleteItem()
        time.sleep(3)
        self.deleteItemNo.clickOnDeleteConfirmation_No()
        print("*********Clicked on Delete Confirmation No!*********")
        self.driver.close()
        self.logger.info("***************Delete Item Clecked On No Passed*************")
        time.sleep(3)
         
        
    
    
    # Function to Click on to see Bulk Item Details view|| Created By: Neha Singh    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Bulk_ItemDetails(self, setup):
        self.logger.info("***************Test_003_Bulk Item Details Viewing*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()

        # waiting for dashboard content to be displayed
        time.sleep(10)

        self.logger.info("*****Login successful*****")
        self.logger.info("*****Starting  Item menue Test*****")
        self.itemDetailView = DeleteItem(self.driver)
        self.itemDetailView.clickOnItemsMenu()
        
        self.itemDetailView.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        time.sleep(10)
        self.logger.info("*****Bulk Item Details Viewing*****")
        self.itemDetailView.clickOnItemDetailView_InBulk()
        time.sleep(3)
        self.driver.execute_script("scrollBy(0,600);")
        time.sleep(3)
        self.driver.execute_script("scrollBy(0,-600);")
        time.sleep(5)
        print("*********Minimizing Bulk Item View*********")
        self.itemDetailView.clickOnItemDetailView_Minimize()
        time.sleep(5)
        self.driver.close()
        self.logger.info("***************Delete Item Passed*************")
        print("*********Minimizing Bulk Item View Passed!*********")
        
    
    
    
    
    
    
    
    
    # Function to Bulkdelete Item || Created By: Neha Singh
    
    # @pytest.mark.sanity
    # @pytest.mark.regression
    # def test_DeleteItem_Checkbox_InBulk(self, setup):
    #     self.logger.info("***************Test_004_Delete In Bulk*************")
    #     self.driver = setup
    #     self.driver.get(self.adminURL)
    #     self.driver.maximize_window()

    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setUserPassword(self.password)
    #     self.lp.clickLogin()

    #     # waiting for dashboard content to be displayed
    #     time.sleep(10)

    #     self.logger.info("*****Login successful*****")
    #     self.logger.info("*****Starting  Item menue Test*****")
    #     self.deleteItem = DeleteItem(self.driver)
    #     self.deleteItem.clickOnItemsMenu()
    #     self.deleteItem.clickOnItemsMenuItem() 
    #     print("*********Clicked on Items Menu done*********")
    #     time.sleep(10)
    #     self.logger.info("*****Starting Delete Item In Bulk Test*****")
    #     self.deleteItem.clickOnFirstCheckbox()
    #     self.deleteItem.clickOnSecondCheckbox()
    #     print("*********Clicked on Delete Items In Bulk Checkbox Button done*********")
    #     time.sleep(5)
    #     self.deleteItem.clickOnAll_ItemDelete()
    #     # time.sleep(5)
    #     # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #     time.sleep(5)
    #     # print("*********Clicked on Delete Confirmation Yes!*********")
    #     # self.driver.close()
    #     self.logger.info("***************Click On Delete All Item  Passed*************")
    #     time.sleep(3)





