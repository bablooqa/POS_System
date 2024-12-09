import random
import string
import time
from turtle import update
 
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
 
from pageObjects.ManageCategoryGroupPage import ManageCategoryGroup
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen

 
class Test_008_ManageCategoryGroup:
   adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
   username = "admin"
   password = "zapbuild1"
   logger = LogGen.loggen()
 
#  Add Category 

   @pytest.mark.sanity
   @pytest.mark.regression
   def test_AddCategory(self, setup):
       self.logger.info("***************Test_001_ManageCategoryGroup*************")
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
 
       self.logger.info("*****Starting ManageCategoryGroup Testing*****")
 
       self.manageCategoryGroup = ManageCategoryGroup(self.driver)
       self.manageCategoryGroup.clickOnItemsMenu()
       time.sleep(3)
       self.manageCategoryGroup.clickOnItemsMenuCategory()
       time.sleep(3)
       #clicked on ManageCategoryGroup Button
       self.manageCategoryGroup.clickOnManageCategoryGroup()
       time.sleep(3)
    #    Short ByID
       self.manageCategoryGroup.clickOnShortByID()
       self.manageCategoryGroup.clickOnShortByID()
       time.sleep(2)
       self.manageCategoryGroup.clickOnShortByID()
       
       #    Short ByName
       time.sleep(3)
       self.manageCategoryGroup.clickOnShortByName()
       self.manageCategoryGroup.clickOnShortByName()
       time.sleep(2)
       self.manageCategoryGroup.clickOnShortByName()
       time.sleep(3)
       self.manageCategoryGroup.clcikOnEditIcon()
       time.sleep(1)
       self.manageCategoryGroup.clickOnCancelButton()
       time.sleep(2)
       self.manageCategoryGroup.clcikOnEditIcon()
       time.sleep(2)
       
       self.editCategoryGroupName = "Juice" +" "+ randomCategoryGroupName_generator() +" " +"ML"
       self.manageCategoryGroup.clickOnEditTextName(self.editCategoryGroupName)
       self.manageCategoryGroup.clickOnDNSTWebstoreCheckBox()
       time.sleep(2)
       self.manageCategoryGroup.clickOnUpdateButton()
       time.sleep(3)
       #Again Click On Manage category Group
       self.manageCategoryGroup.clickOnManageCategoryGroup()
       time.sleep(3)
       self.manageCategoryGroup.clickOnSearchBox(self.editCategoryGroupName)
       time.sleep(2)
       self.manageCategoryGroup.clickOnClearSearchText()
       time.sleep(2)
       self.manageCategoryGroup.clickOnAddNewButton()
       time.sleep(2)
       self.manageCategoryGroup.clickOnCancelEditCategoryGroup()
       time.sleep(2)
       self.manageCategoryGroup.clickOnAddNewButton()
       time.sleep(2)
       self.addNewText = "Juice" +" "+ randomCategoryGroupName_generator() +" " +"ML"
       self.manageCategoryGroup.setAddNewText(self.addNewText)
       self.manageCategoryGroup.clickOnDNSTWebstoreCheckBox()
       time.sleep(2)
       self.manageCategoryGroup.clickOnSaveButtonAddnewCategory()
       time.sleep(2)
       self.manageCategoryGroup.clickOnSearchBox(self.addNewText)
       time.sleep(2)
       self.manageCategoryGroup.clickOnClearSearchText()
       time.sleep(2)
       self.manageCategoryGroup.clickOnpageLink2()
       time.sleep(2)
       self.manageCategoryGroup.clickOnNextPage()
       time.sleep(1)
       self.manageCategoryGroup.clickOnNextPage()
       time.sleep(2)
       self.manageCategoryGroup.clickOnPreviousPage()
       time.sleep(1)
       self.manageCategoryGroup.clickOnPreviousPage()
       time.sleep(3)
       self.manageCategoryGroup.clickOnDrpDownPagination()
       time.sleep(2)
       self.manageCategoryGroup.clickOnDrpDownSelectPagination10()
       time.sleep(2)
       self.manageCategoryGroup.clickOnDrpDownPagination()
       self.manageCategoryGroup.clickOnDrpDownSelectPagination20()
       time.sleep(2)
       self.manageCategoryGroup.clickOnDrpDownPagination()
       self.manageCategoryGroup.clickOnDrpDownSelectPagination100()
       time.sleep(2)
       self.manageCategoryGroup.clickOnDrpDownPagination()
       self.manageCategoryGroup.clickOnDrpDownSelectPaginationAll()
       time.sleep(2)
      #  self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       self.last_element = self.driver.find_element(By.XPATH,"//div[contains(@class,'modal-lg modal-dialog-centered')]")
      #  for i in range(5):
      #  self.driver.execute_script("arguments[0].scrollIntoView(true);", self.last_element)
            #   time.sleep(2)
      #  time.sleep(3)
       self.driver.close()
       self.logger.info("***************Manage Category Group tested successfully!*************")
       print("*********Manage Category Group testcase Passed*********")
    
    
       
 
#Random Functions

def randomCategoryGroupName_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))