from multiprocessing.sharedctypes import Value
import time
import zlib


# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class HandleStoreName:  
#Select Store Name Bottlepos 5.0
    drpDownSelectStore_xpath= "/html/body/div/nav[1]/div/div/div/div/div/div/div/div[2]/div"
    # selectStoreName_xpath="//div[normalize-space()='Automation Store']"
    selectStoreName_xpath='/html/body/div/nav[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]'


# Function to Handle Store Name
    def __init__(self, driver):
        self.driver = driver

    #Click on store Drop Down
    def clickOnSelectStoreDrpDown(self):
        self.driver.find_element(By.XPATH, self.drpDownSelectStore_xpath).click()

    #Select Store Name DropDown
    def clickOnSelectStoreName(self):
        self.driver.find_element(By.XPATH, self.selectStoreName_xpath).click()
        
        