import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.ManageItemsSizesPage import ManageItemSize
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen



#Class for Delete Item Test || Created By: Neha Singh
class Test_00_ManageTag:
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
        self.manageItemSize = ManageItemSize(self.driver)
        self.manageItemSize.clickOnItemsMenu()
        self.manageItemSize.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        time.sleep(5)
        self.manageItemSize.clickOnRefresh()
        time.sleep(3)
        self.manageItemSize.clickOnManageDropDown()
        time.sleep(2)
        
        
        self.manageItemSize.clickOnManageItemSizes()
        time.sleep(3)
        self.manageItemSize.clickOnMISAddSize()
        time.sleep(3)
        self.tagName = "Item" + randomiTagName_generator() + "ML"+" "+"Size-Name"
        self.manageItemSize.setSizeName(self.tagName)
        time.sleep(3)
        self.manageItemSize.clickOnSaveSizeName()
        time.sleep(5)
        self.manageItemSize.setSearchSizeName(self.tagName)
        time.sleep(7)
        self.manageItemSize.clickOnClearSearchText()
        time.sleep(4)

        #clicking on Edit Item SIze
        self.manageItemSize.clickOnEditItemSize()
        time.sleep(3)
        
        # clicking On Cancel Button
        self.manageItemSize.clickOnEditItemSIze_Cancel()
        time.sleep(2)
        
        #Again Clicking On Edit Tag
        self.manageItemSize.clickOnEditItemSize()
        self.itemSIzeNameUpdate = "New" + randomiTagName_generator() +"ML"+ "Item"+"Size"
        self.manageItemSize.setEditItemSizeName(self.itemSIzeNameUpdate)
        time.sleep(3)
        self.manageItemSize.clickOnItemSize_Update()
        time.sleep(5)
        self.manageItemSize.clickOnDeleteItemSize()
        time.sleep(2)
        self.manageItemSize.clickOnDeleteITPupUp_No()
        time.sleep(2)
        self.manageItemSize.clickOnDeleteItemSize()
        time.sleep(3)
        self.manageItemSize.clickOnDeleteITPupup_Yes()
        time.sleep(5)
        
        #closing manage Item Size
        self.manageItemSize.clickOnItemSizeDialogBox_Cancle()
        time.sleep(2)
        #closing Windows
        print("*********Manage Tag All Test Passed!*********")
        self.driver.close()
        self.logger.info("***************Manage Tag All Test Passed!*************")



#Random Functions

def randomiTagName_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))