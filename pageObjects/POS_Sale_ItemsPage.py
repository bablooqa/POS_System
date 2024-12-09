from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class POS_Sale_ItemsPage:
    # login
    txt_username_name = "username"
    txt_password_name = "password"
    # btn_login_xpath = "//button[@id='loginbutton']"

    btn_login_xpath = "//button[@type='submit']"
    btn_logout_xpath = "//a[@title='Logout']"

    # device setup
    btn_device_not_setup_ok_xpath = "//button[contains(text(),'OK')]"
    
    #Initial Device Setup
    #Select an existing store for the device or enter a new store
    selectStore_xpath="/html/body/div[3]/div/div/div[2]/form/div/div[1]/div/div/div/div[2]/div"
    chooseStoreName_xpath="//div[contains(text(),'NEHA STORE')]"
    
    #Select a device to merge with or enter a new device name
    selectDevice_xpath="/html/body/div[3]/div/div/div[2]/form/div/div[2]/div/div/div/div[2]/div"
    chooseDeviceName_xpath="//div[contains(text(),'MOBILE')]"
    
    # Click On Rigister Button
    registerButton_xpath="//button[contains(text(),'Register')]"
    
    #Pax Error Xpath
    heading_pax_alert_xpath="/html/body/div[3]/div/div/div[1]/div"
    btn_pax_ok_xpath="//button[contains(text(),'Ok')]"
    
    # Handling Add Items Xpath
    searchItemByStockCode_xpath="//input[@placeholder='Stock Search']"
    addItemByStockCode_xpath="/html/body/div/div/main/div[1]/div[1]/div/div[3]/div[1]/div/div/div/div/div"
    
    #Addding Item From Category
    addItemFromShortcut_xpath="//body/div[@id='root']/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]"
    
    #Handling Remove Added Items
    removeItem_xpath="//tbody/tr[1]/td[7]/button[3]"
    

    #Handling Item Info
    qtyItem_xpath="//tbody/tr[1]/td[1]/div[1]/input[1]"
    qtyItemSelect_xpath="//span[contains(text(),'5')]"
    priceItem_xpath="//input[@placeholder='Price']"
    priceItemSelect_xpath="//span[normalize-space()='5']"
    itemTax_xpath="//select[@class='form-control']"
    selectItemTax="//option[contains(text(),'HighTax')]"
    editItem_xpath="//button[@title='Edit Item']"
    editItemCancelButton_xpath="//body/div[3]/div[1]/div[1]/div[3]/button[1]"
    
    #Handling Edit Item Options Sections xPath
    editItemOptionsSection_xpath="//body/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/a[1]"
       
    #Handling Edit Item Update Button xPath
    clickOnUpdateButton_xpath="//button[contains(text(),'Update')]"
    
    #Handling Increase/Descrease Item Qty xPath
    itemQtyPlusIcon_xpath="//tbody/tr[1]/td[7]/button[1]"
    itemQtyMinusIcon_xpath="//tbody/tr[1]/td[7]/button[2]"
    
    #Click On Back Button from Shortcut xPath
    shortcutBackButton_xpath="//body/div[@id='root']/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    
    clickOnAllCategories_xpath="//h3[contains(text(),'All Categories')]"
    clickOnMiscellaneous_xpath="//h3[contains(text(),'Miscellaneous')]"
    
    #Handling PAY Button Xpath
    payButton_xpath="/html/body/div/div/main/div[1]/div[2]/div/div/div[3]/button"
    
    
        #Handiling Cancle Sale Xpath
    cancelSale_xpath="//button[contains(text(),'Cancel')]"
    cancelSale_No_xpath="//button[normalize-space()='No']"
    cancelSale_Yes_xpath="//button[normalize-space()='Yes']"
    
    
    #handling Filtered By Status
    clickOnFilterByStatus_xpath="/html/body/div/div/main/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div"
    filterByStatusCanceled_xpath="//div[contains(text(),'Canceled')]"
    
    #Handling Payment By CASH Using Tender Amount
    clickOnExactTenderAmt_xpath="//body/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]"
    
    #Handling Receipt Print Yes/NO Case Xpath
    printReceipt_NO_xpath="//body[1]/div[5]/div[1]/div[1]/div[3]/button[1]"
    
    
    #Handling Sale Teb Xpath
    clickOnSale_xpath="//a[@title='Sales']"
    viewSoldItem_xpath="//tbody/tr[1]/td[10]/button[1]"
    txtNoteViewSoldItem_xpath="//textarea[@placeholder='Notes']"
    
    
    #handling Register
    rigister_xpath="//a[contains(text(),'Register')]"
    
    
    #Handle Save Button Xpath
    saveButton_xpath="//button[contains(text(),'Save')]"
    
    #Handling Print Button Xpath
    printButton_xpath="//button[normalize-space()='Print']"
    
    
    
    
    
    
    
    
    def __init__(self, driver):
        self.driver = driver

    #login Method
    def setUserName(self, username):
        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located((By.NAME, self.txt_username_name)))
        self.driver.find_element(By.NAME, self.txt_username_name).clear()
        self.driver.find_element(By.NAME, self.txt_username_name).send_keys(username)

    def setUserPassword(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).clear()
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    # Setup Method l
    def clickOnDeviceNotSetupBtn(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.btn_device_not_setup_ok_xpath).click()


    #Initial Device Setup Function
    
    # def setStoreName(self, store):
    #     devicedrp = Select(self.driver.find_element(By.XPATH, self.selectStore_xpath))
    #     devicedrp.select_by_visible_text(store)
    
    def setStoreName(self):
        self.driver.find_element(By.XPATH, self.selectStore_xpath).click()
        
    def selectStoreName(self):
        self.driver.find_element(By.XPATH, self.chooseStoreName_xpath).click()
        
    #Set Device Name
    def setDeviceName(self):
        self.driver.find_element(By.XPATH, self.selectDevice_xpath).click()
    
    def selectDeviceName(self):
        self.driver.find_element(By.XPATH, self.chooseDeviceName_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.registerButton_xpath).click()

    # handling pax error
    def clickOnPaxErrorOk(self):
        paxheading = self.driver.find_element(By.XPATH, self.heading_pax_alert_xpath).text
        if paxheading == "Pax Initialization Error":
            self.driver.find_element(By.XPATH, self.btn_pax_ok_xpath).click()
        else:
            return

    #Handling Add Item by Stock Code
    def setItemByStockCode(self,stockCode):
        self.driver.find_element(By.XPATH, self.searchItemByStockCode_xpath).send_keys(stockCode)
    
    def clickOnItemDrpDown(self):
        self.driver.find_element(By.XPATH, self.addItemByStockCode_xpath).click()
    
    def clickOnaddItemFromShortcut(self):
        self.driver.find_element(By.XPATH, self.addItemFromShortcut_xpath).click()
    
    
    #Handling Function of Remove Added Items
    def clickOnRemoveItem(self):
        self.driver.find_element(By.XPATH, self.removeItem_xpath).click()
    
  
    #Handling Item Qty
    def setItemQty(self):
        self.driver.find_element(By.XPATH, self.qtyItem_xpath).click()
    
    def clickOnItemQty(self):
        self.driver.find_element(By.XPATH, self.qtyItemSelect_xpath).click()
    
    def clickOnItemPrice(self):
        self.driver.find_element(By.XPATH, self.priceItem_xpath).click()
        
    def clickOnItemPriceSelect(self):
        self.driver.find_element(By.XPATH, self.priceItemSelect_xpath).click()
    
    
    def clickOnItemTax(self):
        self.driver.find_element(By.XPATH, self.itemTax_xpath).click()
    
    def clickOnItemTaxSelect(self):
        self.driver.find_element(By.XPATH, self.selectItemTax).click()
        
    def clickOnEditItemIcon(self):
        self.driver.find_element(By.XPATH, self.editItem_xpath).click()
        
    def clickOnEditItemCancel_Button(self):
        self.driver.find_element(By.XPATH, self.editItemCancelButton_xpath).click()
        
    #Handling Edit Item Options Sections
    def clickOnEditItemOptionsTab(self):
        self.driver.find_element(By.XPATH, self.editItemOptionsSection_xpath).click()
        
        
    #Hanndle Cancel Sale Functions
    def clickOnCencelSale(self):
        self.driver.find_element(By.XPATH, self.cancelSale_xpath).click()
        
    def clickOnCencelSale_No(self):
        self.driver.find_element(By.XPATH, self.cancelSale_No_xpath).click()
        
    def clickOnCencelSale_Yes(self):
        self.driver.find_element(By.XPATH, self.cancelSale_Yes_xpath).click()
        
    
    #Handling Filter By Status
    def clickOnFilteredStatus(self):
        self.driver.find_element(By.XPATH, self.clickOnFilterByStatus_xpath).click()
    
     #Handling Filter By Cancled
    def clickOnFilteredByStatusCanceled(self):
        self.driver.find_element(By.XPATH, self.filterByStatusCanceled_xpath).click()
    
        
    #handling Register
    def clickOnRigister(self):
        self.driver.find_element(By.XPATH, self.rigister_xpath).click()
        
        
    
    
    
    
    #Handling Edit Item Update Button
    
    def clickOnEditItemUpdateButton(self):
        self.driver.find_element(By.XPATH, self.clickOnUpdateButton_xpath).click()
    
    #Handling Increase/Descrease Item Qty xPath
    def clickOnItemQtyPlusIcon(self):
        self.driver.find_element(By.XPATH, self.itemQtyPlusIcon_xpath).click()
    
    def clickOnItemQtyMinusIcon(self):
        self.driver.find_element(By.XPATH, self.itemQtyMinusIcon_xpath).click()
    
    
    #Click On Back Button from Shortcut
    def clickOnshortcutBackButton(self):
        self.driver.find_element(By.XPATH, self.shortcutBackButton_xpath).click()
        
    def clickOnAllCategories(self):
        self.driver.find_element(By.XPATH, self.clickOnAllCategories_xpath).click()
        
    def clickOnMiscellaneous(self):
        self.driver.find_element(By.XPATH, self.clickOnMiscellaneous_xpath).click()

    #Handling PAY Button Functions
    def clickOnPAYButton(self):
        self.driver.find_element(By.XPATH, self.payButton_xpath).click()


     #Handling Payment By CASH Using Tender Amount Function
    def clickOnExactTenderAmt(self):
        self.driver.find_element(By.XPATH, self.clickOnExactTenderAmt_xpath).click()

    #Handling Recipt Print Yes/NO Case Functions
    def clickOnPrintReceipt_NO(self):
        self.driver.find_element(By.XPATH, self.printReceipt_NO_xpath).click()


    #Handling Sale Teb Section Functions
    def clickOnSaleTab(self):
        self.driver.find_element(By.XPATH, self.clickOnSale_xpath).click()
        
    
    def clickOnViewSoldItem(self):
        self.driver.find_element(By.XPATH, self.viewSoldItem_xpath).click()
    
    def setNoteViewSoldItem(self,noteTxt):
        self.driver.find_element(By.XPATH, self.txtNoteViewSoldItem_xpath).send_keys(noteTxt)
        
    
    #Handle Save Button Functions
    def clickOnSaveButton(self):
        self.driver.find_element(By.XPATH, self.saveButton_xpath).click()
        
    
    #Handling Print Button 
    def clickOnPrintButton(self):
        self.driver.find_element(By.XPATH, self.printButton_xpath).click()
    
        
        
        

    # handling Offline alert
    # def clickOfflineOk(self):
    #     offlineheading = self.driver.find_element(By.XPATH, self.heading_offline_alert_xpath).is_Displayed()
    #     print(offlineheading)
    #     if offlineheading == "True":
    #         self.driver.find_element(By.XPATH, self.btn_offliine_ok_xpath).click()
    #     else:
    #         return
