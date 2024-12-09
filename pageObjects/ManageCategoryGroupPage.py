from multiprocessing.sharedctypes import Value
import time
import zlib
 
# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
 
 
class ManageCategoryGroup:
#Manage Category Group Bottlepos 5.0
   linkItems_menu_xpath = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
   linkItems_Category_xpath = "//span[contains(text(),'Categories')]"
   btnManageCategoryGroup_xpath = "//button[contains(text(),'Manage Category Group')]"
   shortByIDManageCategoryGroup_xpath="/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/table/thead/tr/th[1]"
   shortByNameManageCategoryGroup_xpath="/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/table/thead/tr/th[2]"
   btnEditIcon_xpath="/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/button[1]"
   btnCancel_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/button[1]"
   txtEditCategoryGroup="/html/body/div[5]/div/div/div[2]/form/div[1]/input"
   checkBoxDNSTWebstore_xpath="//input[@id='data']"
   btnUpdate_xpath="//button[contains(text(),'Update')]"
   searchBox_xpath="/html/body/div[3]/div/div/div[2]/div/div[1]/div/label/input"
   clearSearchText_xpath="//button[contains(text(),'Clear')]"
   btnAddNew_xpath="//button[contains(text(),'Add new')]"
   btnCancelEditCategoryGroup_xapth="/html/body/div[5]/div/div/div[3]/button"
   txtAddNewCategoryName_xpath="/html/body/div[5]/div/div/div[2]/form/div[1]/input"
   btnSaveAddNewCategory_xpath="(//button[normalize-space()='Save'])[1]"
   pageLink2click_xpath="//div[contains(@class,'modal-body')]//a[contains(@class,'page-link')][normalize-space()='2']"
   btnNextPage_xpath="//div[contains(@role,'dialog')]//div[contains(@class,'react-bootstrap-table-pagination-list col-md-6 col-xs-6 col-sm-6 col-lg-6')]//li[1]"
   btnPreviousPage_xpath="//div[contains(@role,'dialog')]//div[contains(@class,'react-bootstrap-table-pagination-list col-md-6 col-xs-6 col-sm-6 col-lg-6')]//li[1]"
   drpDownPagination_xpath="//div[contains(@class,'modal-body')]//button[@id='pageDropDown']"
   drpDownSelectPagination10_xpath="//div[contains(@class,'modal-body')]//a[contains(@role,'menuitem')][normalize-space()='10']"
   drpDownSelectPagination20_xpath="//div[contains(@class,'modal-body')]//a[contains(@role,'menuitem')][normalize-space()='20']"
   drpDownSelectPagination100_xpath="//div[contains(@class,'modal-body')]//a[contains(@role,'menuitem')][normalize-space()='100']"
   drpDownSelectPaginationAll_xpath="//div[contains(@class,'modal-body')]//a[contains(@role,'menuitem')][normalize-space()='All']"
   
   
   
   
   def __init__(self, driver):
        self.driver = driver
    # Function to Click on item Menus section
   def clickOnItemsMenu(self):
       self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()
 
    # Function to click on category sections
   def clickOnItemsMenuCategory(self):
       self.driver.find_element(By.XPATH, self.linkItems_Category_xpath).click()
  
   def clickOnManageCategoryGroup(self):
       self.driver.find_element(By.XPATH, self.btnManageCategoryGroup_xpath).click()
  
   def clickOnShortByID(self):
       self.driver.find_element(By.XPATH, self.shortByIDManageCategoryGroup_xpath).click()
   
   
   def clickOnShortByName(self):
       self.driver.find_element(By.XPATH, self.shortByNameManageCategoryGroup_xpath).click()
      
   def clcikOnEditIcon(self):
       self.driver.find_element(By.XPATH, self.btnEditIcon_xpath).click()
   
   def clickOnCancelButton(self):
       self.driver.find_element(By.XPATH, self.btnCancel_xpath).click()
       
   def clickOnEditTextName(self,name):
       self.driver.find_element(By.XPATH, self.txtEditCategoryGroup).clear()
       self.driver.find_element(By.XPATH, self.txtEditCategoryGroup).send_keys(name)
       
   def clickOnDNSTWebstoreCheckBox(self):
           self.driver.find_element(By.XPATH, self.checkBoxDNSTWebstore_xpath).click()   
       
   
   def clickOnUpdateButton(self):
       self.driver.find_element(By.XPATH, self.btnUpdate_xpath).click()
  
   def clickOnSearchBox(self, searchText):
       self.driver.find_element(By.XPATH, self.searchBox_xpath).clear()
       self.driver.find_element(By.XPATH, self.searchBox_xpath).send_keys(searchText)
  
   def clickOnClearSearchText(self):
         self.driver.find_element(By.XPATH, self.clearSearchText_xpath).click()
         
   def clickOnAddNewButton(self):
           self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()
  
   def clickOnCancelEditCategoryGroup(self):
         self.driver.find_element(By.XPATH, self.btnCancelEditCategoryGroup_xapth).click()
  
   def setAddNewText(self, addNewText):
       self.driver.find_element(By.XPATH, self.txtAddNewCategoryName_xpath).send_keys(addNewText)
  
  
  
   def clickOnSaveButtonAddnewCategory(self):
           self.driver.find_element(By.XPATH, self.btnSaveAddNewCategory_xpath).click()
   
   def clickOnpageLink2(self):
           self.driver.find_element(By.XPATH, self.pageLink2click_xpath).click()
  
   def clickOnNextPage(self):
           self.driver.find_element(By.XPATH, self.btnNextPage_xpath).click()
  
   def clickOnPreviousPage(self):
          self.driver.find_element(By.XPATH, self.btnPreviousPage_xpath).click()
          
   def clickOnDrpDownPagination(self):
          self.driver.find_element(By.XPATH, self.drpDownPagination_xpath).click()
          
   def clickOnDrpDownSelectPagination10(self):
          self.driver.find_element(By.XPATH, self.drpDownSelectPagination10_xpath).click()
          

   def clickOnDrpDownSelectPagination20(self):
          self.driver.find_element(By.XPATH, self.drpDownSelectPagination20_xpath).click()
  
  
   def clickOnDrpDownSelectPagination100(self):
              self.driver.find_element(By.XPATH, self.drpDownSelectPagination100_xpath).click()
  
   def clickOnDrpDownSelectPaginationAll(self):
              self.driver.find_element(By.XPATH, self.drpDownSelectPaginationAll_xpath).click()
  
  