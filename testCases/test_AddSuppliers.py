import random
import string
import time
from turtle import update
 
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
 
from pageObjects.AddSuppliersPage import AddSuppliers
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
 
 
class Test_006_AddSupplier:
   adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
   username = "admin"
   password = "zapbuild1"
   logger = LogGen.loggen()
 
 
   @pytest.mark.sanity
   @pytest.mark.regression
   def test_AddSuppliers(self, setup):
       self.logger.info("***************Test_001_AddSuppliers*************")
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
 
       self.logger.info("*****Starting AddSuppliers Testing*****")
 
       self.addSuppliers = AddSuppliers(self.driver)
       self.addSuppliers.clickOnItemsMenu()
       time.sleep(3)
       self.addSuppliers.clickOnItemsMenuSuppliers()
       time.sleep(3)
       #clicked on Add Suppliers Button
       self.addSuppliers.clickOnAddSupplier()
 
       time.sleep(3)
       self.logger.info("*****Adding Suppliers Inputs testing*****")
       print("*****Adding Suppliers Inputs testing*****")
       
       self.randomSuppleirName="NehaSuppleir" + randomName_generator()
       self.addSuppliers.setSupplierName(self.randomSuppleirName)
       
       
       self.randomEmail="example" + randomName_generator() + "@gmail.com"
       self.addSuppliers.setSupplierEmail(self.randomEmail)
       
       
       self.rendomMobileNumber=randomNumber_generator()
       self.addSuppliers.setSupplierPhone(self.rendomMobileNumber)
       
       self.randomAddress="New Delhi-110"+ randomName_generator()
       self.addSuppliers.setSupplierAddress(self.randomAddress)
       
       self.randomSupplierAInvoice="Invoice" +randomName_generator()
       self.addSuppliers.setSupplierAInvoice(self.randomSupplierAInvoice)
       
       self.reandomRepName="Rep" + randomName_generator()
       self.addSuppliers.setSupplierRepName(self.reandomRepName)
       
       self.rendomRepPhone=randomNumber_generator()
       self.addSuppliers.setSupplierRepPhone(self.rendomRepPhone)
       time.sleep(1)
       self.addSuppliers.setSupplierNotes("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
       time.sleep(2)
    #    Click on Suppliers Save Button
       self.addSuppliers.clickOnSaveButton()
       time.sleep(5)
       self.addSuppliers.clickOnSearchInput(self.randomSuppleirName)
       time.sleep(3)
       self.addSuppliers.clickOnClearSearchInputButton()
 
 
       time.sleep(5)
       self.driver.close()
       self.logger.info("***************Supplier Added successfully!*************")
       print("*********Add Supplier testcase Passed*********")
 
#Rendom Name generator

def randomName_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))

#Rendom Number generator

def randomNumber_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))