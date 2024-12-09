import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.DeleteSupplierPage import DeleteSupplier
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen



#Class for Delete Item Test || Created By: Neha Singh
class Test_007_DeleteSupplier:
    adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
    username = "admin"
    password = "zapbuild1"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_DeleteSupplier(self, setup):
        self.logger.info("***************Test_001_Delete Supplier*************")
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
        self.logger.info("*****Starting  Item menu Test*****")
        self.deleteSupplier = DeleteSupplier(self.driver)
        self.deleteSupplier.clickOnItemsMenu()
        time.sleep(2)
        self.deleteSupplier.clickOnItemsMenuSupplier()   
        print("*********Clicked on Suppliers SideBar Menu done*********")
        time.sleep(10)
        self.logger.info("*****Starting Delete Suopplier Button Test*****")
        self.deleteSupplier.clickOnDeleteSupplier()
        print("*********Clicked on Delete Suopplier Button done*********")
        time.sleep(1)
        self.deleteSupplier.clickOnDeleteConfirmation_No()
        print("*********Clicked on Delete Confirmation No! Done*********")
        
        self.logger.info("*****Again Starting Delete Supplier Button Test*****")
        self.deleteSupplier.clickOnDeleteSupplier()
        print("*********Again Clicked on Delete Suopplier Button done*********")

        time.sleep(2)
        self.deleteSupplier.clickOnDeleteConfirmation_Yes()
        time.sleep(7)
        print("*********Clicked on Delete Confirmation Yes!*********")
        self.driver.close()
        self.logger.info("***************Delete Suppliers Clicked On Yes Passed!*************")
        time.sleep(3)
        
        
        
    # #Function to delete Item Confirmation No || Created By: Neha Singh    || Not In Use From Date:30-11-2022 || Updated By: Neha Singh
    # @pytest.mark.sanity
    # @pytest.mark.regression
    # def test_DeleteItem_CleckOn_No(self, setup):
    #     self.logger.info("***************Test_002_Delete Supplier No*************")
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
    #     self.deleteSupplierNo = DeleteSupplier(self.driver)
    #     self.deleteSupplierNo.clickOnItemsMenu()
    #     time.sleep(1)
    #     self.deleteSupplierNo.clickOnItemsMenuSupplier() 
    #     print("*********Clicked on Suppliers Menu done*********")
    #     time.sleep(10)
    #     self.logger.info("*****Starting Delete Supplier Test*****")
    #     self.deleteSupplierNo.clickOnDeleteSupplier()
    #     time.sleep(3)
    #     self.deleteSupplierNo.clickOnDeleteConfirmation_No()
    #     print("*********Clicked on Delete Confirmation No!*********")
    #     self.driver.close()
    #     self.logger.info("***************Delete Item Clicked On No Passed*************")
    #     time.sleep(3)
        
    
    
        
