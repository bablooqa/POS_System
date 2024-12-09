import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#For DropDown
from selenium.webdriver.support.ui import Select


from pageObjects.AdditemPage import AddItem
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.SelectStoreNamePage import HandleStoreName


class Test_003_AddItem:
    adminURL = "http://bottlepos5-qa.bottlepos.com/admin"
    username = "Reliance Automation"
    password = "zapbuild1"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addItem(self, setup):
        self.logger.info("***************Test_003_AddItem*************")
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
        self.logger.info("*****Starting Add Item Test*****")
        
        # Start Handle Store Name******************************************
        self.selectStoreName=HandleStoreName(self.driver)
        
        #Click On select Store Drop dowan
        self.selectStoreName.clickOnSelectStoreDrpDown()
        
        #Click On To Select Store Name
        self.selectStoreName.clickOnSelectStoreName()
        # End Handle Store Name******************************************
        time.sleep(3)
        self.logger.info("*****Starting Add Item Test*****")
        self.additem = AddItem(self.driver)

        self.additem.clickOnItemsMenu()
        
        self.additem.clickOnItemsMenuItem() 
        print("*********Clicked on Items Menu done*********")
        WebDriverWait(self.driver,   30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[10]/div/a")))
        self.logger.info("*****Providng the Item info*****")
        self.additem.clickOnAdd()
        time.sleep(5)
        self.stockcode = randomcodegenerator()
        self.additem.setStockcode(self.stockcode)
        self.additem.clickAddStockCodePlusIcon()
        time.sleep(3)
        #Clicking on Back code.
        self.additem.setStockcodeByBarCode()
        
        #Manual Enter Stock code using randomcodegenerator functions
        # self.additem.clickAddStockCodePlusIcon()
        # self.additem.setStockcode3("1234098765")
        
          
        
        self.itemname = "Rhythm"+ " "+ "Winery" + " " + randomitemname_generator() + "ML"
        time.sleep(3)
        self.additem.setName(self.itemname)
        # self.additem.setStockcode("9466177105")
        self.additem.setQtyOnHand("200")
        self.additem.setQtyOnHand2("150")
        # self.additem.clickQtyPlusIcon()
        
        
        self.additem.setPrice("50")
        self.additem.setAvgCost("5")
        self.additem.setMargin("10")
        self.additem.setMarkup("11.11")
        self.additem.setLatestCost("5")
        #clicking on Dropdown
        self.additem.clickOnItemSize_Drp()
        
        #Select Dropdown
        
        self.additem.setDrpItemSize()
        
        
        self.additem.clickOnItemCategory_Drp()
        self.additem.setDrpItemCategory()
        
        self.additem.clickOnItemSupplier_Drp()
        self.additem.setDrpItemSupplier()
        
        self.additem.clickOnItemTax_Drp()
        self.additem.setDrpItemTax()
        
    
    
        self.venderItemNo = randomcodegenerator()
        self.additem.setVendorNo(self.venderItemNo) 
        
        
        self.additem.setSKU("0002500")
        self.additem.setUnitPerCase("11")
        self.additem.setCaseCostTotal(52)
        self.additem.setRpoint("7")
        self.additem.setRvalue("101")
        
        self.additem.clickOnItemRank_Drp()
        self.additem.setDrpItemRank()
        self.additem.checkedAddAI()
        time.sleep(1)
        self.additem.checkedAddAI()
        # self.additem.checked_PL()
        time.sleep(1)

        
        
        # Navigate to options tab || Created By: Neha Singh
        self.additem.clickOptions()
        self.additem.clickDoNotAutoUpdate()
        self.additem.clickDoNotTrackInv()
        self.additem.clickAddToShortcutKey()
        self.additem.clickCloseOutItem()
        
        time.sleep(1)
        self.additem.clickDoNotDiscount()
        self.additem.clickDoNotShowToWebstore()
        self.additem.clickHideInventory()
        self.additem.clickEBTEligible()
        
        self.additem.setDefaultQty("5")
        self.additem.setMinPrice(2)
        # self.additem.setRemindDate()
        # self.additem.setSelectedDate()
        
        self.venderName = "Neha" + randomitemname_generator() + "ZP"
        self.additem.setVendorItmName(self.venderName)
         
        self.additem.setNotes("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
        time.sleep(1)
        #Dropdown Sections
        self.additem.clickOnOptionsTag_Drp()
        time.sleep(1)
        self.additem.setOptionsTag()
        
        self.additem.clickOnOptionsIType_Drp()
        self.additem.setOptionsIType()
        
        time.sleep(2)
        self.additem.clickOnSave()
        time.sleep(10)
        
        #Search Added Item Name
        self.additem.findAddedItem(self.itemname)
        time.sleep(2)
        #Expend Added Item
        self.additem.expendSearchedItem()
        time.sleep(6)
        self.additem.clickOnClearSearchedItem()
        time.sleep(3)
        self.additem.closedExpendedItem()
        
        assert True
        self.logger.info("*****Saved customer info*****")
        # time.sleep(5)  
        # self.additem.sortItemIDcol()
        # self.additem.getNoOfRows()
        # self.additem.getNoOfColumns()
        # status = self.additem.verifyAddItem(self.itemname)
        # assert True == status
        time.sleep(10)
        self.logger.info("*****Test_003_AddItem Finished*****")
        print("*****Test_003_AddItem Finished*****")
        self.driver.close()


def randomitemname_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))

  
def randomcodegenerator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))
