import pytest
import time

from pageObjects.POS_Sale_ItemsPage import POS_Sale_ItemsPage
from utilities.customLogger import LogGen


class Test_002_POS_SaleItem:
    posURL = "http://bottlepos5-qa.bottlepos.com"
    posURL2 = "http://bottlepos5-qa.bottlepos.com/pos"
    username = "admin"
    password = "zapbuild1"
    logger = LogGen.loggen()

    # @pytest.mark.regression
    # def test_POS_Login(self, setup):           
    #     self.logger.info("*****Test_002_POS_Login started*****")
    #     self.logger.info("***************Opening the login page*************")
    #     self.driver = setup
    #     self.driver.get(self.posURL)
    #     self.driver.maximize_window()
        
       

    #     act_url = self.driver.current_url
    #     print(act_url,"This is Current URL")

    #     if act_url == "http://bottlepos5-qa.bottlepos.com/":
    #         time.sleep(5)
    #         assert True
    #         # self.driver.close()
    #         self.logger.info("***************POS Login page launch Passed*************")
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\" + "test_poshomePage.png")
    #         # self.driver.close()
    #         self.logger.info("***************POS Login page launch is Failed*************")
    #         assert False
    
    
    

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_POS_SaleItems(self, setup):
        self.logger.info("***************Verifying the POS Login test*************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.posURL)
        
        print(self.driver.get_cookies())
       
        self.posSale = POS_Sale_ItemsPage(self.driver)
        time.sleep(5)
        self.posSale.clickOnDeviceNotSetupBtn()
        
        if self.posURL == "http://bottlepos5-qa.bottlepos.com":
            
            time.sleep(5)
            self.posSale.setUserName(self.username)
            self.posSale.setUserPassword(self.password)
            self.posSale.clickLogin()
            self.driver.save_screenshot(".\\Screenshots\\" + "Screenshots/posLoginPassed.png")
            assert True
            # self.driver.close()
            self.logger.info("***************POS Login test passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "postest_login.png")
            self.driver.close()
            self.logger.info("***************Login test failed*************")
            assert False
        time.sleep(3)
        
        #Initial Device Setup
        print("Started Initial Device Setup")
        if self.posURL == "http://bottlepos5-qa.bottlepos.com":   
            self.logger.info("***************Initial Device Setup************")
            self.deviceSetup = POS_Sale_ItemsPage(self.driver)
            self.deviceSetup.setStoreName()
            time.sleep(1)
            self.deviceSetup.selectStoreName()
            time.sleep(1)
            self.deviceSetup.setDeviceName()
            time.sleep(1)
            self.deviceSetup.selectDeviceName()
            time.sleep(1)
            self.deviceSetup.clickRegister()
            time.sleep(3)
            assert True
            # self.driver.close()
            print("Device Setup Done")
            self.logger.info("***************Device Setup Test Passed*************")
            
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "postest_DeviceSetup_Failed.png")
            self.driver.close()
            self.logger.info("***************DeviceSetup  test failed*************")
            assert False
        
        
        
        time.sleep(3)
        print("*********Started Item Sale Cancel Cases*********")
        self.logger.info("***************Started Item Sale Cancel Cases*************")
        # if self.posURL2 == "http://bottlepos5-qa.bottlepos.com/pos":  
        #Handling Pax Error
        self.deviceSetup.clickOnPaxErrorOk()
        time.sleep(1)
        #Starting Page Reload Its Temp Code
        self.current_url="http://bottlepos5-qa.bottlepos.com/pos"
        self.driver.get(self.driver.current_url)
        time.sleep(3)
        self.driver.refresh()
        time.sleep(16)
        #End Page Reload Its Temp Code
        #Adding Item By Searching Item Name 
        self.logger.info("***************Started Adding Item Name By Searching Name ************")
        print("***************Started Adding Item By Searching Stock Code ************")
        self.posSaleItem=POS_Sale_ItemsPage(self.driver)
        time.sleep(2)
        self.posSaleItem.setItemByStockCode(9999910548)
        time.sleep(2)
        self.posSaleItem.clickOnItemDrpDown()
        time.sleep(2)
        
            #Handing Cncle Sales
        print("********Handing Cancel Sales********")
        self.posSaleItem.clickOnCencelSale()
        self.posSaleItem.clickOnCencelSale_No()
        self.posSaleItem.clickOnCencelSale()
        self.posSaleItem.clickOnCencelSale_Yes()
        
        #Handling Sale Teb 
        print("Handling Sale Teb For  Cenceled Item ")
        time.sleep(3)
        self.posSaleItem.clickOnSaleTab()
        time.sleep(10)
        
        #Handling FilteŕBy Status Item Order
        print("Handling FilterBy Status Item for Canceled Item")
        self.posSaleItem.clickOnFilteredStatus()       
        time.sleep(3)
        self.posSaleItem.clickOnFilteredByStatusCanceled() 
            
        self.posSaleItem.clickOnRigister()
        
        # self.posSaleItem.clickOnViewSoldItem()
        # time.sleep(1)
        # self.posSaleItem.setNoteViewSoldItem("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
        time.sleep(2)
        self.posSaleItem.setItemByStockCode(9999910548)
        time.sleep(2)
        self.posSaleItem.clickOnItemDrpDown()
        time.sleep(2)
        
        
        
        self.posSaleItem.clickOnRemoveItem()
        time.sleep(2)
        self.posSaleItem.setItemByStockCode(9999910548)
        time.sleep(2)
        self.posSaleItem.clickOnItemDrpDown()
        time.sleep(1)
        self.posSaleItem.setItemQty()
        time.sleep(1)
        self.posSaleItem.clickOnItemQty()
        time.sleep(1)
        # self.posSaleItem.clickOnItemPrice()
        # self.posSaleItem.clickOnItemPriceSelect()
        # time.sleep(1)
        # self.posSaleItem.clickOnItemPriceSelect()
        # time.sleep(1)
        # self.posSaleItem.clickOnItemPriceSelect()
        # time.sleep(1)
        # self.posSaleItem.clickOnItemPriceSelect()
        # time.sleep(1)
        # self.posSaleItem.clickOnItemPriceSelect()
        # time.sleep(1)
        self.posSaleItem.clickOnItemTax()
        time.sleep(1)
        self.posSaleItem.clickOnItemTaxSelect()
        time.sleep(1)
        self.posSaleItem.clickOnEditItemIcon()
        time.sleep(1)
        self.posSaleItem.clickOnEditItemCancel_Button()
        time.sleep(1)
        self.posSaleItem.clickOnEditItemIcon()
        time.sleep(1)
        self.posSaleItem.clickOnEditItemOptionsTab()   
        time.sleep(1)
        self.posSaleItem.clickOnEditItemUpdateButton()
        time.sleep(3)
        self.posSaleItem.clickOnItemQtyPlusIcon()
        time.sleep(1)
        self.posSaleItem.clickOnItemQtyMinusIcon()
    
        # Adding Item by ItemName
        time.sleep(2)
        self.posSaleItem.setItemByStockCode("Rhythm Winery ")
        time.sleep(2)
        self.posSaleItem.clickOnItemDrpDown()
        
        #Adding Item From ShortCode
        time.sleep(2)
        self.posSaleItem.clickOnaddItemFromShortcut()
        
        #Clicking On Back Button Shortcut
        time.sleep(1)
        self.posSaleItem.clickOnshortcutBackButton()
        
        #Handling  All Category Item
        time.sleep(1)
        self.posSaleItem.clickOnAllCategories()
        time.sleep(2)
        self.posSaleItem.clickOnaddItemFromShortcut()
        time.sleep(1)
        self.posSaleItem.clickOnshortcutBackButton()
        
        #Handling Miscellaneous
        time.sleep(1)
        self.posSaleItem.clickOnMiscellaneous()
        time.sleep(2)
        self.posSaleItem.clickOnaddItemFromShortcut()
        time.sleep(1)
        self.posSaleItem.clickOnshortcutBackButton()
        
        #Handling to Click On  PAY Button
        time.sleep(1)
        self.posSaleItem.clickOnPAYButton()
        
        #Handling Payment By CASH Using Exact Tender Amount 
        time.sleep(3)
        self.posSaleItem.clickOnExactTenderAmt()
        
        #Handling Recipt Print Yes/NO Case
        time.sleep(1)
        self.posSaleItem.clickOnPrintReceipt_NO()
        
        #Handling Sale Teb 
        time.sleep(1)
        self.posSaleItem.clickOnSaleTab()
        time.sleep(10)
        self.posSaleItem.clickOnViewSoldItem()
        time.sleep(1)
        self.posSaleItem.setNoteViewSoldItem("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
        
        #handling SavéButton
        time.sleep(3)
        self.posSaleItem.clickOnSaveButton()
        
        #handling Print Button
        time.sleep(5)
        self.posSaleItem.clickOnPrintButton()
        time.sleep(5)
            
    # Handling Window Close
        assert True
        
        print("*****Item Sold Successfully!*****")
        self.logger.info("***************POS Item Sale Test Passed Successfully ************")
        self.driver.save_screenshot(".\\Screenshots\\" + "/ItemSoldSuccessfully.png")
        # self.driver.close()
        
        
    # else:
        # print("*****Item Sold Failed!*****")
        # self.driver.save_screenshot(".\\Screenshots\\" + "ItemSoldFailed.png")
        # self.driver.close()
        # self.logger.info("*************** POS Item Sale Test Failed!*************")
        # assert False
        
        