import pytest
import time

from pageObjects.POSLoginPage import POSLoginPage
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class Test_001_POS_Login:
    posURL = "http://bottlepos5-qa.bottlepos.com"
    posURLForLogout="http://bottlepos5-qa.bottlepos.com/pos"
    username = "admin"
    password = "zapbuild1"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_LoginPage(self, setup):           
        self.logger.info("*****Test_006_POS_Login started*****")
        self.logger.info("**************Opening the login page*************")
        self.driver = setup
        self.driver.get(self.posURL)
        self.driver.maximize_window()
        
       

        act_url = self.driver.current_url
        print(act_url,"This is Current URL")

        if act_url == "http://bottlepos5-qa.bottlepos.com/":
            time.sleep(5)
            assert True
            self.driver.close()
            self.logger.info("***************POS Login page launch Passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_poshomePage.png")
            self.driver.close()
            self.logger.info("***************POS Login page launch Failed*************")
            assert False
            
            

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginValidation(self, setup):
        self.logger.info("***************Verifying the POS Login test*************")
        self.driver = setup
        self.driver.get(self.posURL)
        self.driver.maximize_window()
        print(self.driver.get_cookies())
       
        self.posLogin = POSLoginPage(self.driver)
        self.posLogin.clickOnDeviceNotSetupBtn()
        time.sleep(8)
        print("******Handling POSLogin username/Password Validations******")
        #Handling POSLogin username/Password Validations
        
        #  Rigister Button xPath
        # self.registerButton_xpath="//button[contains(text(),'Register')]"
        # self.driver.find_element(By.XPATH, self.registerButton_xpath)
        
        if self.posURL == "http://bottlepos5-qa.bottlepos.com":
            # time.sleep(5)
            
            #Login without Username & Password
            print("Login without Username & Password")
            self.posLogin.clickLogin()
            time.sleep(10)
            
            #Login With Username Only
            print("Login With Username Only")
        
            self.posLogin.setUserName("admin")
            time.sleep(5)
            self.posLogin.clickLogin()
            time.sleep(10)
            
            #Login with Password Only
            print("Login with Password Only")
            time.sleep(3)
            self.posLogin.clearUserNameField(Keys.CONTROL + "a")
            time.sleep(3)
            self.posLogin.clearUserNameField(Keys.DELETE)
            time.sleep(3)
            self.posLogin.setUserPassword("1234567890")
            self.posLogin.clickLogin()
            time.sleep(5)
            
            
            #Login With Invalid Username & Password
            time.sleep(3)
            print("Login With Invalid Username & Password")
            self.posLogin.setUserName("nehaadmin1")
            time.sleep(1)
            self.posLogin.setUserPassword("987654321")
            self.posLogin.clickLogin()
            time.sleep(3)
            
            #Login With Invalid Username & Valid Password
            time.sleep(3)
            print("Login With Invalid Username & Valid Password")
            self.posLogin.setUserName("admin-neha")
            time.sleep(1)
            self.posLogin.setUserPassword("zapbuild1")
            self.posLogin.clickLogin()
            time.sleep(3)
            
            
            #Login With Valid Username & InValid Password
            time.sleep(3)
            print("Login With Valid Username & InValid Password")
            self.posLogin.setUserName("admin")
            time.sleep(1)
            self.posLogin.setUserPassword("zapbuild2")
            self.posLogin.clickLogin()
            time.sleep(3)
            
            
            #Login With Valid Username & Valid Password
            time.sleep(3)
            print("Login With Valid Username & Valid Password")
            self.posLogin.setUserName(self.username)
            time.sleep(1)
            self.posLogin.setUserPassword(self.password)
            self.posLogin.clickLogin()
            time.sleep(3)
            
            assert True
            self.driver.close()
            print("Login Username/Password Validation test passed")
            self.logger.info("***************POS Login Username/Password Validation test passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "postest_loginFailed.png")
            self.driver.close()
            self.logger.info("***************POS Login Username/Password Validation test failed*************")
            assert False
        time.sleep(3)
        

        
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_DeviceSetupLogOut(self, setup):
        self.logger.info("***************Verifying the POS Login test*************")
        self.driver = setup
        self.driver.get(self.posURL)
        self.driver.maximize_window()
        print(self.driver.get_cookies())
       
        self.posLogOut = POSLoginPage(self.driver)
        self.posLogOut.clickOnDeviceNotSetupBtn()
        time.sleep(8)
        print("******Handling POSLogin username/Password Validations******")
        #Handling POSLogin username/Password Validations
        
        if self.posURL == "http://bottlepos5-qa.bottlepos.com":
            # time.sleep(5)
            
            #Login With Username & Password
            # time.sleep(3)
            print("Login With Valid Username & Valid Password")
            self.posLogOut.setUserName(self.username)
            self.posLogOut.setUserPassword(self.password)
            self.posLogOut.clickLogin()
            time.sleep(3)
            assert True
            # self.driver.close()
            print("Login Username/Password Validation test passed")
            self.logger.info("***************POS Login Username/Password Validation test passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "postest_loginWrongCredentials.png")
            self.driver.close()
            self.logger.info("***************Wrong Credentials POS Login Username/Password Validation test failed*************")
            assert False
        time.sleep(3)
        
        
        # self.posLogin.setUserName("hhhhhhhhhhhh")
        
        
        
        # self.posLogin.clickLogin()
        
        if self.posURL == "http://bottlepos5-qa.bottlepos.com":
            #Initial Device Setup
            self.logger.info("***************Initial Device Setup************")
            self.deviceSetup = POSLoginPage(self.driver)
            self.deviceSetup.setStoreName()
            time.sleep(3)
            self.deviceSetup.selectStoreName()
            time.sleep(3)
            self.deviceSetup.setDeviceName()
            time.sleep(3)
            self.deviceSetup.selectDeviceName()
            time.sleep(3)
            self.deviceSetup.clickRegister()
            time.sleep(3)
            assert True
            # self.driver.close()
            print("Device Setup ")
            self.logger.info("***************Device Setup Test Passed*************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "postest_DeviceSetup_Failed.png")
            self.driver.close()
            self.logger.info("***************DeviceSetup  test failed*************")
            assert False
            
            
        time.sleep(3)
        if self.posURLForLogout == "http://bottlepos5-qa.bottlepos.com/pos":    
            #Handling Pax Error
            self.deviceSetup.clickOnPaxErrorOk()
            time.sleep(1)
            #Handing Logout Functionality 
            self.deviceSetup.handlingLogoutMenu()
            time.sleep(1)
            self.deviceSetup.clickOnLogOut()
            time.sleep(3)
            #Handling Logout Confirmation
            self.deviceSetup.clickOnLogOut_logoutConfirmation_No()
            time.sleep(1)
            self.deviceSetup.handlingLogoutMenu()
            time.sleep(1)
            self.deviceSetup.clickOnLogOut()
            time.sleep(3)
            self.deviceSetup.clickOnLogOut_logoutConfirmation_Yes()
            time.sleep(5)
            #closing Driver
            assert True
            self.driver.close()
            self.logger.info("***************POS Logout Test Case Passed Successfully ************")

            
            # self.driver.close()
            print(" Lougout Passed")
            self.logger.info("***************Lougout Test Passed*************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "postest_Lougout_Failed.png")
            self.driver.close()
            self.logger.info("*************** Lougout test failed*************")
            assert False
