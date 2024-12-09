from multiprocessing.sharedctypes import Value
import time
import zlib
 
# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
 
 
class AddCategory:
#Add Category Bottlepos 5.0
   linkItems_menu_xpath = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
   linkItems_Category_xpath = "//span[contains(text(),'Categories')]"
   btnAddCategory_xpath = "//button[normalize-space()='Add Category']"
   drpDownCategoryGroup_xpath = "//body/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
   drpDownSelectorCategoryGroup_xpath = "//div[contains(text(),'Beer')]"
   btnAddCategoryGroup_xpath = "//body/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/button[1]"
   btnAddCategoryGroupName_Cancel_xpath = "//body/div[5]/div[1]/div[1]/div[3]/button[1]"
   txtAddCategoryGroupNameForAddGroup_xpath = "//input[@placeholder='Enter Name']"
   checkBoxDNSTWebstore_xpath = "//input[@id='data']"
   btnSaveAddCategoryGroupName = "/html/body/div[5]/div/div/div[2]/form/button"
   txtCategoryGroupName_xpath="//input[@placeholder='Name']"
   drpDownDefaultTax_xpath = "//body/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]"
   drpDownSelectorDefaultTax_xpath = "//div[contains(text(),'GST')]"
   txtAgeVerification_xpath="//input[contains(@placeholder,'Age Verification')]"
   txtDefaultMargin_xpath="//input[@placeholder='Default Margin']"
   checkBoxAllowEBT_xpath="//input[@id='ebt']"
   checkBoxAllowDNDiscount_xpath="//input[@id='discount']"
   checkBoxDoNotShowToWebstore_xpath="//input[@id='webstore']"
   checkBoxExcludeNonCashAdj_xpath="//input[@id='noncashadj']"
   checkBoxExcludeLoyaltyReward_xpath="//input[@id='loyaltyrewards']"
   btnAddCategory_Save_xpath="//button[@type='submit']"
   btnAddCategoryGroup_Cancel_xpath ="//button[normalize-space()='Cancel']"
   
   
   #Update Category XPATH
   editCategoryIcon_xpath="(//button[@title='Edit Category'])[1]"
   editdrpDownSelectorCategoryGroup_xpath = "//div[contains(text(),'Wine')]"
   txtEditCategoryGroupName_xpath="//input[@placeholder='Name']"
   editdrpDownSelectorDefaultTax_xpath = "//div[contains(text(),'High Tax')]"
#    editdrpDownSelectorDefaultTax_xpath="//div[normalize-space()='HighTax']"
   

   #Delete Category Group
   btnDeleteCategoryGroup_xpath="(//img[@alt='Delete'])[1]"
   btnDeleteCategoryGroup_No_xpath="//button[normalize-space()='No']"
   btnDeleteCategoryGroup_Yes_xpath="//button[contains(text(),'Yes, Delete')]"
   
    #Sorting By Id, Name, Group and items XPATH
   shortByIdCategoryGroup_xpath="//thead/tr[1]/th[2]/span[1]"
   shortByNameCategoryGroup_xpath="//thead/tr[1]/th[3]/span[1]"
   shortByGroupCategoryGroup_xpath="//thead/tr[1]/th[4]/span[1]"
   shortByItemsCategoryGroup_xpath="//thead/tr[1]/th[5]/span[1]"
   
   #Pagination XPATH
   drpDownButton_xpath="//button[@id='pageDropDown']"
   drpDownSelectAll_xpath="//body/div[@id='root']/main[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/span[1]/ul[1]/li[5]"
   
   def __init__(self, driver):
        self.driver = driver
    # Function to Click on item Menus section
   def clickOnItemsMenu(self):
       self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()
 
    # Function to click on category sections
   def clickOnItemsMenuCategory(self):
       self.driver.find_element(By.XPATH, self.linkItems_Category_xpath).click()
  
   def clickOnAddCaterogy(self):
       self.driver.find_element(By.XPATH, self.btnAddCategory_xpath).click()
  
   def clickOnDrpDownCategoryGroup(self):
       self.driver.find_element(By.XPATH, self.drpDownCategoryGroup_xpath).click()
   
   
   def setdrpDownSelectorCategoryGroup(self):
       self.driver.find_element(By.XPATH, self.drpDownSelectorCategoryGroup_xpath).click()
      
   def clcikOnAddCategoryGroup_plusIcon(self):
       self.driver.find_element(By.XPATH, self.btnAddCategoryGroup_xpath).click()
   
   def setAddCategoryGroupName(self,addCategoryGroup):
       self.driver.find_element(By.XPATH, self.txtAddCategoryGroupNameForAddGroup_xpath).send_keys(addCategoryGroup)
   
   def clickOnAddCategoryGroupName_CancelButton(self):
       self.driver.find_element(By.XPATH, self.btnAddCategoryGroupName_Cancel_xpath).click()
  
   def clickOnCheckBoxDNSTWebstore(self):
       self.driver.find_element(By.XPATH, self.checkBoxDNSTWebstore_xpath).click()
  
   def clickOnAddCategoryGroupName_SaveButton(self):
         self.driver.find_element(By.XPATH, self.btnSaveAddCategoryGroupName).click()
         
   def setCategoryGroupName(self,categoryGroupName):
           self.driver.find_element(By.XPATH, self.txtCategoryGroupName_xpath).send_keys(categoryGroupName)
  
   def clickOndrpDownDefaultTax(self):
         self.driver.find_element(By.XPATH, self.drpDownDefaultTax_xpath).click()
  
  
   def clickOnSelectorDrpDown(self):
           self.driver.find_element(By.XPATH, self.drpDownSelectorDefaultTax_xpath).click()
   
   def setAgeVerification(self,ageVerification):
           self.driver.find_element(By.XPATH, self.txtAgeVerification_xpath).send_keys(ageVerification)
  
   def setDefaultMargin(self,defaultMargin):
           self.driver.find_element(By.XPATH, self.txtDefaultMargin_xpath).send_keys(defaultMargin)
  
   def clickOnCheckBoxAllowEBT(self):
          self.driver.find_element(By.XPATH, self.checkBoxAllowEBT_xpath).click()
          
   def clickOnCheckBoxDNDiscount(self):
          self.driver.find_element(By.XPATH, self.checkBoxAllowDNDiscount_xpath).click()
          
   def clickOnCheckBoxDoNotShowToWebstore(self):
          self.driver.find_element(By.XPATH, self.checkBoxDoNotShowToWebstore_xpath).click()
  
   def clickOnCheckBoxBoxExcludeNonCashAdj(self):
          self.driver.find_element(By.XPATH, self.checkBoxExcludeNonCashAdj_xpath).click()
  
   def clickOnCheckBoxExcludeLoyaltyReward(self):
          self.driver.find_element(By.XPATH, self.checkBoxExcludeLoyaltyReward_xpath).click()
  
   def clickOnSaveAddCategory(self):
          self.driver.find_element(By.XPATH, self.btnAddCategory_Save_xpath).click()
          
   def clickOnAddCategory_Cancel(self):
          self.driver.find_element(By.XPATH, self.btnAddCategoryGroup_Cancel_xpath).click()
  
  
  #Function to Edit Category  || Created By Neha Singh
  
   def clickOnEditCategoryIcon(self):
          self.driver.find_element(By.XPATH, self.editCategoryIcon_xpath).click()
          
        #Function to change Category group dropdown
    
   def clickOnEditDrpDownCategoryGroup(self):
          self.driver.find_element(By.XPATH, self.editdrpDownSelectorCategoryGroup_xpath).click()     


   def setEditCategoryGroupName(self, editGroupCategoryName):
        self.driver.find_element(By.XPATH, self.txtEditCategoryGroupName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEditCategoryGroupName_xpath).send_keys(editGroupCategoryName)

    
   def clickOnSelectorDrpDownUpdate(self):
           self.driver.find_element(By.XPATH, self.editdrpDownSelectorDefaultTax_xpath).click()
    
    
   def setEditAgeVerification(self,editAgeVerification):
           self.driver.find_element(By.XPATH, self.txtAgeVerification_xpath).clear()
           self.driver.find_element(By.XPATH, self.txtAgeVerification_xpath).send_keys(editAgeVerification)
           
    
   def setEditDefaultMargin(self,editDefaultMargin):
           self.driver.find_element(By.XPATH, self.txtDefaultMargin_xpath).clear()
           self.driver.find_element(By.XPATH, self.txtDefaultMargin_xpath).send_keys(editDefaultMargin)
           

    
    
    # Function to Delete Category
   def clickOnDeleteCategoryGroup(self):
           self.driver.find_element(By.XPATH, self.btnDeleteCategoryGroup_xpath).click()
    
   def clickOnDeleteCategoryGroup_No(self):
           self.driver.find_element(By.XPATH, self.btnDeleteCategoryGroup_No_xpath).click()
           
   def clickOnDeleteCategoryGroup_Yes(self):
           self.driver.find_element(By.XPATH, self.btnDeleteCategoryGroup_Yes_xpath).click()
   
   

    # Function to Shorting
    
   def clickOnShortByID(self):
           self.driver.find_element(By.XPATH, self.shortByIdCategoryGroup_xpath).click()
           
   def clickOnShortByName(self):
           self.driver.find_element(By.XPATH, self.shortByNameCategoryGroup_xpath).click()        
   
   def clickOnShortByGroup(self):
           self.driver.find_element(By.XPATH, self.shortByGroupCategoryGroup_xpath).click() 
           
   def clickOnShortByItems(self):
           self.driver.find_element(By.XPATH, self.shortByItemsCategoryGroup_xpath).click()     
           
           
           
     # Function For Pagination
          
   def clickOnPaginationDrpDown(self):
           self.driver.find_element(By.XPATH, self.drpDownButton_xpath).click()
           
   def clickOnPaginationDrpDownSelectAll(self):
           self.driver.find_element(By.XPATH, self.drpDownSelectAll_xpath).click()     
           