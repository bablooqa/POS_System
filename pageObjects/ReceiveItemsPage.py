from multiprocessing.sharedctypes import Value
import time
import zlib


# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class ReceiveItems:  
#ReceiveItems Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_Receive_xpath = "/html/body/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[10]/div/div/div/div/div[4]/a"
    refresh_xpath="/html/body/div/main/div[1]/ul/li[1]/button"
    
    #Button XPATH 
    btnReceiveItems_xpath="//button[contains(text(),'Receive Items')]"
    btnItemsClose_xpath="/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[1]"
    btnClickOnNo_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[3]/button[2]"
    btnClickOnYes_xpath="//button[normalize-space()='Yes']"
    
    btnFinalize_xpath="//button[normalize-space()='Finalize']"
    btnInvoiceDetailsErrorOk_xpath="//button[contains(text(),'Ok')]"
    btnSaveForlater_xpath="//button[normalize-space()='Save For later']"
    btnPrint_xpath="//button[normalize-space()='Print']"
    #Add New Items
    btnAddNewItem_xpath="//button[contains(text(),'Add New Item')]"
    btnAddItemPlusIcon_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr[3]/td[17]/div/button[1]"
    
    #Print Button to Save File
    printButtonToSaveFile_xpath='//*[@id="sidebar"]//print-preview-button-strip//div/cr-button[1]'
      
    
    
    drpDownSelectSupplier_xpath="//body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
    drpDownSelectSupplierValue_xpath="//div[contains(text(),'GENERAL WHOLESALE')]"
    
    invoiceNumberInput_xpath="//input[@placeholder='Invoice Number']"
    invoiceTotalInput_xpath="//input[@placeholder='Invoice Total']"
    
    searchProductNameInput_xpath="//input[@placeholder='Search product name and press enter']"
    closingItemDetailDialogBox_xpath="//body[1]/div[5]/div[1]/div[1]/div[3]/button[1]"
    
    
    #XPATH of Items Details
    receivedCaseInput_xpath="//input[@placeholder='Received Case']"
    unitPerCaseInput_xpath="//input[@placeholder='Unit Per Case']"
    totalCostInput_xpath="//input[@placeholder='Total Cost']"
    costPerBottleInput_xpath="//input[@placeholder='Cost Per Bottle']"
    priceInput_xpath="//input[@placeholder='Price']"
    marginInput_xpath="//input[@name='margin']"
    markupInput_xpath="//input[@placeholder='Markup']"
    
    #XPATH of Save Button
    btnSaveItemDetails_xpath="//button[normalize-space()='Save']"
    
    
    #Date Input
    invoiceDatePic_xpath='//*[@id="invoiceDate"]/div/div[1]/div/input'
    invoiceDateSelect_xpath="/html/body/div[3]/div/div/div[2]/form/div[1]/div[9]/div/div/div[2]/div/table/tbody/tr[4]/td[4]"
    dueDatePic_xpath="//div[@class='input-group']//input"
    dueDateSelect_xpath="/html/body/div[3]/div/div/div[2]/form/div[1]/div[10]/div/div/div[2]/div/table/tbody/tr[5]/td[3]"
    
    #Notes Text Area
    txtNotes_xpath="//textarea[@placeholder='Notes']"
    
    
    inputStockCode_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr[3]/td[4]/input"
    inputItemName_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr[3]/td[5]/input"
    inputReceivedCase_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr[3]/td[8]/input"
    inputPrice_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr[3]/td[13]/input"
    inputVendorItemNo_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr[3]/td[16]/input"
    
    
    
    
    # Function to click on Various Buttions
    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsReceive(self):
        self.driver.find_element(By.XPATH, self.linkItems_Receive_xpath).click()



    
    def clickOnRefresh(self):
        self.driver.find_element(By.XPATH, self.refresh_xpath).click()
    
    def clickOnReceiveItemsButton(self):
        self.driver.find_element(By.XPATH, self.btnReceiveItems_xpath).click()
        
    def clickOnCloseReceiveButton(self):
        self.driver.find_element(By.XPATH, self.btnItemsClose_xpath).click()
        
    def clickOnNoButton(self):
        self.driver.find_element(By.XPATH, self.btnClickOnNo_xpath).click()
        
    def clickOnYesButton(self):
        self.driver.find_element(By.XPATH, self.btnClickOnYes_xpath).click()
      
      
      
          
    def clickOnFinalize(self):
        self.driver.find_element(By.XPATH, self.btnFinalize_xpath).click()
        
    def clickOnInvoiceDetailsErrorOk(self):
        self.driver.find_element(By.XPATH, self.btnInvoiceDetailsErrorOk_xpath).click()   
        
    def clickOnSaveForlater(self):
        self.driver.find_element(By.XPATH, self.btnSaveForlater_xpath).click()
        
    def clickOnPrint(self):
        self.driver.find_element(By.XPATH, self.btnPrint_xpath).click()
        
    def clickOnPrintButtonToSaveFile(self):
        self.driver.find_element(By.XPATH, self.printButtonToSaveFile_xpath).perform()
        
        
    
        
    def clickOnDrpDownSelectSupplier(self):
        self.driver.find_element(By.XPATH, self.drpDownSelectSupplier_xpath).click()
        
    def clickOndrpDownSelectSupplierValue(self):
        self.driver.find_element(By.XPATH, self.drpDownSelectSupplierValue_xpath).click()
        
        
    def setInvoiceNumberInput(self,invoiceNumber):
        # self.driver.find_element(By.XPATH, self.invoiceNumberInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.invoiceNumberInput_xpath).send_keys(invoiceNumber)
        
    def setInvoiceTotalInput(self,totalInvoice):
        self.driver.find_element(By.XPATH, self.invoiceTotalInput_xpath).send_keys(totalInvoice)
        
    def setSearchProductNameInput(self,productName):
        self.driver.find_element(By.XPATH, self.searchProductNameInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.searchProductNameInput_xpath).send_keys(productName)

#Click On Enter Key

    def clickOnEnterKey(self):
        self.driver.find_element(By.XPATH, self.searchProductNameInput_xpath).send_keys(Keys.ENTER)

#Closing Dialog box of Item Details

    def clickOnClosingItemDetailDialogBox(self):
        self.driver.find_element(By.XPATH, self.closingItemDetailDialogBox_xpath).click()
        
        
    
      
      
#click on Items Details
    def setReceivedCaseInput(self,receivedCaseInput):
        self.driver.find_element(By.XPATH, self.receivedCaseInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.receivedCaseInput_xpath).send_keys(receivedCaseInput)
        
    def setUnitPerCaseInput(self,unitPerCaseInput):
        self.driver.find_element(By.XPATH, self.unitPerCaseInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.unitPerCaseInput_xpath).send_keys(unitPerCaseInput)
        
    def setTotalCostInput(self,totalCostInput):
        self.driver.find_element(By.XPATH, self.totalCostInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.totalCostInput_xpath).send_keys(totalCostInput)
        
    def setCostPerBottleInput(self,costPerBottleInput):
        self.driver.find_element(By.XPATH, self.costPerBottleInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.costPerBottleInput_xpath).send_keys(costPerBottleInput)
        
    def setPriceInput(self,priceInput):
        self.driver.find_element(By.XPATH, self.priceInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.priceInput_xpath).send_keys(priceInput)
        
    def setMarginInput(self,marginInput):
        self.driver.find_element(By.XPATH, self.marginInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.marginInput_xpath).send_keys(marginInput)
        
    def setMarkupInput(self,markupInput):
        self.driver.find_element(By.XPATH, self.markupInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.markupInput_xpath).send_keys(markupInput)



    #clicking Save Buttons
    def clickOnSaveItemDetails(self):
        self.driver.find_element(By.XPATH, self.btnSaveItemDetails_xpath).click()
        
        

    def setInvoiceDatePic(self):
        self.driver.find_element(By.XPATH, self.invoiceDatePic_xpath).click()
        

    def setInvoiceDateSelect(self):
        self.driver.find_element(By.XPATH, self.invoiceDateSelect_xpath).click()
        

    def setDueDatePic(self):
        self.driver.find_element(By.XPATH, self.dueDatePic_xpath).click()

    def setDueDateSelect(self):
        self.driver.find_element(By.XPATH, self.dueDateSelect_xpath).click()
        

    def setNotes(self, notes):
        self.driver.find_element(By.XPATH, self.txtNotes_xpath).send_keys(notes)
        

    def clickOnAddNewItem(self):
        self.driver.find_element(By.XPATH, self.btnAddNewItem_xpath).click()
        

    def setStockCode(self,stockCode):
        self.driver.find_element(By.XPATH, self.inputStockCode_xpath).send_keys(stockCode)
        

    def setItemName(self,itemName):
        self.driver.find_element(By.XPATH, self.inputItemName_xpath).send_keys(itemName)
        

    def setReceivedCase(self,receivedCase):
        self.driver.find_element(By.XPATH, self.inputReceivedCase_xpath).clear()
        self.driver.find_element(By.XPATH, self.inputReceivedCase_xpath).send_keys(receivedCase)
        

    def setPrice(self,price):
        self.driver.find_element(By.XPATH, self.inputPrice_xpath).clear()
        self.driver.find_element(By.XPATH, self.inputPrice_xpath).send_keys(price)
        
    def setInputVendorItemNo(self,inputVendorItemNo):
        self.driver.find_element(By.XPATH, self.inputVendorItemNo_xpath).send_keys(inputVendorItemNo)
        
        
    def clickOnAddItemPlusIcon(self):
        self.driver.find_element(By.XPATH, self.btnAddItemPlusIcon_xpath).click()
        
        
        