from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class LoginPage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "//button[@type='submit']"
    btn_logout_xpath = "//div[contains(@class,'align-items-center navbar-nav')]//a[contains(@title,'Logout')][normalize-space()='Logout']"
    btn_logoutconfirm_xpath = "//button[@type='submit']"
    btn_denyLogoutconfirm_xpath = "//button[normalize-space()='No']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username1):
        # self.driver.find_element(By.NAME, self.textbox_username_id).send_keys(u'\ue009' + u'\ue003')
        # time.sleep(2)
        # self.webElement= self.driver.find_element(By.NAME, self.textbox_username_id)
        # self.webElement.sendKeys(Keys.CONTROL + "a")
        # self.webElement.sendKeys(Keys.DELETE)
        # StrValue = Keys.chord(Keys.CONTROL, "a")
        # self.l.sendKeys(StrValue)
        # self.l.sendKeys(Keys.DELETE);
        self.driver.find_element(By.NAME, self.textbox_username_id).send_keys(username1)
        
        
        #Celar Username Input Fields
    def clearUserNameField(self, clearField1,clearField2):
        # self.driver.find_element(By.NAME, self.textbox_username_id).send_keys(clearField)
        self.WebElement= self.driver.find_element(By.NAME, self.textbox_username_id)
        self.WebElement.send_keys(clearField1)
        self.WebElement.send_keys(clearField2)
        
        
        

    def setUserPassword(self, password1):
        self.driver.find_element(By.NAME, self.textbox_password_id).send_keys(u'\ue009' + u'\ue003')
        time.sleep(2)
        self.driver.find_element(By.NAME, self.textbox_password_id).send_keys(password1)

    def clickLogin(self): 
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

    def clickLogoutConfirm(self):
        time.sleep(5)

        self.driver.find_element(By.XPATH, self.btn_logoutconfirm_xpath).click()

    
    def clickDenyLogout(self):

        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_denyLogoutconfirm_xpath).click()



