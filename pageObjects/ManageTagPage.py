from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ManageTag:
#Delete Item Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_menuitem_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]"
    btnAddn_xpath = "/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[6]/button[1]"
    refresh_xpath="/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[1]/button[1]"
    btnManageDropDown_xpath="//button[normalize-space()='Manage']"
    btnManageTag_xpath="//a[contains(text(),'Manage Tag')]"
    btnMTAddTag_xpath="//button[normalize-space()='Add Tag']"
    txtMTATTagName_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    btnSaveTagName_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/form[1]/button[1]"
    textSearchTagName_xpath="(//input[@id='search-bar-0'])[2]"    
    clearSearchText_xpath="//button[contains(text(),'Clear')]"
    editTagName_xpath="//tbody/tr[1]/td[2]/div[1]/button[1]"
    txtEditTagName_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/form[1]/div[1]/input[1]"
    btnEditTagPupUp_Cancel__xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/button[1]"
    btnEditTagPupUp_Update_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/form[1]/button[1]"
    btnDeleteTagName_xpath="//tbody/tr[1]/td[2]/div[1]/button[2]"
    btnDeleteTagName_No_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/button[2]"
    btnDeleteTagName_Yes_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/button[1]"
    showingEnteties_Drp_xpath="/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]/button[1]"
    SowingEntetiesSelector_drp_xpath="//a[contains(text(),'All')]"
    btnManageTagDialogBox_Cancle_xpath="/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]"
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
    
    
    
    def clickOnManageTag(self):
        self.driver.find_element(By.XPATH, self.btnManageTag_xpath).click()

    def clickOnMTAddTag(self):
        self.driver.find_element(By.XPATH, self.btnMTAddTag_xpath).click()
    
    def setTagName(self, tagName):
        self.driver.find_element(By.XPATH, self.txtMTATTagName_xpath).send_keys(tagName)
        
    
    def clickOnSaveTagName(self):
        self.driver.find_element(By.XPATH, self.btnSaveTagName_xpath).click()
    
    def setSearchTagName(self, searchTagName):
        self.driver.find_element(By.XPATH, self.textSearchTagName_xpath).send_keys(searchTagName)
    
    def clickOnClearSearchText(self):
        self.driver.find_element(By.XPATH, self.clearSearchText_xpath).click()
        
    def clickOnEditTag(self):
        self.driver.find_element(By.XPATH, self.editTagName_xpath).click()
        
    def setEditTagName(self, editTagName):
        self.driver.find_element(By.XPATH, self.txtEditTagName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEditTagName_xpath).send_keys(editTagName) 
    
    def clickOnEditTag_Cancel(self):
            self.driver.find_element(By.XPATH, self.btnEditTagPupUp_Cancel__xpath).click()
        
    def clickOnEditTag_Update(self):
            self.driver.find_element(By.XPATH, self.btnEditTagPupUp_Update_xpath).click()
    
    def clickOnDeleteTag(self):
            self.driver.find_element(By.XPATH, self.btnDeleteTagName_xpath).click()
    
    def clickOnDeleteTNPupUp_No(self):
            self.driver.find_element(By.XPATH, self.btnDeleteTagName_No_xpath).click()
    
    def clickOnDeleteTNPupup_Yes(self):
            self.driver.find_element(By.XPATH, self.btnDeleteTagName_Yes_xpath).click()
    
    def clickOnShowingEnteties_Drp(self):
            self.driver.find_element(By.XPATH, self.showingEnteties_Drp_xpath).click()       
    
    def clickOnShowingEntetiesSelector_Drp(self):
            self.driver.find_element(By.XPATH, self.SowingEntetiesSelector_drp_xpath).click()         
    
    def clickOnDialogBox_Cancle(self):
            self.driver.find_element(By.XPATH, self.btnManageTagDialogBox_Cancle_xpath).click()


 
            