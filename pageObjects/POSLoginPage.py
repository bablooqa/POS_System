from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class POSLoginPage:
    # login
    txt_username_name = "username"
    txt_password_name = "password"
    # btn_login_xpath = "//button[@id='loginbutton']"

    btn_login_xpath = "//button[@type='submit']"
    btn_logout_xpath = "//a[@title='Logout']"

    # device setup
    btn_device_not_setup_ok_xpath = "/html/body/div[3]/div/div/div[3]/button"
    
    #Initial Device Setup
    #Select an existing store for the device or enter a new store
    selectStore_xpath="/html/body/div[3]/div/div/div[2]/form/div/div[1]/div/div/div/div[2]/div"
    chooseStoreName_xpath="//div[contains(text(),'NEHA STORE')]"
    
    #Select a device to merge with or enter a new device name
    selectDevice_xpath="/html/body/div[3]/div/div/div[2]/form/div/div[2]/div/div/div/div[2]/div"
    chooseDeviceName_xpath="//div[contains(text(),'MOBILE')]"
    
    # Click On Rigister Button
    registerButton_xpath="//button[contains(text(),'Register')]"
    
    #Pax Error Xpath
    heading_pax_alert_xpath="/html/body/div[3]/div/div/div[1]/div"
    btn_pax_ok_xpath="//button[contains(text(),'Ok')]"
    
    #Xpath of POSLogOut Functionality
    clickOnMenuLogout_xpath="//span[contains(text(),'Menu')]"
    clickOnLogOutDrpDown_xpath="//body/div[@id='root']/div[1]/nav[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/a[3]"
    
    # handling Logout Confirmation xPath
    logoutConfirmation_No_xpath="//body/div[3]/div[1]/div[1]/div[3]/button[1]"
    logoutConfirmation_Yes_xpath="//button[contains(text(),'Yes')]"
    
    
    def __init__(self, driver):
        self.driver = driver

    #login Method
    def setUserName(self, username):
        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located((By.NAME, self.txt_username_name)))
        self.driver.find_element(By.NAME, self.txt_username_name).clear()
        self.driver.find_element(By.NAME, self.txt_username_name).send_keys(username)
        
        
    def clearUserNameField(self, clearField1):
        self.driver.find_element(By.NAME, self.txt_username_name).send_keys(clearField1)
        # self.driver.find_element(By.NAME, self.txt_username_name).send_keys(clearField2)
        
        
    

    def setUserPassword(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).clear()
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    # Setup Method l
    def clickOnDeviceNotSetupBtn(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.btn_device_not_setup_ok_xpath).click()


    #Initial Device Setup Function
    
    # def setStoreName(self, store):
    #     devicedrp = Select(self.driver.find_element(By.XPATH, self.selectStore_xpath))
    #     devicedrp.select_by_visible_text(store)
    
    def setStoreName(self):
        self.driver.find_element(By.XPATH, self.selectStore_xpath).click()
        
    def selectStoreName(self):
        self.driver.find_element(By.XPATH, self.chooseStoreName_xpath).click()
        
    #Set Device Name
    def setDeviceName(self):
        self.driver.find_element(By.XPATH, self.selectDevice_xpath).click()
    
    def selectDeviceName(self):
        self.driver.find_element(By.XPATH, self.chooseDeviceName_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.registerButton_xpath).click()

    # handling pax error
    def clickOnPaxErrorOk(self):
        paxheading = self.driver.find_element(By.XPATH, self.heading_pax_alert_xpath).text
        if paxheading == "Pax Initialization Error":
            self.driver.find_element(By.XPATH, self.btn_pax_ok_xpath).click()
        else:
            return

    #Handling Logout Functionality 
    def handlingLogoutMenu(self):
        self.driver.find_element(By.XPATH, self.clickOnMenuLogout_xpath).click()
    
    def clickOnLogOut(self):
        self.driver.find_element(By.XPATH, self.clickOnLogOutDrpDown_xpath).click()
        
    # handling Logout Confirmation
    def clickOnLogOut_logoutConfirmation_No(self):
        self.driver.find_element(By.XPATH, self.logoutConfirmation_No_xpath).click()
        
    def clickOnLogOut_logoutConfirmation_Yes(self):
        self.driver.find_element(By.XPATH, self.logoutConfirmation_Yes_xpath).click()




    # handling Offline alert
    # def clickOfflineOk(self):
    #     offlineheading = self.driver.find_element(By.XPATH, self.heading_offline_alert_xpath).is_Displayed()
    #     print(offlineheading)
    #     if offlineheading == "True":
    #         self.driver.find_element(By.XPATH, self.btn_offliine_ok_xpath).click()
    #     else:
    #         return
