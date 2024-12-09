import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


from pageObjects.ManagePromotionsPage import ManagePromotions
from pageObjects.LoginPage import LoginPage
from testCases.test_addItem import randomcodegenerator
from utilities.customLogger import LogGen
from selenium.webdriver.common.keys import Keys

#Class for Manage Promotions Test || Created By: Neha Singh
class Test_00_ManagePromotions:
    adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
    username = "admin"
    password = "zapbuild1"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ManagePromotions(self, setup):
        self.logger.info("***************Test_001_Manage Promotions*************")
        self.driver = setup
        self.driver.get(self.adminURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()

        # waiting for dashboard content to be 
        
        time.sleep(10)

        self.logger.info("*****Login successful*****")
        self.logger.info("*****Starting  Item menue Test*****")
        self.managePromotions = ManagePromotions(self.driver)
        self.managePromotions.clickOnItemsMenu()
        self.managePromotions.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        time.sleep(5)
        self.managePromotions.clickOnRefresh()
        time.sleep(3)

        
        self.managePromotions.clickOnManagePromotions()
        time.sleep(2)
        self.managePromotions.clickOnManagePromotionsDialogBox_Close()
        time.sleep(2)
        self.managePromotions.clickOnManagePromotions()
        time.sleep(2)
        self.managePromotions.clickOnManagePromotionsAddPromotions()
        time.sleep(1)

        
        #General Section of Manage Promotions
        
        self.promotionName = "Ester" +" "+ randomPromotionsName_generator() +" " +"Fest"
        self.managePromotions.clickOnPromotionName(self.promotionName)
        time.sleep(1)
        self.managePromotions.clickOnPromotionType()
        time.sleep(1)
        self.managePromotions.clickOnDrpDownPromotionTypeSelect_Doller_Y_Off_X_Qty()
        time.sleep(1)
        self.managePromotions.clickOnPromotionType()
        time.sleep(2)
        self.managePromotions.clickOnDrpDownPromotionTypeSelect_Per_Y_Off_X_Qty()
        time.sleep(1)
        self.managePromotions.clickOnPromotionType()
        time.sleep(1)
        self.managePromotions.clickOnDrpDownPromotionTypeSelectFixedItemPricelist()
        time.sleep(1)
        self.managePromotions.clickOnPromotionType()
        time.sleep(1)
        self.managePromotions.clickOnDrpDownPromotionTypeSelect_Per_Y_Off_X_Qty()
        time.sleep(1)
        self.managePromotions.clickOnStartDate()
        time.sleep(1)
        self.managePromotions.clickOnstartDateSelectToday()
        time.sleep(1)
        self.managePromotions.clickOnEndDate()
        time.sleep(1)
        self.managePromotions.clickOnEndDateSelect()
        time.sleep(1)
        self.managePromotions.clickDrpDownSelectTax()
        time.sleep(1)
        self.managePromotions.clickDrpDownSelectTaxValue()
        self.managePromotions.clickOnCheckBoxGroupPromotion()
        self.managePromotions.clickOnCheckBoxScanData()
        self.managePromotions.clickOnAdd()
        self.randomQty=randomNumbergenerator()
        self.managePromotions.clickOnBulkSaleQty(self.randomQty)
        self.randomPrice=randomNumbergenerator()
        self.managePromotions.clickOnnumEnterPromotionPrice(self.randomPrice)
        
        time.sleep(1)
        self.managePromotions.clickOnAdd()
        self.randomQty1=randomNumbergenerator()
        self.managePromotions.clickOnBulkSaleQty2(self.randomQty1)
        self.randomPrice1=randomNumbergenerator()
        self.managePromotions.clickOnnumEnterPromotionPrice2(self.randomPrice1)        
        
        time.sleep(1)
        self.managePromotions.clickOnAdd()
        self.randomQty2=randomNumbergenerator()
        self.managePromotions.clickOnBulkSaleQty2(self.randomQty2)
        self.randomPrice2=randomNumbergenerator()
        self.managePromotions.clickOnnumEnterPromotionPrice2(self.randomPrice2) 
        
        time.sleep(2)
        self.managePromotions.clickDeleteQtySection()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection_No()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection()
        self.managePromotions.clickDeleteQtySection_Yes()   
        
        
        #Items Section of Manage Promotions
        time.sleep(2)
        self.managePromotions.clickOnbtnItemsSection()
        self.managePromotions.clickOntxtSearch("APPLE JUICE")
        time.sleep(2)
        self.managePromotions.clickOntxtSearch_Clear()
        
        time.sleep(1)
        self.managePromotions.clickOnAddSelectedItemsToPromotion()
        time.sleep(1)
        self.managePromotions.clickOnAddSelectedItemsToPromotion_Ok()
        time.sleep(2)
        self.managePromotions.clickOnCheckBoxSelectAll()
        self.managePromotions.clickOnAddSelectedItemsToPromotion()
        time.sleep(2)
        self.managePromotions.clickOnItemsInPromotionNameShorting()
        time.sleep(1)
        self.managePromotions.clickOnItemsInPromotionNameShorting()
        time.sleep(1)
        self.managePromotions.clickOnItemsInPromotionNameShorting()
        
        time.sleep(2)
        self.managePromotions.clickOnItemsInPromotionPriceShorting()
        self.managePromotions.clickOnItemsInPromotionPriceShorting()
        time.sleep(1)
        self.managePromotions.clickOnItemsInPromotionPriceShorting()
        time.sleep(1)
        self.managePromotions.clickOnRemoveAll()
        time.sleep(2)
        self.managePromotions.clickOnNoBtn()
        
        self.managePromotions.clickOnRemoveAll()
        time.sleep(2)
        self.managePromotions.clickOnYesBtn()
        time.sleep(2)
        
        
        self.managePromotions.clickOnAddPlusIcon()
        time.sleep(2)
        self.managePromotions.clickOnRemoveAll()
        time.sleep(2)
        self.managePromotions.clickOnNoBtn()
        time.sleep(2)
        self.managePromotions.clickOnRemoveAll()
        time.sleep(2)
        self.managePromotions.clickOnYesBtn()
        time.sleep(1)
        self.managePromotions.clickOnAddPlusIcon()
        
        
        #Categories Section of Manage Promotions Functions
        time.sleep(2)
        self.managePromotions.clickOnCategoriesSection()
        time.sleep(1)
        self.managePromotions.clickOnCategoriesSearch("CategoryGroup337 Name")
        time.sleep(1)
        self.managePromotions.clickOnCategoriesSearchClear()
        time.sleep(1)
        self.managePromotions.clickOnshortCategoriesName()
        time.sleep(1)
        self.managePromotions.clickOnshortCategoriesName()
        time.sleep(1)
        self.managePromotions.clickOnAddCategoryPlusIcon()
        time.sleep(1)
        self.managePromotions.clickOnRemoveCategory()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection_No()
        time.sleep(1)
        self.managePromotions.clickOnRemoveCategory()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection_Yes() 
        time.sleep(1)
        self.managePromotions.clickOnAddSelectedCategoryToPromotion()
        time.sleep(1)
        self.managePromotions.clickOnAddSelectedItemsToPromotion_Ok()
        time.sleep(1)
        self.managePromotions.clickOncheckBoxCategorySelectAll()
        time.sleep(1)
        self.managePromotions.clickOnAddSelectedCategoryToPromotion()
        time.sleep(1)
        self.managePromotions.clickOnshortingCategoriesInPromotion()
        time.sleep(1)
        self.managePromotions.clickOnshortingCategoriesInPromotion()
        time.sleep(2)
        self.managePromotions.clickOnRemoveAll()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection_No()
        time.sleep(1)
        self.managePromotions.clickOnRemoveAll()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection_Yes()
        time.sleep(1)
        self.managePromotions.clickOnAddCategoryPlusIcon()
        
        
        #Size Section of Manage Promotions Functions
        time.sleep(2)
        self.managePromotions.clickOnbtnSizeTab()
        time.sleep(1)
        self.managePromotions.clickOnSizeSearch('ITEM692ML SIZE-NAME')
        time.sleep(1)
        self.managePromotions.clickOnCategoriesSearchClear()
        time.sleep(1)
        self.managePromotions.clickOnshortSizeName()
        time.sleep(1)
        self.managePromotions.clickOnshortSizeName()
        time.sleep(1)
        self.managePromotions.clickOnAddSizePlusIcon()
        
        #Remove Size
        time.sleep(1)
        self.managePromotions.clickOnRemoveSize()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection_No()
        time.sleep(1)
        self.managePromotions.clickOnRemoveSize()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection_Yes() 
        
        #Add Selected Sizes To Promotion
        self.managePromotions.clickOnAddSelectedSizesToPromotion()
        time.sleep(2)
        self.managePromotions.clickOnSizeOk()
        time.sleep(1)
        self.managePromotions.clickOnCheckBoxAddSelectedAllSizesToPromotion()
        time.sleep(1)
        self.managePromotions.clickOnAddSelectedSizesToPromotion()
        time.sleep(3)
        self.managePromotions.clickOnRemoveAll()
        time.sleep(1)
        
        
        self.managePromotions.clickDeleteQtySection_No()
        time.sleep(1)
        self.managePromotions.clickOnRemoveAll()
        time.sleep(1)
        self.managePromotions.clickDeleteQtySection_Yes() 
        
        time.sleep(1)
        self.managePromotions.clickOnAddSizePlusIcon()
        
        
        
        
        #Tags Section Tab of Manage Promotions Functions
        self.managePromotions.clickOnTagsTab()
        time.sleep(1)
        self.managePromotions.clickOnTagsDrpDown()
        time.sleep(1)
        self.managePromotions.clickOnTagsDrpDownSelector()
        time.sleep(2)
        self.managePromotions.clickOnRemoveTagsOne_By_One()
        
        #Again Adding Tags
        time.sleep(2)
        self.managePromotions.clickOnTagsDrpDown()
        time.sleep(1)
        self.managePromotions.clickOnTagsDrpDownSelector()
        # time.sleep(1)
        # self.managePromotions.clickOnTagsDrpDownSelector()
        time.sleep(1)
        self.managePromotions.clickOnTagsSearch("Neha")
        time.sleep(1)
        self.managePromotions.clickOnremoveTagsAlls()
        
        
        # Tags Adding By Search
        time.sleep(1)
        self.managePromotions.clickOnTagsDrpDown()
        time.sleep(1)
        self.managePromotions.clickOnTagsDrpDownSelector()
        time.sleep(1)
        self.managePromotions.clickOnTagsDrpDownSelector()
        
        time.sleep(2)
        self.managePromotions.clickOnTagsSearch("Neha")
        time.sleep(2) 
        self.managePromotions.clickOnTagsSearch2("Neha")
        time.sleep(2)
        self.managePromotions.clickOnTagsSearch3("Neha")
        
        
        
        
        #Tags Section Tab of Manage Promotions Functions
        time.sleep(1)
        self.managePromotions.clickOnCustomersTab()
        
        
        time.sleep(1)
        # self.managePromotions.pressEnterKey()
        print("*********Manage Promotions General, Items, Categories, Size, Tags, and Customers All Test Passed!**********")
        self.driver.close()
        self.logger.info("***************Manage Promotions General, Items, Categories, Size, Tags, and Customers All Test Passed!*************")


#Random Functions

def randomPromotionsName_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))

#Random Number Genorator

def randomNumbergenerator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))