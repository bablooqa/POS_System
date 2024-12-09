from multiprocessing.sharedctypes import Value
import time
import zlib
 
# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
 
 
class AddSuppliers:
#Add Item Bottlepos 5.0
   linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
   linkItems_Suppliers_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]/span[1]"
   btnAddSupplier_xpath = "//button[normalize-space()='Add Supplier']"
   txtSupplierName_xpath = "//input[contains(@placeholder,'Enter Name ...')]"
   txtSupplierEmail_xpath = "//input[@placeholder='Email']"
   txtSupplierPhone_xpath = "//input[@placeholder='Phone']"
   txtSupplierAddress_xpath = "//input[@placeholder='Address']"
   txtAinvoiceName_xpath = "//input[@placeholder='Autoinvoice Name']"
   txtRepName_xpath = "//input[@placeholder='Rep Name']"
   txtRepPhone_xpath = "//input[@placeholder='Rep Phone']"
   txtAddSupplierNotes_xpath = "//textarea[@placeholder='Notes']"
   btnSaveSupplier_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]"
  
   #Search Added Suppliers name
   inputSupplierNameSearch_xpath="//input[@id='search-bar-0']"
   searchInputTextClear_xpath="//button[@class='btn btn-default clear']"
 
  
   def __init__ (self,driver):
        self.driver = driver
 
   def clickOnItemsMenu(self):
       self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()
 
   def clickOnItemsMenuSuppliers(self):
       self.driver.find_element(By.XPATH, self.linkItems_Suppliers_xpath).click()
  
   def clickOnAddSupplier(self):
       self.driver.find_element(By.XPATH, self.btnAddSupplier_xpath).click()
 
  
   def setSupplierName(self, name):
       self.driver.find_element(By.XPATH, self.txtSupplierName_xpath).send_keys(name)
 
  
   def setSupplierEmail(self, email):
       self.driver.find_element(By.XPATH, self.txtSupplierEmail_xpath).send_keys(email)
      
   def setSupplierPhone(self, phone):
       self.driver.find_element(By.XPATH, self.txtSupplierPhone_xpath).send_keys(phone)
  
   def setSupplierAddress(self, address):
       self.driver.find_element(By.XPATH, self.txtSupplierAddress_xpath).send_keys(address)
  
   def setSupplierAInvoice(self, autoInvoice):
       self.driver.find_element(By.XPATH, self.txtAinvoiceName_xpath).send_keys(autoInvoice)
  
   def setSupplierRepName(self, repName):
       self.driver.find_element(By.XPATH, self.txtRepName_xpath).send_keys(repName)
 
   def setSupplierRepPhone(self, repPhone):
       self.driver.find_element(By.XPATH, self.txtRepPhone_xpath).send_keys(repPhone)
  
   def setSupplierNotes(self, notes):
       self.driver.find_element(By.XPATH, self.txtAddSupplierNotes_xpath).send_keys(notes)
 
   def clickOnSaveButton(self):
       self.driver.find_element(By.XPATH, self.btnSaveSupplier_xpath).click()
       
       #Search Suppliers AddeďItems
   def clickOnSearchInput(self,searchInput):
       self.driver.find_element(By.XPATH, self.inputSupplierNameSearch_xpath).send_keys(searchInput)
   
   def clickOnClearSearchInputButton(self):
       self.driver.find_element(By.XPATH, self.searchInputTextClear_xpath).click()
