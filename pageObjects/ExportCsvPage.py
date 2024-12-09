from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ExportCSV:
#Delete Item Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_menuitem_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]"
    btnAddn_xpath = "/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[6]/button[1]"
    refresh_xpath="/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[1]/button[1]"
    btnExportCsv_xpath="//button[normalize-space()='Export CSV']"
    
    
#Function to click on various Buttions || Created By: Neha Singh
  
    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsMenuItem(self):
        
        self.driver.find_element(By.XPATH, self.linkItems_menuitem_xpath).click()
        
        
    def clickOnRefresh(self):
        self.driver.find_element(By.XPATH, self.refresh_xpath).click()
    
    def clickOnExportCsv(self):
    
        self.driver.find_element(By.XPATH, self.btnExportCsv_xpath).click()

   