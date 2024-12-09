from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DeleteItem:
#Delete Item Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_menuitem_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]"
    btnAddn_xpath = "/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[6]/button[1]"
    btnDelete_item_xpath = "(//button[@title='Delete Item'])[1]"
    btnConfirmation_Yes_xpath ="/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]"
    btnConfirmation_No_xpath ="/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    btnItemDetail_View_InBulk_xpath="//th[@class='expand-cell-header']//img[@alt='plus icon']"
    btnItemDetail_View_Minimize_xpath="//th[@class='expand-cell-header']//img[@alt='minus icon']"
    first_checkbox_xpath="/html[1]/body[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]"
    second_checkbox_xpath="/html[1]/body[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[6]/td[2]/input[1]"
    btn_ItemDelete ="//button[@class='p-0 ms-2 btn btn-link']//body/div[@id='root']/main[1]/div[2]/div[1]/div[1]/div[4]/div[1]/p[1]/button[2]/*[1]"
    
    
#Function to click on various Buttions || Created By: Neha Singh
  
    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkItems_menuitem_xpath).click()
        
    def clickOnDeleteItem(self):
        self.driver.find_element(By.XPATH, self.btnDelete_item_xpath).click()
        
    def clickOnDeleteConfirmation_Yes(self):
        self.driver.find_element(By.XPATH, self.btnConfirmation_Yes_xpath).click()
    
    def clickOnDeleteConfirmation_No(self):
        self.driver.find_element(By.XPATH, self.btnConfirmation_No_xpath).click()
        
    def clickOnItemDetailView_InBulk(self):
        self.driver.find_element(By.XPATH, self.btnItemDetail_View_InBulk_xpath).click()
        
    def clickOnItemDetailView_Minimize(self):
        self.driver.find_element(By.XPATH, self.btnItemDetail_View_Minimize_xpath).click()
        
    def clickOnFirstCheckbox(self):
        self.driver.find_element(By.XPATH, self.first_checkbox_xpath).click()
    
    def clickOnSecondCheckbox(self):
        self.driver.find_element(By.XPATH, self.second_checkbox_xpath).click()
        
    def clickOnAll_ItemDelete(self):
        
        self.driver.find_element(By.XPATH, self.btn_ItemDelete).click()
        
        
        