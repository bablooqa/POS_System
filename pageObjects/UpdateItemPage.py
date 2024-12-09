from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class UpdateItem:
#Add Item Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_menuitem_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]"
    
    # btnUpdateItem_xpath="/html[1]/body[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[15]/div[1]/button[1]/img[1]"
    btnUpdateItem_xpath="/html/body/div/main/div[2]/div/div/div/div[3]/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[17]/div/button[1]/img"
    btnAddn_xpath = "/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[6]/button[1]"
    
    txtStockcode_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    txtName_xpath = "//body/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]"
    txtQtyonHand_xpath = "//input[@placeholder='Qty On Hand (Items)']"
    iconqtyplus_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/*[name()='svg'][1]/*[name()='path'][1]"
    iconStockcode2_xpath = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
    txtQtyonHand2_xpath = "//input[@placeholder='Qty On Hand (Cases)']"
    # txtName_xpath = "/html/body/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div[2]/div/input"
    txtPrice_xpath = "//input[@placeholder='Price']"
    txtAvgCost_xpath = "//input[@placeholder='Avg Cost']"
    txtMargin = "//input[@placeholder='Margin']"
    txtMarkup = "//input[@placeholder='Markup']"
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
    checkbox_PrintLabel_xpath="//input[@id='printlabel']"
   
    btnSave_xpath = "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]"
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
    txt_VendorItmName_xpath = "//input[@placeholder='Vendor Item Name']"
    txtarea_Notes_xpath = "//textarea[@placeholder='Notes']"
    itemSize_dropDown_xpath = "//div[@class='react-select__control react-select__control--is-focused react-select__control--menu-is-open css-1pahdxg-control']//div[@class='react-select__input-container css-ackcql']"
    
  
  
  
  
  
    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkItems_menuitem_xpath).click()
    
    def clickOnItemsUpdate(self):
        self.driver.find_element(By.XPATH, self.btnUpdateItem_xpath).click()

    def updateItemName(self, name):
        self.driver.find_element(By.XPATH, self.txtName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtName_xpath).send_keys(name)
    
    def updateItemQtyOnHand(self, qtyonhand):
        self.driver.find_element(By.XPATH, self.txtQtyonHand_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtQtyonHand_xpath).send_keys(qtyonhand)
    
    def updateItemQtyOnHand2(self, qtyonhand2):
        self.driver.find_element(By.XPATH, self.txtQtyonHand2_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtQtyonHand2_xpath).send_keys(qtyonhand2)
        
    def updateItemPrice(self, price):
        self.driver.find_element(By.XPATH, self.txtPrice_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtPrice_xpath).send_keys(price)
    
    def updateItemVendorNo(self, vno):
        self.driver.find_element(By.XPATH, self.txtVendorItemNo_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtVendorItemNo_xpath).send_keys(vno)
        
    def updateItemSKU(self, sku):
        self.driver.find_element(By.XPATH, self.txtItemSKU_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtItemSKU_xpath).send_keys(sku)
    
    def updateItemUnitPerCase(self, unitpercase):
        self.driver.find_element(By.XPATH, self.txtUnitPerCase_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtUnitPerCase_xpath).send_keys(unitpercase)
    
    def updateItemCaseCostTotal(self, casecosttotal):
        self.driver.find_element(By.XPATH, self.txtCaseCostTotal_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCaseCostTotal_xpath).send_keys(casecosttotal)
    
    def updateItemRpoint(self, rpoint):
        self.driver.find_element(By.XPATH, self.txtRpoint_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtRpoint_xpath).send_keys(rpoint)
    
    def updateItemRvalue(self, rvalue):
        self.driver.find_element(By.XPATH, self.txtRvalue_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtRvalue_xpath).send_keys(rvalue)
    
    def updateItemChecked_PL(self):
        self.driver.find_element(By.XPATH, self.checkbox_PrintLabel_xpath).click()
        
    
    #Function to Click on Item Update Option Section || Created By: Neha Singh
    
    def updateItemclickOptions(self):
        self.driver.find_element(By.XPATH, self.liOptions_xpath).click()
    
    def updateItem_Options_DefaultQty(self, defaultqty):
        self.driver.find_element(By.XPATH, self.txt_DefaultQty_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_DefaultQty_xpath).send_keys(defaultqty)
    
    def updateItem_Options_MinPrice(self, mprice):
        self.driver.find_element(By.XPATH, self.txt_MinPrice_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_MinPrice_xpath).send_keys(mprice)
    
    def updateItem_Options_VendorItemName(self, vname):
        self.driver.find_element(By.XPATH, self.txt_VendorItmName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_VendorItmName_xpath).send_keys(vname)
    
    def updateItem_Options_Notes(self, note):
        self.driver.find_element(By.XPATH, self.txtarea_Notes_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtarea_Notes_xpath).send_keys(note)
    
    def clickkOnUpdate(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
        
    
    
    
    