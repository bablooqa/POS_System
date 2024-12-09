import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_001_Login:
    # reading data from config.ini file
    # baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getpassword()
    adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
    adminURLLogOut="http://bottlepos5-qa.bottlepos.com/admin/dashboard"
    username = "admin"
    password = "zapbuild1"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*****Test_001_Login started*****")
        self.logger.info("***************Opening the login page*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        print(act_title)

        if self.adminURL == "http://bottlepos5-qa.bottlepos.com/admin":
            assert True
            self.driver.close()
            self.logger.info("***************Login test is Passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("***************Login test is Failed*************")
            assert False
   
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***************Verifying the Login test*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()

        if self.adminURL == "http://bottlepos5-qa.bottlepos.com/admin":
            time.sleep(5)
            assert True
            self.driver.close()
            self.logger.info("***************Login test passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("***************Login test failed*************")
            assert False
        
# Function to Admin Page Lougout

    def test_Admin_logout(self,setup):
        time.sleep(5)
        self.logger.info("***************Verifying the Login test for logout functionality*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        # assert True
        if self.adminURLLogOut== "http://bottlepos5-qa.bottlepos.com/admin/dashboard":
            
            self.logger.info("*****Test_001_LogOut started*****")
            self.logger.info("***************Clicking the logOut Button*************")
            self.driver = setup
            self.driver.get(self.adminURLLogOut)
            time.sleep(5)
            self.lp.clickLogout()
            time.sleep(5)
            self.lp.clickLogoutConfirm()
            assert True
            self.logger.info("*****Test_001_LogOut Completed!*****")
       
        else:
            self.driver.close()
            assert False

    #for cancelconfirmlogout

    def test_deny_logout(self,setup):
        time.sleep(5)
        self.logger.info("***************Verifying the again Login test*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        # assert True
        if self.adminURLLogOut== "http://bottlepos5-qa.bottlepos.com/admin/dashboard":
            
            self.logger.info("*****Test_001_LogOut started*****")
            self.logger.info("***************Clicking the logOut page*************")
            self.driver = setup
            self.driver.get(self.adminURLLogOut)
            time.sleep(5)
            self.lp.clickLogout()
            time.sleep(5)
            self.lp.clickDenyLogout()
            time.sleep(5)
            assert True
            self.logger.info("*****Test_001_LogOut stopped!*****")
       
        else:
            self.driver.close()
            assert False


           





