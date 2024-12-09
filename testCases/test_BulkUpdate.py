import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


from pageObjects.BulkUpdatePage import BulkUpdate
from pageObjects.LoginPage import LoginPage
from testCases.test_addItem import randomcodegenerator
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys

#Class for BulkUpdate Test || Created By: Neha Singh
class Test_00_BulkUpdate:
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
        self.bulkUpdate = BulkUpdate(self.driver)
        self.bulkUpdate.clickOnItemsMenu()
        self.bulkUpdate.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        time.sleep(5)
        
        self.bulkUpdate.clickOnRefresh()
        time.sleep(3)
        
        #click On Bulk Update Buttton
        self.bulkUpdate.clickOnManageDropDown()
        time.sleep(1)
        self.bulkUpdate.clickOnBulkUpdateButton()
        time.sleep(1)
        self.bulkUpdate.clickOnBulkUpdateBox_Close()
        time.sleep(1)
        self.bulkUpdate.clickOnManageDropDown()
        time.sleep(1)
        self.bulkUpdate.clickOnBulkUpdateButton()
        time.sleep(1)
        self.bulkUpdate.clickOnAdvanceUpdate()
        self.bulkUpdate.clickOnOK()
        
        #Working on Advance Search
        
        self.bulkUpdate.clickOnAdvanceUpdateSearch()
        self.bulkUpdate.clickOnAdvanceUpdateSearch_Cancel()
        self.bulkUpdate.clickOnAdvanceUpdateSearch()
        self.bulkUpdate.setStockCode(9999928212)
        # self.bulkUpdate.setQtyOnHand(500)
        # self.bulkUpdate.setQtyOnHandTo(7)
        self.bulkUpdate.setAdvanceSearchName("Coconut Oil (testing)")
        self.bulkUpdate.setUnitPrice(1)
        self.bulkUpdate.setUnitPriceTo(1000)
        self.bulkUpdate.setMarginInput(1)
        self.bulkUpdate.setMarginToInput(100)
        self.bulkUpdate.setCostInput(1)
        self.bulkUpdate.setCostToInput(6)
        self.bulkUpdate.setVendorItemNo(7777777333)
        self.bulkUpdate.setUnitsPerCase(81)
        self.bulkUpdate.setEnterDefaultQty(50)
        self.bulkUpdate.setEnterSKU(2000)
        self.bulkUpdate.setReorderPoint(10)
        self.bulkUpdate.setReorderValue(15)
        self.bulkUpdate.setVendorName("NEHA TESTING")
        self.bulkUpdate.setMinPrice(50.00)
        time.sleep(1)
        
        
        #Clear Advance Search Inputes to click on Clear Button
        self.bulkUpdate.clickOnAClearAdvanceSearchInputs()
        time.sleep(2)
        
        #Again Filling Advance Search Inputes
        self.bulkUpdate.setStockCode(9999928212)
        # self.bulkUpdate.setQtyOnHand(500)
        # self.bulkUpdate.setQtyOnHandTo(7)
        self.bulkUpdate.setAdvanceSearchName("Coconut Oil (testing)")
        self.bulkUpdate.setUnitPrice(1)
        self.bulkUpdate.setUnitPriceTo(1000)
        self.bulkUpdate.setMarginInput(1)
        self.bulkUpdate.setMarginToInput(100)
        self.bulkUpdate.setCostInput(1)
        self.bulkUpdate.setCostToInput(6)
        self.bulkUpdate.setVendorItemNo(7777777333)
        self.bulkUpdate.setUnitsPerCase(81)
        self.bulkUpdate.setEnterDefaultQty(50)
        self.bulkUpdate.setEnterSKU(2000)
        self.bulkUpdate.setReorderPoint(10)
        self.bulkUpdate.setReorderValue(15)
        self.bulkUpdate.setVendorName("NEHA TESTING")
        time.sleep(1)
        self.bulkUpdate.setMinPrice(50.00)
     
        #Click On Advance Search Button
        time.sleep(2)
        self.bulkUpdate.clickOnAdvanceSearchSubmit()
        
        
        
        # *******Advance Update Functions*******
        # time.sleep(1)
        # self.bulkUpdate.clickOnSearchFilters()
        # time.sleep(1)
        # self.bulkUpdate.clickOnSearchFilters()
        # self.bulkUpdate.clickOnSearch()
        # time.sleep(2)
        # self.bulkUpdate.clickOnRemoveItem()
        # self.bulkUpdate.clickOnRemoveItemConfirmation_No()
        # time.sleep(1)
        # self.bulkUpdate.clickOnRemoveItem()
        # time.sleep(1)
        # self.bulkUpdate.clickOnRemoveItemConfirmation_Yes()
        # time.sleep(1)
        # self.bulkUpdate.clickOnRemoveItemAllItems()
        # self.bulkUpdate.clickOnSearch()
        # time.sleep(1)
        # self.bulkUpdate.clickOnEnterName("Apple")
        # time.sleep(1)
        # self.bulkUpdate.clickOnSearch()
        # time.sleep(2)
        # self.bulkUpdate.clickOnEnterNameClear()
        # time.sleep(1)
        # self.bulkUpdate.clickOnRemoveItemAllItems()
        # time.sleep(2)
        # self.bulkUpdate.clickOnSearch()
        # time.sleep(1)
        # self.bulkUpdate.clickOnEnterUnitPerCase(1000)
        # time.sleep(1)
        # self.bulkUpdate.clickOnEnterUnitPerCaseDownArrow()
        # self.bulkUpdate.clickOnEnterUnitCase(500)
        # self.bulkUpdate.clickOnEnterUnitCostDownArrow()
        # self.bulkUpdate.clickOnEnterUnitPrice(600)
        # time.sleep(1)
        # self.bulkUpdate.clickOnEnterUnitPriceDownArrow()
        # time.sleep(2)
        # self.bulkUpdate.clickOnDrpDownTax()
        # time.sleep(1)
        # self.bulkUpdate.clickOnDrpDownSelectTax()
        # self.bulkUpdate.clickOnTaxDownArrow()
        
        # time.sleep(1)
        # self.bulkUpdate.clickOnSupplierDropDown()
        # self.bulkUpdate.clickOnDropDownSelectSupplier()
        # self.bulkUpdate.clickOnSupplierDownArrow()
        
        # time.sleep(1)
        # self.bulkUpdate.clickOnDropDownCategory()
        # self.bulkUpdate.clickOnDownSelectCategory()
        # self.bulkUpdate.clickOnCategoryDownArrow()
        
        # time.sleep(1)
        # self.bulkUpdate.setEnterReorderPoint(700)
        # self.bulkUpdate.clickOnEnterReorderPointDownArrow()
        
        # time.sleep(1)
        # self.bulkUpdate.setEnterReorderValue(900)
        # self.bulkUpdate.clickOnEnterReorderValue()
        
        # time.sleep(1)
        # self.bulkUpdate.clickOnDropDownSize()
        # self.bulkUpdate.clickOnSelectDropDownSize()
        # self.bulkUpdate.clickOnSizeDownArrow()
        
        
        # time.sleep(1)
        # self.bulkUpdate.clickOnUpdate()
        # time.sleep(3)
        # self.bulkUpdate.clickOnUpdatingBulkItemsDilogBox_Close()
        
        # time.sleep(2)
        # print("*********Bulk Uudate All Test Passed!**********")
        # self.driver.close()
        # self.logger.info("***************Bulk Uudate All Test Passed!*************")
  