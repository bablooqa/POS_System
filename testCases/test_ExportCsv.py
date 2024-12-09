import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.ExportCsvPage import ExportCSV
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen



#Class for ExportCSV File Test || Created By: Neha Singh
class Test_00_ExportCsv:
    adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
    username = "admin"
    password = "zapbuild1"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ManagePromotions(self, setup):
        self.logger.info("***************Test_001_ExportCsv*************")
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
        self.exportCsv = ExportCSV(self.driver)
        self.exportCsv.clickOnItemsMenu()
        self.exportCsv.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        time.sleep(5)
        self.exportCsv.clickOnRefresh()
        time.sleep(3)

        self.exportCsv.clickOnExportCsv()
        time.sleep(5)
        print("*********ExportCsv All Test Passed!*********")
        self.driver.close()
        self.logger.info("***************ExportCsv All Test Passed!*************")


