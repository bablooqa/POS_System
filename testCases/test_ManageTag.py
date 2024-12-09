import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.ManageTagPage import ManageTag
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
        self.manageTag = ManageTag(self.driver)
        self.manageTag.clickOnItemsMenu()
        self.manageTag.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        time.sleep(5)
        self.manageTag.clickOnRefresh()
        time.sleep(3)
        self.manageTag.clickOnManageDropDown()
        time.sleep(3)
        self.manageTag.clickOnManageTag()
        time.sleep(3)
        self.manageTag.clickOnMTAddTag()
        time.sleep(3)
        self.tagName = "Neha" + randomiTagName_generator() + "Tag"
        self.manageTag.setTagName(self.tagName)
        time.sleep(3)
        self.manageTag.clickOnSaveTagName()
        time.sleep(5)
        self.manageTag.setSearchTagName(self.tagName)
        time.sleep(7)
        self.manageTag.clickOnClearSearchText()
        time.sleep(4)
        # self.manageTag.clickOnShowingEnteties_Drp()
        # time.sleep(2)
        # self.manageTag.clickOnShowingEntetiesSelector_Drp()
        # time.sleep(3)

        #clicking on Edit Tag
        self.manageTag.clickOnEditTag()
        time.sleep(3)
        
        #clicking On Cancel Button
        self.manageTag.clickOnEditTag_Cancel()
        time.sleep(2)
        
        #Again Clicking On Edit Tag
        self.manageTag.clickOnEditTag()
        self.tagNameUpdate = "Tag" + randomiTagName_generator() +" "+ "Updated"
        self.manageTag.setEditTagName(self.tagNameUpdate)
        time.sleep(3)
        self.manageTag.clickOnEditTag_Update()
        time.sleep(5)
        self.manageTag.clickOnDeleteTag()
        time.sleep(2)
        self.manageTag.clickOnDeleteTNPupUp_No()
        time.sleep(2)
        self.manageTag.clickOnDeleteTag()
        time.sleep(3)
        self.manageTag.clickOnDeleteTNPupup_Yes()
        time.sleep(3)
        #closing manage Tag
        self.manageTag.clickOnDialogBox_Cancle()

        print("*********Manage Tag All Test Passed!*********")
        self.driver.close()
        self.logger.info("***************Manage Tag All Test Passed!*************")



#Random Functions

def randomiTagName_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))