from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddItem:
#Add Item Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_menuitem_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]"
    btnAddn_xpath = "//button[normalize-space()='Add']"
    
    txtStockcode_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    addStockCode_PlusIcon_xpath = "//button[contains(@title,'Add Stock Code')]"
    click_barcode_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/img[1]"
    stockCode3_xpath="/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]"

    txtName_xpath = "//input[@placeholder='Name']"
    txtQtyonHand_xpath = "//input[@placeholder='Qty On Hand (Items)']"
    txtQtyonHand2_xpath = "//input[@placeholder='Qty On Hand (Cases)']"
    # txtName_xpath = "/html/body/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div[2]/div/input"
    txtPrice_xpath = "//input[@placeholder='Price']"
    txtAvgCost_xpath = "//input[@placeholder='Avg Cost']"
    txtMargin = "//input[@placeholder='Margin']"
    txtMarkup = "//input[@placeholder='Markup']"
    txtLatestCost_xpath="//input[@placeholder='Latest Cost']"
    
    #Click On Dropdown
    click_On_ItemSizeDrp_xpath="//div[@class='modal-content']//div[1]//div[6]//div[1]//div[1]//div[1]//div[2]//div[1]"
    click_On_ItemCategoryDrp_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div[7]/div/div/div/div[2]/div"
    click_On_ItemSupplierDrp_xpath="//div[@class='modal-content']//div[1]//div[8]//div[1]//div[1]//div[1]//div[2]//div[1]"
    click_On_ItemTax_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div[9]/div/div/div/div[2]/div"
    click_On_ItemRank_xpath="//div[@class='mb-4 custom-react-select col-md-2']//div//div[@class='react-select__indicator react-select__dropdown-indicator css-1xc3v61-indicatorContainer']"
    
    
    #Dropdown XPath Selector
    drpSlect_ItemSize_xpath="//div[normalize-space()='1000L']"
    drpSelect_ItemCategory_xpath="//div[normalize-space()='WINE 750ML']"
    drpSelect_ItemSupplier_xpath="//div[normalize-space()='PRIME WINES & SPIRITS']"
    drpSelect_ItemTax_xpath="//div[normalize-space()='HighTax']"
    drpSelect_ItemRank_xpath="//div[normalize-space()='B']"
    
    iconAddModifier_xpath = "//a[contains(@class,'space-left3')]"
    txtMod2Qty_xpath = "//tbody[2]/tr[1]/td[2]/input"
    txtMod2Price = "//tbody[2]/tr[1]/td[6]/input"
    txtMod2AvgCost = "//tbody[2]/tr[1]/td[6]/input"
      
    txtMod2Margin_xpath = "//input[@placeholder='Margin']"
    txtMod2Markup_xpath = "//input[@placeholder='Markup']"
    drpItemSize_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]"
    
    txtVendorItemNo_xpath = "//input[@placeholder='Vendor Item No']"
    txtItemSKU_xpath = "//input[@placeholder='SKU']"
    txtUnitPerCase_xpath = "//input[@placeholder='Units Per Case']"
    txtCaseCostTotal_xpath = "//input[@placeholder='Case Cost Total']"
    #txtItemTax_xpath = "//div[@class='react-select__control react-select__control--is-focused css-1pahdxg-control']//div[@class='react-select__input-container css-ackcql']"
    txtRpoint_xpath = "//input[@placeholder='Reorder Point']"
    txtRvalue_xpath = "//input[@placeholder='Reorder Value']"
    checkAddAnotherItem_xpath="//input[@id='addanotheritem']"
    checkbox_PrintLabel_xpath="//input[@id='printlabel']"
   
    btnSave_xpath = "//button[normalize-space()='Save']"
    liOptions_xpath = "//a[normalize-space()='Options']"

  #Items-Options
    # Item>Options:checkbox name
    chkbox_DoNotAutoUpdate_xpath = "//input[@id='autoupdate']"
    chkbox_DoNotTrackInv_xpath = "//input[@id='donottrackinventory']"
    chkbox_AddToShortcutKey_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]"
    click_ShortcutColor_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]"
    select_color_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[4]/div[7]/span[1]/div[1]s"
    chkbox_CloseOutItem_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/div[1]/div[1]/div[4]/input[1]"
    chkbox_DoNotDiscount_xpath = "//input[@id='donotdiscount']"
    chkbox_DoNotShowToWebstore_xpath = "//input[@id='showtoweb']"
    chkbox_HideInventory_xpath = "//input[@id='hideinventory']"
    chkbox_EBTEligible_xpath = "//input[@id='ebteligible']"
    
    txt_DefaultQty_xpath = "//input[@placeholder='Default Qty']"
    txt_MinPrice_xpath = "//input[@placeholder='Min Price']"
    # remindDate_Picker_xpath="//body/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
    # selectDate_xpath="//td[contains(text(),'16')]"   
    txt_VendorItmName_xpath = "//input[@placeholder='Vendor Item Name']"
    txtarea_Notes_xpath = "//textarea[@placeholder='Notes']"
    
    #Clicking Options Tag Dropdown
    click_On_OptionsTag_xpath = "(//div[@aria-hidden='true'])[10]"
    click_On_OptionsIType_xpath="/html/body/div[3]/div/div/div[2]/form/div[2]/div[2]/div[4]/div[5]/div/div/div/div[2]/div"
    
    #selecting Options Tag
    drpSelect_OptionsTag_xpath="//div[contains(text(),'Neha460Tag')]"
    drpSelect_OptionsIType_xpath="//div[contains(text(),'Excise Duty')]"
    
    #Search Added Item Name
    searchInput_xpath="//input[@id='search-bar-0']"
  
    #Expend Searched Item
    expendItem_xpath="(//img[@alt='plus icon'])[1]"
    closedExpendItem_xpath="//thead/tr[1]/th[1]/img[1]"
    
    #Click On Cross Icom of Search Bar   
    searchClear_xpath="//button[contains(text(),'Clear')]"
  
  #Starting Function || Created By: Neha singh
  
    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkItems_menuitem_xpath).click()

    def clickOnAdd(self):
        self.driver.find_element(By.XPATH, self.btnAddn_xpath).click()

    def setStockcode(self, stockcode):
        self.driver.find_element(By.XPATH, self.txtStockcode_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtStockcode_xpath).send_keys(stockcode)
    
    
        
    def clickAddStockCodePlusIcon(self):
        self.driver.find_element(By.XPATH, self.addStockCode_PlusIcon_xpath).click()

    def setStockcodeByBarCode(self):
        self.driver.find_element(By.XPATH, self.click_barcode_xpath).click()
    
    def setStockcode3(self):
        self.driver.find_element(By.XPATH, self.stockCode3_xpath).click()
    
    
        
        
        #for margin & markup  ******code starts here.
    
    def setMargin(self, margin):
        self.driver.find_element(By.XPATH, self.txtMod2Margin_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtMod2Margin_xpath).send_keys(margin)
        
        
    def setMarkup(self, markup):
            self.driver.find_element(By.XPATH, self.txtMod2Markup_xpath).clear()
            self.driver.find_element(By.XPATH, self.txtMod2Markup_xpath).send_keys(markup)
            
    def setLatestCost(self, markup):
            self.driver.find_element(By.XPATH, self.txtLatestCost_xpath).clear()
            self.driver.find_element(By.XPATH, self.txtLatestCost_xpath).send_keys(markup)


    #Function for clicking on Dropdown 
    def clickOnItemSize_Drp(self):
            self.driver.find_element(By.XPATH, self.click_On_ItemSizeDrp_xpath).click()
            
    def clickOnItemCategory_Drp(self):
            self.driver.find_element(By.XPATH, self.click_On_ItemCategoryDrp_xpath).click()
            
    def clickOnItemSupplier_Drp(self):
            self.driver.find_element(By.XPATH, self.click_On_ItemSupplierDrp_xpath).click()
    
    def clickOnItemTax_Drp(self):
            self.driver.find_element(By.XPATH, self.click_On_ItemTax_xpath).click()
    
    def clickOnItemRank_Drp(self):
            self.driver.find_element(By.XPATH, self.click_On_ItemRank_xpath).click()
            
            
            
            
    
    #Function for Dropdon Selector 
    def setDrpItemSize(self):
            self.driver.find_element(By.XPATH, self.drpSlect_ItemSize_xpath).click()
    
    def setDrpItemCategory(self):
            self.driver.find_element(By.XPATH, self.drpSelect_ItemCategory_xpath).click()
    
    def setDrpItemSupplier(self):
            self.driver.find_element(By.XPATH, self.drpSelect_ItemSupplier_xpath).click()
    
    def setDrpItemTax(self):
            self.driver.find_element(By.XPATH, self.drpSelect_ItemTax_xpath).click()

    def setDrpItemRank(self):
            self.driver.find_element(By.XPATH, self.drpSelect_ItemRank_xpath).click()
    
    
    
    

    def setQtyOnHand(self, qtyonhand):
        self.driver.find_element(By.XPATH, self.txtQtyonHand_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtQtyonHand_xpath).send_keys(qtyonhand)

    

    def setQtyOnHand2(self, qtyonhand2):
        self.driver.find_element(By.XPATH, self.txtQtyonHand2_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtQtyonHand2_xpath).send_keys(qtyonhand2)

    def setName(self, name):
        self.driver.find_element(By.XPATH, self.txtName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtName_xpath).send_keys(name)

    def setPrice(self, price):
        self.driver.find_element(By.XPATH, self.txtPrice_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPrice_xpath).send_keys(price)

    def setAvgCost(self, avgcost):
        self.driver.find_element(By.XPATH, self.txtAvgCost_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtAvgCost_xpath).send_keys(avgcost)
     
   
    def setVendorNo(self, vno):
        self.driver.find_element(By.XPATH, self.txtVendorItemNo_xpath).send_keys(vno)

    def setSKU(self, sku):
        self.driver.find_element(By.XPATH, self.txtItemSKU_xpath).send_keys(sku)

    def setUnitPerCase(self, unitpercase):
        self.driver.find_element(By.XPATH, self.txtUnitPerCase_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtUnitPerCase_xpath).send_keys(unitpercase)
        
    def setCaseCostTotal(self, casecosttotal):
        self.driver.find_element(By.XPATH, self.txtCaseCostTotal_xpath).send_keys(casecosttotal)
        
    def setRpoint(self, rpoint):
        self.driver.find_element(By.XPATH, self.txtRpoint_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtRpoint_xpath).send_keys(rpoint)

    def setRvalue(self, rvalue):
        self.driver.find_element(By.XPATH, self.txtRvalue_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtRvalue_xpath).send_keys(rvalue)
    
    def checkedAddAI(self):
        self.driver.find_element(By.XPATH, self.checkAddAnotherItem_xpath).click()
    
    def checked_PL(self):
        self.driver.find_element(By.XPATH, self.checkbox_PrintLabel_xpath).click()

    
   
        # self.driver.execute_script("argument[0].click();", self.savebtn)#not required

    # def sortItemIDcol(self):
    #     itemId = self.driver.find_element(By.XPATH, self.colmnID_xpath)
    #     self.action = ActionChains(self.driver)
    #     self.action.double_click(on_element=itemId).perform()

    # def getNoOfRows(self):
    #     return len(self.driver.find_elements(By.XPATH, self.table_Rows_xpath))

    # def getNoOfColumns(self):
    #     return len(self.driver.find_elements(By.XPATH, self.table_Columns_xpath))
        
    def getItemName(self, name):
        itemname = self.driver.find_element(By.XPATH, self.txtName_xpath).get_attribute('value')
        print("Name=", itemname)
        if name == itemname:
            return True
        else:
            return False
        
        
   
#********************************************Options Tab Start*******************************************
    

    def clickOptions(self):
        self.driver.find_element(By.XPATH, self.liOptions_xpath).click()
        
    def clickDoNotAutoUpdate(self):
        self.driver.find_element(By.XPATH, self.chkbox_DoNotAutoUpdate_xpath).click()
    
    def clickDoNotTrackInv(self):
            self.driver.find_element(By.XPATH, self.chkbox_DoNotTrackInv_xpath).click()
    
    def clickAddToShortcutKey(self):  # Yes, No
        self.driver.find_element(By.XPATH, self.chkbox_AddToShortcutKey_xpath).click()
        
    # def clickShortcutColor(self):
    #     self.driver.find_element(By.XPATH, self.click_ShortcutColor_xpath).click()

    def clickCloseOutItem(self):
        self.driver.find_element(By.XPATH, self.chkbox_CloseOutItem_xpath).click()
        
        
    def clickDoNotDiscount(self):
        self.driver.find_element(By.XPATH, self.chkbox_DoNotDiscount_xpath).click()

    def clickDoNotShowToWebstore(self):
        self.driver.find_element(By.XPATH, self.chkbox_DoNotShowToWebstore_xpath).click()

    def clickHideInventory(self):
        self.driver.find_element(By.XPATH, self.chkbox_HideInventory_xpath).click()

    def clickEBTEligible(self):
        self.driver.find_element(By.XPATH, self.chkbox_EBTEligible_xpath).click()

    def setDefaultQty(self, defaultqty):
        self.driver.find_element(By.XPATH, self.txt_DefaultQty_xpath).send_keys(defaultqty)

    def setMinPrice(self, mprice):
        self.driver.find_element(By.XPATH, self.txt_MinPrice_xpath).send_keys(mprice)
    
    def setRemindDate(self):
        self.driver.find_element(By.XPATH, self.remindDate_Picker_xpath).click()
    
    def setSelectedDate(self):
        self.driver.find_element(By.XPATH, self.selectDate_xpath).click()
    
    
    

    def setVendorItmName(self, vname):
        self.driver.find_element(By.XPATH, self.txt_VendorItmName_xpath).send_keys(vname)

    def setNotes(self, note):
        self.driver.find_element(By.XPATH, self.txtarea_Notes_xpath).send_keys(note)
  
    
    #DropDown Function clicking
    def clickOnOptionsTag_Drp(self):
        self.driver.find_element(By.XPATH, self.click_On_OptionsTag_xpath).click()
    
    def clickOnOptionsIType_Drp(self):
            self.driver.find_element(By.XPATH, self.click_On_OptionsIType_xpath).click()
            
            
    #Selecting Value from dropdown
    def setOptionsTag(self):
        self.driver.find_element(By.XPATH, self.drpSelect_OptionsTag_xpath).click()
    
    def setOptionsIType(self):
            self.driver.find_element(By.XPATH, self.drpSelect_OptionsIType_xpath).click()
    
    
    
    
        
        
    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    
#Get Metthod
    def getName(self):
        self.driver.find_element(By.XPATH, self.txtName_xpath).text
        
        
#Search Added Input Name

    def findAddedItem(self, findName):
        self.driver.find_element(By.XPATH, self.searchInput_xpath).clear()
        self.driver.find_element(By.XPATH, self.searchInput_xpath).send_keys(findName)
        
        
#Expend Added Item

    def expendSearchedItem(self):
        self.driver.find_element(By.XPATH, self.expendItem_xpath).click()
        
  #Closed Expend Added Item      
    def closedExpendedItem(self):
        self.driver.find_element(By.XPATH, self.closedExpendItem_xpath).click()
          
        
        
#clear Search Item
    def clickOnClearSearchedItem(self):
        self.driver.find_element(By.XPATH, self.searchClear_xpath).click()
        
        