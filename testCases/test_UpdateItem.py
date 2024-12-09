import random
import string
import time
from turtle import update   

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.UpdateItemPage import UpdateItem
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_004_UpdateItem:
    adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
    username = "admin"
    password = "zapbuild1"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_updateItem(self, setup):
        self.logger.info("***************Test_001_UpdateItem*************")
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
        self.logger.info("*****Starting Update Item Testing*****")
        self.updateItem = UpdateItem(self.driver)
        self.updateItem.clickOnItemsMenu()
        
        
        
        
        
        self.updateItem.clickOnItemsMenuItem() 
        time.sleep(5)
        
        #Clicking on Update Item Icon
        self.updateItem.clickOnItemsUpdate()
        time.sleep(3)
        # self.updateItem.updateItemName('Apple For Testing')
        self.itemname=('Apple','Tomato','Grapes', 'Juice 250ML')
        self.randomitemname=''.join(random.choice(self.itemname)for _ in range(1)) 
        self.updateItem.updateItemName(self.randomitemname)
        
        self.updateItem.updateItemQtyOnHand('1000')
        self.updateItem.updateItemQtyOnHand2('51')
        self.updateItem.updateItemPrice('110')
        self.updateItem.updateItemVendorNo("1234567890")
        self.updateItem.updateItemSKU('540')
        self.updateItem.updateItemUnitPerCase('21')
        self.updateItem.updateItemCaseCostTotal(61)
        self.updateItem.updateItemRpoint(5)
        self.updateItem.updateItemRvalue(4)
        time.sleep(3)
        self.updateItem.updateItemChecked_PL()
        time.sleep(3)

        #Method to Clicking and Updating Options Section data | Created By: Neha Singh
        self.updateItem.updateItemclickOptions()
        self.updateItem.updateItem_Options_DefaultQty('8')
        self.updateItem.updateItem_Options_MinPrice(10)
        self.updateItem.updateItem_Options_VendorItemName("Neha Singh Testing")
        self.updateItem.updateItem_Options_Notes('There is need to add item related notes')
        time.sleep(3)
        self.driver.execute_script("scrollBy(0,600);")
        time.sleep(3)
        self.updateItem.clickkOnUpdate()
        time.sleep(7)
        
        self.driver.close()
        self.logger.info("***************Update Item Test Case Passed*************")
        print("*********Item Updated Successfully.*********")
        
        
        
