import random
import string
import time
from turtle import update
 
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
 
from pageObjects.AddCategoryPage import AddCategory
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen

  
class Test_006_AddCategory:
   adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
   username = "admin"
   password = "zapbuild1"
   logger = LogGen.loggen()
 
#  Add Category 

   @pytest.mark.sanity
   @pytest.mark.regression
   def test_AddCategory(self, setup):
       self.logger.info("***************Test_001_AddCategory*************")
       self.driver = setup
       self.driver.get(self.adminURL)
       self.driver.maximize_window()
 
       self.lp = LoginPage(self.driver)
       self.lp.setUserName(self.username)
       self.lp.setUserPassword(self.password)
       self.lp.clickLogin()
  
       # waiting for dashboard content to be displayed
       time.sleep(10)
       self.logger.info("*****Login successful*****")
 
       self.logger.info("*****Starting AddCategory Testing*****")
 
       self.addCategory = AddCategory(self.driver)
       self.addCategory.clickOnItemsMenu()
       time.sleep(3)
       self.addCategory.clickOnItemsMenuCategory()
       time.sleep(3)
       #clicked on Add Category Button
       self.addCategory.clickOnAddCaterogy()
       #click on Add Category Cancel button
       time.sleep(3)
       self.addCategory.clickOnAddCategory_Cancel()
       time.sleep(3)
       #again Click on Add Category Buttton
       self.addCategory.clickOnAddCaterogy()
       
       time.sleep(3)
       self.logger.info("*****Adding Category Inputs testing*****")
       print("*****Adding Category Inputs testing*****")
 
       self.addCategory.clickOnDrpDownCategoryGroup()
       self.addCategory.setdrpDownSelectorCategoryGroup()
       
       # Click On Add Category Group Plus Icon
       time.sleep(5)
       self.addCategory.clcikOnAddCategoryGroup_plusIcon()
       time.sleep(3)
       self.addCategoryGroupName = "CategoryGroup" + randomCategoryName_generator() + " "+"Name"
       self.addCategory.setAddCategoryGroupName(self.addCategoryGroupName)
       self.addCategory.clickOnCheckBoxDNSTWebstore()
       time.sleep(3)
       self.addCategory.clickOnAddCategoryGroupName_CancelButton()
       
      #  Again Click On Add Category Group Plus Icon
       time.sleep(3)
       self.addCategory.clcikOnAddCategoryGroup_plusIcon()
       time.sleep(3)
       self.addCategoryGroupName = "CategoryGroup" + randomCategoryName_generator() + " "+"Name"
       self.addCategory.setAddCategoryGroupName(self.addCategoryGroupName)
       self.addCategory.clickOnCheckBoxDNSTWebstore()
       time.sleep(3)
       self.addCategory.clickOnAddCategoryGroupName_SaveButton()
       
       time.sleep(5)
       self.addCategoryGroupName = "CategoryGroup" + randomCategoryName_generator() + " "+"Name"
       self.addCategory.setCategoryGroupName(self.addCategoryGroupName)
       self.addCategory.clickOndrpDownDefaultTax()
       self.addCategory.clickOnSelectorDrpDown()
       time.sleep(3)
       
       self.ageVerification = "Age" + randomCategoryName_generator() + " "+"Varification"
       self.addCategory.setAgeVerification(self.ageVerification)
       self.defaultMargin = "default" + randomCategoryName_generator() + " "+"Margin"
       self.addCategory.setDefaultMargin(self.defaultMargin)
       time.sleep(3)
       self.addCategory.clickOnCheckBoxAllowEBT()
       self.addCategory.clickOnCheckBoxDNDiscount()
       self.addCategory.clickOnCheckBoxDoNotShowToWebstore()
       self.addCategory.clickOnCheckBoxBoxExcludeNonCashAdj()
       self.addCategory.clickOnCheckBoxExcludeLoyaltyReward()
       time.sleep(3)
      #  Click On Save Add Category
       self.addCategory.clickOnSaveAddCategory()
       time.sleep(3)
       self.driver.close()
       self.logger.info("***************Add Category Added successfully!*************")
       print("*********Add Category testcase Passed*********")
    
    
       
       
#        #Function to Update Category || Created By: Neha Singh------------------------------------------------

        
   
   @pytest.mark.sanity
   @pytest.mark.regression
   def test_UpdateCategory(self, setup):
       self.logger.info("***************Test_002_UpdateCategory*************")
       self.driver = setup
       self.driver.get(self.adminURL)
       self.driver.maximize_window()
 
       self.lp = LoginPage(self.driver)
       self.lp.setUserName(self.username)
       self.lp.setUserPassword(self.password)
       self.lp.clickLogin()
 
       # waiting for dashboard content to be displayed
       time.sleep(10)
       self.logger.info("*****Login successful*****")
 
       self.logger.info("*****Starting Update Category Testing*****")
       self.updateCategory = AddCategory(self.driver)
       self.updateCategory.clickOnItemsMenu()
       time.sleep(3)
       self.updateCategory.clickOnItemsMenuCategory()
       time.sleep(3)
       self.updateCategory.clickOnEditCategoryIcon()
       time.sleep(3)
       self.updateCategory.clickOnAddCategory_Cancel()
       time.sleep(3)
       self.updateCategory.clickOnEditCategoryIcon()
       time.sleep(3)
       self.updateCategory.clickOnDrpDownCategoryGroup()
       time.sleep(2)
       self.updateCategory.clickOnEditDrpDownCategoryGroup()
       time.sleep(2)
       #Function to generate Group Name
       self.editCategoryGroupName = "Apple" + randomCategoryName_generator() + " "+"Fruits"
       self.updateCategory.setEditCategoryGroupName(self.editCategoryGroupName)
       
       self.updateCategory.clickOndrpDownDefaultTax()
       time.sleep(2)
       self.updateCategory.clickOnSelectorDrpDownUpdate()
       time.sleep(2)
       self.editAgeVarification = "Grapes" + randomCategoryName_generator() + " "+"Fruit"
       self.updateCategory.setEditAgeVerification(self.editAgeVarification)
       self.editDefaultMargin = "Orange" + randomCategoryName_generator() + " "+"Fruit"
       self.updateCategory.setEditDefaultMargin(self.editDefaultMargin)
       time.sleep(2)
       self.updateCategory.clickOnCheckBoxAllowEBT()
       self.updateCategory.clickOnCheckBoxDNDiscount()
       self.updateCategory.clickOnCheckBoxDoNotShowToWebstore()
       self.updateCategory.clickOnCheckBoxBoxExcludeNonCashAdj()
       self.updateCategory.clickOnCheckBoxExcludeLoyaltyReward()
       time.sleep(3)
       self.updateCategory.clickOnSaveAddCategory()
       self.driver.close()
       time.sleep(3)
       self.logger.info("***************Update Category Added successfully!*************")
       print("*********Update Category testcase Passed*********")
    
    
    
    
    # Function to Delete Category Group
       
   @pytest.mark.sanity
   @pytest.mark.regression
   def test_DeleteCategory(self, setup):
       self.logger.info("***************Test_004_DeleteCategory*************")
       self.driver = setup
       self.driver.get(self.adminURL)
       self.driver.maximize_window()
 
       self.lp = LoginPage(self.driver)
       self.lp.setUserName(self.username)
       self.lp.setUserPassword(self.password)
       self.lp.clickLogin()
 
       # waiting for dashboard content to be displayed
       time.sleep(10)
       self.logger.info("*****Login successful*****")
 
       self.logger.info("*****Starting Update Category Testing*****")
       self.deleteCategory = AddCategory(self.driver)
       self.deleteCategory.clickOnItemsMenu()
       time.sleep(3)
       self.deleteCategory.clickOnItemsMenuCategory()
       time.sleep(3)
       self.deleteCategory.clickOnDeleteCategoryGroup()
       time.sleep(2)
       self.deleteCategory.clickOnDeleteCategoryGroup_No()
       time.sleep(3)
       self.deleteCategory.clickOnDeleteCategoryGroup()
       time.sleep(3)
       self.deleteCategory.clickOnDeleteCategoryGroup_Yes()
       time.sleep(3)
       self.driver.close()
       time.sleep(3)
       self.logger.info("***************Delete Category Added successfully!*************")
       print("*********Delete Category testcase Passed*********")
       

 # Function to Shorting Category by Id, Name, Group and Items

       
   @pytest.mark.sanity
   @pytest.mark.regression
   def test_ShortingCategory(self, setup):
       self.logger.info("***************Test_004_ShortingCategory*************")
       self.driver = setup
       self.driver.get(self.adminURL)
       self.driver.maximize_window()
 
       self.lp = LoginPage(self.driver)
       self.lp.setUserName(self.username)
       self.lp.setUserPassword(self.password)
       self.lp.clickLogin()
 
       # waiting for dashboard content to be displayed
       time.sleep(10)
       self.logger.info("*****Login successful*****")
 
       self.logger.info("*****Starting Update Category Testing*****")
       self.shortingCategory = AddCategory(self.driver)
       self.shortingCategory.clickOnItemsMenu()
       time.sleep(3)
       self.shortingCategory.clickOnItemsMenuCategory()
       
       #Short By ID
       time.sleep(3)
       self.shortingCategory.clickOnShortByID()
       self.shortingCategory.clickOnShortByID()
       time.sleep(3)
       self.shortingCategory.clickOnShortByID()
       time.sleep(3)

       #Short By Name
       self.shortingCategory.clickOnShortByName()
       self.shortingCategory.clickOnShortByName()
       time.sleep(2)
       self.shortingCategory.clickOnShortByName()
       
       #Short By Group
       time.sleep(3)
       self.shortingCategory.clickOnShortByGroup()
       self.shortingCategory.clickOnShortByGroup()
       time.sleep(2)
       self.shortingCategory.clickOnShortByGroup()
       
       
       #Short By Items
       time.sleep(3)
       self.shortingCategory.clickOnShortByItems()
       self.shortingCategory.clickOnShortByItems()
       time.sleep(2)
       self.shortingCategory.clickOnShortByItems()
       
       
       #checking DropDown Paginantion
       time.sleep(3)
       self.shortingCategory.clickOnPaginationDrpDown()
       time.sleep(2)
       self.shortingCategory.clickOnPaginationDrpDownSelectAll()
       time.sleep(2)
       self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

       
       time.sleep(3)
       self.driver.close()
       self.logger.info("***************Shorting By ID,NAME,GROUP,ITEMS and Clicking Paginantion successfully!*************")
       print("*********Shorting By ID,NAME,GROUP,ITEMS and Clicking Paginantion testcase Passed*********")
    
       
 
#Random Functions

def randomCategoryName_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))