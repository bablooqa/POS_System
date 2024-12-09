from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DeleteSupplier:
#Delete Item Bottlepos 5.0


    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_Suppliers_xpath = "/html/body/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[10]/div/div/div/div/div[3]/a/span"

   # linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    #linkItems_Suppliers_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]/span[1]"
    btnAddn_xpath = "/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[6]/button[1]"
    btnDelete_supplier_xpath = "(//button[contains(@title,'Delete Supplier')])[1]"
    btnConfirmation_No_xpath ="//button[contains(text(),'No')]"
    btnConfirmation_Yes_xpath ="//button[contains(text(),'Yes, Delete')]"
    
    
    
#Function to click on various Buttons 

    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsMenuSupplier(self):
        self.driver.find_element(By.XPATH, self.linkItems_Suppliers_xpath).click()
        
    def clickOnDeleteSupplier(self):
        self.driver.find_element(By.XPATH, self.btnDelete_supplier_xpath).click()
        
    def clickOnDeleteConfirmation_Yes(self):
        self.driver.find_element(By.XPATH, self.btnConfirmation_Yes_xpath).click()
    
    def clickOnDeleteConfirmation_No(self):
        self.driver.find_element(By.XPATH, self.btnConfirmation_No_xpath).click()
        
        
    # def clickOnItemDelete_InBulk_Checkbox(self):
    #     self.driver.find_element(By.XPATH, self.btnItemDelete_inBulk_checkbox_xpath).click()
        
    # def clickOnAll_ItemDelete(self):
    #     self.driver.find_element(By.XPATH, self.btnAll_ItemDelete).click()