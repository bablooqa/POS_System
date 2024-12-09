from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ManageItemSize:
#Delete Item Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_menuitem_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]"
    btnAddn_xpath = "/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[6]/button[1]"
    refresh_xpath="/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[1]/button[1]"
    btnManageDropDown_xpath="//button[normalize-space()='Manage']"
    btnManageItemSizes_xpath="//a[normalize-space()='Manage Item Sizes']"
    btnMISAddSize_xpath="//button[normalize-space()='Add New']"
    txtMISSizeName_xpath= "/html[1]/body[1]/div[7]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    btnSaveSizeName_xpath="/html[1]/body[1]/div[7]/div[1]/div[1]/div[2]/form[1]/button[1]"
    textSearchManageItemSize_xpath="(//input[contains(@placeholder,'Search')])[2]"   
    clearSearchText_xpath= "//button[contains(text(),'Clear')]"
    
    editItemSizeName_xpath="(//button[contains(@title,'Edit Item Size')])[1]"
    txtEditItemSizeName_xpath="//body[1]/div[7]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    btnEditItemSIzePupUp_Cancel__xpath="//body/div[7]/div[1]/div[1]/div[3]/button[1]"
    btnEditItemSizePupUp_Update_xpath="//body/div[7]/div[1]/div[1]/div[2]/form[1]/button[1]"
    
    
    btnDeleteItemSize_xpath="(//button[contains(@title,'Delete Item Size')])[1]"
    btnDeleteItemSizeName_No_xpath="//button[normalize-space()='No']"
    btnDeleteItemSizeName_Yes_xpath="//button[contains(text(),'Yes')]"
    
    

    btnManageItemSizeDialogBox_Cancle_xpath="//button[normalize-space()='Close']"
#Function to click on various Buttions || Created By: Neha Singh
  
    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkItems_menuitem_xpath).click()
        
        
    def clickOnRefresh(self):
        self.driver.find_element(By.XPATH, self.refresh_xpath).click()
    
    def clickOnManageDropDown(self):
        self.driver.find_element(By.XPATH, self.btnManageDropDown_xpath).click()
    
    def clickOnManageItemSizes(self):
        self.driver.find_element(By.XPATH, self.btnManageItemSizes_xpath).click()

    def clickOnMISAddSize(self):
        self.driver.find_element(By.XPATH, self.btnMISAddSize_xpath).click()
        
        
    
    def setSizeName(self, tagName):
        self.driver.find_element(By.XPATH, self.txtMISSizeName_xpath).send_keys(tagName)
        
    
    def clickOnSaveSizeName(self):
        self.driver.find_element(By.XPATH, self.btnSaveSizeName_xpath).click()
        
    
    def setSearchSizeName(self, searchSizeName):
        self.driver.find_element(By.XPATH, self.textSearchManageItemSize_xpath).send_keys(searchSizeName)
    
    def clickOnClearSearchText(self):
        self.driver.find_element(By.XPATH, self.clearSearchText_xpath).click()
        
    def clickOnEditItemSize(self):
        self.driver.find_element(By.XPATH, self.editItemSizeName_xpath).click()
        
    def setEditItemSizeName(self, editItemSizeName):
        self.driver.find_element(By.XPATH, self.txtEditItemSizeName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEditItemSizeName_xpath).send_keys(editItemSizeName) 
    
    def clickOnEditItemSIze_Cancel(self):
            self.driver.find_element(By.XPATH, self.btnEditItemSIzePupUp_Cancel__xpath).click()
        
    def clickOnItemSize_Update(self):
            self.driver.find_element(By.XPATH, self.btnEditItemSizePupUp_Update_xpath).click()
    
    
    
    def clickOnDeleteItemSize(self):
            self.driver.find_element(By.XPATH, self.btnDeleteItemSize_xpath).click()
    
    def clickOnDeleteITPupUp_No(self):
            self.driver.find_element(By.XPATH, self.btnDeleteItemSizeName_No_xpath).click()
    
    def clickOnDeleteITPupup_Yes(self):
            self.driver.find_element(By.XPATH, self.btnDeleteItemSizeName_Yes_xpath).click()
    
    # def clickOnShowingEnteties_Drp(self):
    #         self.driver.find_element(By.XPATH, self.showingEnteties_Drp_xpath).click()       
    
    # def clickOnShowingEntetiesSelector_Drp(self):
    #         self.driver.find_element(By.XPATH, self.SowingEntetiesSelector_drp_xpath).click()         
    
    def clickOnItemSizeDialogBox_Cancle(self):
            self.driver.find_element(By.XPATH, self.btnManageItemSizeDialogBox_Cancle_xpath).click()


 
            