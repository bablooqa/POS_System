from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys



class BulkUpdate:  
#Bulk Update Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_menuitem_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]"
    refresh_xpath="/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[1]/button[1]"
    btnManageDropDown_xpath="/html/body/div/main/div[1]/ul/li[3]/div"
    btnBulkUpdate_xpath="//a[contains(text(),'Bulk Update')]"
    btnBulkUpdateBox_Close_xpath="//button[normalize-space()='Close']"
   
    #Click On Advance Update
    btnAdvanceUpdate_xpath="//button[contains(text(),'Advance Update')]"
    btnOK_xpath="//button[contains(text(),'OK')]"
    
    #XPATH For Advance Search
    btnAdvanceUpdateSearch_xpath="/html/body/div[3]/div/div/div[2]/div[1]/button[2]"
    btnAdvanceUpdateSearch_Cancel_xpath="//button[contains(text(),'Cancel')]"
    inputStockCode_xpath="/html/body/div[5]/div/div/div[2]/form/div[1]/div[1]/div/input"
    inputQtyOnHand_xpath="/html/body/div[5]/div/div/div[2]/form/div[1]/div[2]/div[1]/input"
    inputQtyOnHandTo_xpath="/html/body/div[5]/div/div/div[2]/form/div[1]/div[2]/div[2]/input"
    txtAdvanceSearchName_xpath="//input[@placeholder='name']"
    inputUnitPrice_xpath="//input[@name='unitpricemin']"
    inputUnitPriceTo_xpath="//input[@name='unitpricemax']"
    inputMargin_xpath="//input[@placeholder='Enter Margin']"
    inputMarginTo_xpath="//input[@name='marginmax']"
    inputCost_xpath="//input[@placeholder='Enter Cost']"
    inputCostTo_xpath="//input[@name='costmax']"
    inputVendorItemNo_xpath="//input[@placeholder='Enter Item No']"
    advanceSerachSubmit_xpath="//button[@type='submit']"
    inputUnitsPerCase_xpath="//input[@placeholder='Units Per Case']"
    inputEnterDefaultQty_xpath="//input[@placeholder='Enter Default Qty']"
    inputEnterSKU_xpath="//input[@placeholder='Enter SKU']"
    inputReorderPoint_xpath="/html/body/div[5]/div/div/div[2]/form/div[7]/div[4]/div/input"
    inputReorderValue_xpath="/html/body/div[5]/div/div/div[2]/form/div[7]/div[5]/div/input"
    inputVendorName_xpath="/html/body/div[5]/div/div/div[2]/form/div[7]/div[9]/div/input"
    inputMinPrice_xpath="/html/body/div[5]/div/div/div[2]/form/div[7]/div[11]/div/input"
    
    #Clear Advance Search Inpute
    btnClearAdvanceSearchInputs_xpath="//button[@type='button'][normalize-space()='Clear']"
    
    
    # *******Xpath for Advance Update******* 
    btnSearchFilters_xpath="//button[normalize-space()='Search FIlters']"
    btnSearch_xpath="//button[@title='Search']"
    btnRemoveItem_xpath="(//button[@title='Remove item'])[1]"
    removeItemConfirmation_No_xpath="//button[normalize-space()='No']"
    removeItemConfirmation_Yes_xpath="//button[normalize-space()='Yes']"
    removeAllItems_xpath="//button[@title='Remove All Items']"
    txtEnterName_xpath="//input[@placeholder='Enter Name']"
    txtEnterUnitPerCase_xpath="//input[@placeholder='Enter Unit Per Case']"
    btnEnterUnitPerCaseDownArrow_xpath="/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[2]/button"
    txtEnterUnitCost_xpath="//input[@placeholder='Enter Unit Cost']"
    btnEnterUnitCostCostDownArrow_xpath="/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[3]/button"
    txtEnterUnitPrice_xpath="//input[@placeholder='Enter Unit Price']"
    
    btnEnterUnitPriceDownArrow_xpath="/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[4]/button"
    
    drpDownTax_xpath="/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[5]/div/div/div[1]"
    drpDownSelectTax="//div[contains(text(),'HighTax')]"
    btnTaxDownArrow_xpath="//button[@title='Reset Tax in Data Table']"
    
    drpDownSupplier_xpath="/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[6]/div/div/div[1]"
    drpDownSelectSupplier_xpath="//div[normalize-space()='spenser']"
    btnSupplierDownArrow_xpath="//button[@title='Reset Supplier in Data Table']"
    
    
    drpDownCategory_xpath="(//div[@class='react-select__input-container css-ackcql'])[5]"
    drpDownSelectCategory_xpath="//div[normalize-space()='CategoryGroup793 Name']"
    btnCategoryDownArrow_xpath="//button[@title='Reset Category in Data Table']"
    
    txtEnterReorderPoint_xpath="//input[@placeholder='Enter Reorder Point']"
    btnEnterReorderPointDownArrow_xpath="//button[@title='Reset Reorder Point in Data Table']"

    
    txtEnterReorderValue_xpath="//input[@placeholder='Enter Reorder Value']"
    btnEnterReorderValue_xpath="//button[@title='Reset Reorder Value in Data Table']"
    
    drpDownSize_xpath="/html/body/div[3]/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[10]/div/div/div[1]/div[2]"
    drpDownSelectSize_xpath="//div[normalize-space()='ITEM805ML SIZE-NAME']"
    btnSizeDownArrow_xpath="//button[@title='Reset Size in Data Table']"
    
    
    btnUpdate_xpath="//button[normalize-space()='Update']"
    btnUpdatingBulkItemsDilogBox_Close_xpath="//button[contains(@class,'btn btn-success px-5')]"

    
#Function to click on various Buttions || Created By: Neha Singh
  
    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkItems_menuitem_xpath).click()
        
        
    def clickOnRefresh(self):
        self.driver.find_element(By.XPATH, self.refresh_xpath).click()
    
    def clickOnBulkUpdateButton(self):
        self.driver.find_element(By.XPATH, self.btnBulkUpdate_xpath).click()
        
    
    def clickOnManageDropDown(self):
        self.driver.find_element(By.XPATH, self.btnManageDropDown_xpath).click()
        
        
        

    def clickOnBulkUpdateBox_Close(self):
        self.driver.find_element(By.XPATH, self.btnBulkUpdateBox_Close_xpath).click()
        
        
        
    #Function Of Advance Update    
        
    def clickOnAdvanceUpdate(self):
        self.driver.find_element(By.XPATH, self.btnAdvanceUpdate_xpath).click()
        
    def clickOnOK(self):
        self.driver.find_element(By.XPATH, self.btnOK_xpath).click()
        
        
    def clickOnAdvanceUpdateSearch(self):
        self.driver.find_element(By.XPATH, self.btnAdvanceUpdateSearch_xpath).click()
        
   
        
    def clickOnAdvanceUpdateSearch_Cancel(self):
        self.driver.find_element(By.XPATH, self.btnAdvanceUpdateSearch_Cancel_xpath).click()
        
   
        
    def setStockCode(self,stockCode):
        self.driver.find_element(By.XPATH, self.inputStockCode_xpath).send_keys(stockCode)
        
        
    def setQtyOnHand(self,qtyOnHand):
        self.driver.find_element(By.XPATH, self.inputQtyOnHand_xpath).send_keys(qtyOnHand)
        
   
        
    def setQtyOnHandTo(self,qtyOnHandTo):
        self.driver.find_element(By.XPATH, self.inputQtyOnHandTo_xpath).send_keys(qtyOnHandTo)
        
   
        
    def setAdvanceSearchName(self,adName):
        self.driver.find_element(By.XPATH, self.txtAdvanceSearchName_xpath).send_keys(adName)
        
        
    def setUnitPrice(self,unitPrice):
        self.driver.find_element(By.XPATH, self.inputUnitPrice_xpath).send_keys(unitPrice)
        
        
    def setUnitPriceTo(self,unitPriceTo):
        self.driver.find_element(By.XPATH, self.inputUnitPriceTo_xpath).send_keys(unitPriceTo)
        
    def setMarginInput(self,margin):
        self.driver.find_element(By.XPATH, self.inputMargin_xpath).send_keys(margin)
        
        
    def setMarginToInput(self,marginTo):
        self.driver.find_element(By.XPATH, self.inputMarginTo_xpath).send_keys(marginTo)
        
        
    def setCostInput(self,cost):
        self.driver.find_element(By.XPATH, self.inputCost_xpath).send_keys(cost)
        
    
        
    def setCostToInput(self,costTo):
        self.driver.find_element(By.XPATH, self.inputCostTo_xpath).send_keys(costTo)
        
        
    def setVendorItemNo(self,vendorINo):
        self.driver.find_element(By.XPATH, self.inputVendorItemNo_xpath).send_keys(vendorINo)
        
    def setUnitsPerCase(self, upc):
        self.driver.find_element(By.XPATH, self.inputUnitsPerCase_xpath).send_keys(upc)
        
    def setEnterDefaultQty(self, qty):
        self.driver.find_element(By.XPATH, self.inputEnterDefaultQty_xpath).send_keys(qty)
        
    def setEnterSKU(self, sku):
        self.driver.find_element(By.XPATH, self.inputEnterSKU_xpath).send_keys(sku)
        
    def setReorderPoint(self, reorderPoint):
        self.driver.find_element(By.XPATH, self.inputReorderPoint_xpath).send_keys(reorderPoint)
        
    def setReorderValue(self, reorderValue):
        self.driver.find_element(By.XPATH, self.inputReorderValue_xpath).send_keys(reorderValue)
        
    def setVendorName(self, vendorName):
        self.driver.find_element(By.XPATH, self.inputVendorName_xpath).send_keys(vendorName)
        
    def setMinPrice(self, minPrice):
        self.driver.find_element(By.XPATH, self.inputMinPrice_xpath).send_keys(minPrice)
        
        
         #Click On Advance Search Clear Button
    def clickOnAClearAdvanceSearchInputs(self):
        self.driver.find_element(By.XPATH, self.btnClearAdvanceSearchInputs_xpath).click()
        
        
        #click On Advance search Button
    def clickOnAdvanceSearchSubmit(self):
        self.driver.find_element(By.XPATH, self.advanceSerachSubmit_xpath).click()
      
      
      
        
       # *******Advance Update******* 
 

    def clickOnSearchFilters(self):
            self.driver.find_element(By.XPATH, self.btnSearchFilters_xpath).click()
      

    def clickOnSearch(self):
            self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def clickOnRemoveItem(self):
            self.driver.find_element(By.XPATH, self.btnRemoveItem_xpath).click()
            
    
    def clickOnRemoveItemConfirmation_No(self):
        self .driver.find_element(By.XPATH, self.removeItemConfirmation_No_xpath).click()
    
    def clickOnRemoveItemConfirmation_Yes(self):
        self.driver.find_element(By.XPATH, self.removeItemConfirmation_Yes_xpath).click()
            
    
    def clickOnRemoveItemAllItems(self):
        self.driver.find_element(By.XPATH, self.removeAllItems_xpath).click()
            
    
    def clickOnEnterName(self,name):
        self.driver.find_element(By.XPATH, self.txtEnterName_xpath).send_keys(name)
            
    
    def clickOnEnterNameClear(self):
        self.driver.find_element(By.XPATH, self.txtEnterName_xpath).clear()
            
    def clickOnEnterUnitPerCase(self,enterUnitPerCase):
            self.driver.find_element(By.XPATH, self.txtEnterUnitPerCase_xpath).send_keys(enterUnitPerCase)
       
            
    def clickOnEnterUnitPerCaseDownArrow(self):
            self.driver.find_element(By.XPATH, self.btnEnterUnitPerCaseDownArrow_xpath).click()
       
            
    def clickOnEnterUnitCase(self,enterUnitCase):
            self.driver.find_element(By.XPATH, self.txtEnterUnitCost_xpath).send_keys(enterUnitCase)
       
            
    def clickOnEnterUnitCostDownArrow(self):
            self.driver.find_element(By.XPATH, self.btnEnterUnitCostCostDownArrow_xpath).click()
       
            
    def clickOnEnterUnitPrice(self,enterUnitPrice):
            self.driver.find_element(By.XPATH, self.txtEnterUnitPrice_xpath).send_keys(enterUnitPrice)
       
            
    def clickOnEnterUnitPriceDownArrow(self):
            self.driver.find_element(By.XPATH, self.btnEnterUnitPriceDownArrow_xpath).click()
            
            
    def clickOnDrpDownTax(self):
            self.driver.find_element(By.XPATH, self.drpDownTax_xpath).click()
            
            
    def clickOnDrpDownSelectTax(self):
            self.driver.find_element(By.XPATH, self.drpDownSelectTax).click()
            
            
    def clickOnTaxDownArrow(self):
            self.driver.find_element(By.XPATH, self.btnTaxDownArrow_xpath).click()
            
            
    def clickOnSupplierDropDown(self):
            self.driver.find_element(By.XPATH, self.drpDownSupplier_xpath).click()
            
            
    def clickOnDropDownSelectSupplier(self):
            self.driver.find_element(By.XPATH, self.drpDownSelectSupplier_xpath).click()
            
    
            
    def clickOnSupplierDownArrow(self):
            self.driver.find_element(By.XPATH, self.btnSupplierDownArrow_xpath).click()
            
            
    def clickOnDropDownCategory(self):
            self.driver.find_element(By.XPATH, self.drpDownCategory_xpath).click()
            
            
    def clickOnDownSelectCategory(self):
            self.driver.find_element(By.XPATH, self.drpDownSelectCategory_xpath).click()
            
    
            
    def clickOnCategoryDownArrow(self):
            self.driver.find_element(By.XPATH, self.btnCategoryDownArrow_xpath).click()
            
            
    def setEnterReorderPoint(self,reorderPoint):
            self.driver.find_element(By.XPATH, self.txtEnterReorderPoint_xpath).send_keys(reorderPoint)
            
    
    def clickOnEnterReorderPointDownArrow(self):
            self.driver.find_element(By.XPATH, self.btnEnterReorderPointDownArrow_xpath).click()
            
    
    def setEnterReorderValue(self,reorderValue):
            self.driver.find_element(By.XPATH, self.txtEnterReorderValue_xpath).send_keys(reorderValue)
            
    
    def clickOnEnterReorderValue(self):
            self.driver.find_element(By.XPATH, self.btnEnterReorderValue_xpath).click()
            
    
    def clickOnDropDownSize(self):
            self.driver.find_element(By.XPATH, self.drpDownSize_xpath).click()
            
    
    def clickOnSelectDropDownSize(self):
            self.driver.find_element(By.XPATH, self.drpDownSelectSize_xpath).click()
            
    def clickOnSizeDownArrow(self):
            self.driver.find_element(By.XPATH, self.btnSizeDownArrow_xpath).click()
 
 #click on Bulk Update Button
            
    def clickOnUpdate(self):
            self.driver.find_element(By.XPATH, self.btnUpdate_xpath).click()
            
            
    def clickOnUpdatingBulkItemsDilogBox_Close(self):
            self.driver.find_element(By.XPATH, self.btnUpdatingBulkItemsDilogBox_Close_xpath).click()
            
    
    
            
    

    
    
    
    