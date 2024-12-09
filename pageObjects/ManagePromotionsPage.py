from multiprocessing.sharedctypes import Value
import time
import zlib

# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys



class ManagePromotions:
#ManagePromotion Bottlepos 5.0
    linkItems_menu_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/a[1]"
    linkItems_menuitem_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[1]"
    btnAddn_xpath = "/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[6]/button[1]"
    refresh_xpath="/html[1]/body[1]/div[1]/main[1]/div[1]/ul[1]/li[1]/button[1]"
    btnManagePromotions_xpath="//button[normalize-space()='Manage Promotions']"
    btnManagePromotionsDialogBox_Close_xpath="//button[normalize-space()='Close']"
    btnManagePromotionsAddPromotion_xpath="//button[contains(text(),'Add Promotion')]"
    
    # General Section of Manage Promotions
    
    txtPromotionName_xpath="//body/div[5]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    drpDownPromotionType_xpath="//body/div[5]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]"
    drpDownPromotionTypeSelect_Doller_Y_Off_X_Qty_xpath="//div[normalize-space()='$Y Off X Qty']"
    drpDownPromotionTypeSelect_Per_Y_Off_X_Qty_xpath="//div[contains(text(),'%Y Off X Qty')]"
    drpDownPromotionTypeSelectFixedItemPricelist_xpath="//div[normalize-space()='Fixed Item Pricelist']"
    startDate_xpath="//input[@name='start_date']"
    startDateSelectToday_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[1]/div[1]/div[3]/div/div/div[2]/div/table/tbody/tr[3]/td[4]"
    endDate_xpath="//input[@name='end_date']"
    endDateSelect_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[1]/div[1]/div[4]/div/div/div[2]/div/table/tbody/tr[5]/td[6]"
    drpDownSelectTax_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[1]/div[1]/div[5]/div/div/div/div[2]/div"
    drpDownSelectTaxValue_xpath="//div[normalize-space()='High Tax']"
    checkBoxGroupPromotion_xpath="//input[@id='group_promotion']"
    checkboxScanData_xpath="//input[@id='scan_data']"
    btnAdd_xpath="//button[normalize-space()='Add']"
    numBulkSaleQty_xpath="//input[@name='Qty']"
    numEnterPromotionPrice_xpath="//input[@name='EnterPromotionPrice']"
    numBulkSaleQty2_xpath="//td[@data-title='Qty']//div[@class='form-floating']//input[1]"
    numEnterPromotionPrice2_xpath="//td[@data-title='Enter Promotion Price']//div[@class='form-floating']//input[1]"
    btnDeleteQtySection_xpath="(//button[@title='delete'])[3]"
    btnDeleteQtySection_No_xpath="//button[normalize-space()='No']"
    btnDeleteQtySection_Yes_xpath="(//button[normalize-space()='Yes'])[1]"
    
    
     # Items Section of Manage Promotions XPATH
    
    btnItemsSection_xpath="//a[contains(text(),'Items')]"
    txtSearch_xpath="//div[contains(@class,'fade items tab-pane active show')]//input[@id='search-bar-0']"
    txtSearchClear_xpath="//button[@class='btn btn-default clear']"
    btnAddSelectedItemsToPromotion_xpath="//button[contains(text(),'Add Selected Items To Promotion')]"
    btnOk_xpath="//button[contains(text(),'OK')]"
    
    
    checkBoxSelectAll_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div/div[4]/div[1]/table/thead/tr/th[1]/input"
    
    btnRemoveAll_xpath="//button[contains(text(),'Remove All')]"
      
    btnClickOnNo_xpath="/html[1]/body[1]/div[7]/div[1]/div[1]/div[3]/button[2]"
    btnClickOnYes_xpath="//button[normalize-space()='Yes']"
    btnAddPlusIcon_xpath="//button[@title='Add Item']//*[name()='svg']//*[name()='path' and contains(@fill,'currentCol')]"
    
    #Shorting Items
    itemsInPromotionNameShorting_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/table/thead/tr/th[1]"
    itemsInPromotionPriceShorting_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/table/thead/tr/th[2]"
    
    
    # Categories Section of Manage Promotions XPATH
    
    btnCategoriesSection_xpath="//a[contains(text(),'Categories')]"
    txtSearchCategory_xpath="(//input[@placeholder='Search'])[4]"
    txtSearchCategoryClear_xpath="(//button[normalize-space()='Clear'])[1]"
    shortCategoriesName_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[3]/div/div[1]/div/div[3]/div[1]/table/thead/tr/th[2]"
    btnAddCategoryPlusIcon_xpath="(//button[contains(@title,'Add Size')])[1]"
    btnRemoveCategory_xpath="//img[@alt='remove']"    
    btnAddSelectedCategoryToPromotion_xpath="//button[normalize-space()='Add Selected Category To Promotion']"
    checkBoxCategorySelectAll_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/form[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/table[1]/thead[1]/tr[1]/th[1]/input[1]"
    shortingCategoriesInPromotion_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/table/thead/tr/th[1]"
    
    
    # Size Section of Manage Promotions XPATH
    
    btnSizeTab_xpath="//a[normalize-space()='Size']"
    txtSearchSize_xpath="(//input[@id='search-bar-0'])[5]"
    shortSizeName_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[4]/div/div[1]/div/div[3]/div[1]/table/thead/tr/th[2]"
    btnAddSizePlusIcon_xpath="(//button[@title='Add Size'])[11]"
    btnRemoveSize_xpath="//img[@alt='delete']"
    btnAddSelectedSizesToPromotion_xpath="//button[normalize-space()='Add Selected Sizes To Promotion']"
    btnSizeOk_xpath="//button[normalize-space()='Ok']"
    checkBoxAddSelectedAllSizesToPromotion_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[4]/div/div[1]/div/div[3]/div[1]/table/thead/tr/th[1]/input"
    shortingSizeInPromotionName_xpath="/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/form[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[1]"
    
    
    
    
     # Tags Section of Manage Promotions XPATH
    btnTagsTab_xpath="//a[normalize-space()='Tags']"
    drpDownTags_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[5]/div/div/div/div/div/div[2]/div"
    drpDownTagsSelector_xpath="//div[contains(text(),'Neha118Tag')]"
    
    #for Cross Button Click XPATH
    removeTagsOne_By_One_xpath="//div[@aria-label='Remove Neha118Tag']//*[name()='svg']"
    removeTagsAll_xpath="(//*[name()='svg'][contains(@class,'css-8mmkcg')])[8]"
    
    #select By Search
    txtSearchTags_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[5]/div/div/div/div/div/div[1]/div[3]/input"
    txtSearchTags2_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[5]/div/div/div/div/div/div[1]/div[4]/input"
    txtSearchTags3_xpath="/html/body/div[5]/div/div/div[2]/form/div[2]/div[5]/div/div/div/div/div/div[1]/div[5]/input"
    
    
    
    
     #  Customers Section of Manage Promotions XPATH
    btnCustomers_xpath="//a[normalize-space()='Customers']"
    
    
    
#Function to click on various Buttions || Created By: Neha Singh
  
    def __init__(self, driver):
        self.driver = driver

    def clickOnItemsMenu(self):
        self.driver.find_element(By.XPATH, self.linkItems_menu_xpath).click()

    def clickOnItemsMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkItems_menuitem_xpath).click()
        
        
    def clickOnRefresh(self):
        self.driver.find_element(By.XPATH, self.refresh_xpath).click()
    
    def clickOnManagePromotions(self):
        self.driver.find_element(By.XPATH, self.btnManagePromotions_xpath).click()

    def clickOnManagePromotionsDialogBox_Close(self):
        self.driver.find_element(By.XPATH, self.btnManagePromotionsDialogBox_Close_xpath).click()
        
    def clickOnManagePromotionsAddPromotions(self):
        self.driver.find_element(By.XPATH, self.btnManagePromotionsAddPromotion_xpath).click()
        
        
         # General Section of Manage Promotions
        
        
    def clickOnPromotionName(self,pName):
        self.driver.find_element(By.XPATH, self.txtPromotionName_xpath).send_keys(pName)   
     
        
    def clickOnPromotionType(self):
        self.driver.find_element(By.XPATH, self.drpDownPromotionType_xpath).click()
       
       
    def clickOnDrpDownPromotionTypeSelect_Doller_Y_Off_X_Qty(self):
        self.driver.find_element(By.XPATH, self.drpDownPromotionTypeSelect_Doller_Y_Off_X_Qty_xpath).click()   
        
    
    def clickOnDrpDownPromotionTypeSelect_Per_Y_Off_X_Qty(self):
            self.driver.find_element(By.XPATH, self.drpDownPromotionTypeSelect_Per_Y_Off_X_Qty_xpath).click()   
       
    
    def clickOnDrpDownPromotionTypeSelectFixedItemPricelist(self):
          self.driver.find_element(By.XPATH, self.drpDownPromotionTypeSelectFixedItemPricelist_xpath).click()    
        
    
    def clickOnStartDate(self):
          self.driver.find_element(By.XPATH, self.startDate_xpath).click() 
    
    def clickOnstartDateSelectToday(self):
          self.driver.find_element(By.XPATH, self.startDateSelectToday_xpath).click() 
        
    def clickOnEndDate(self):
          self.driver.find_element(By.XPATH, self.endDate_xpath).click() 
        
    def clickOnEndDateSelect(self):
          self.driver.find_element(By.XPATH, self.endDateSelect_xpath).click() 
          

    def clickDrpDownSelectTax(self):
        self.driver.find_element(By.XPATH, self.drpDownSelectTax_xpath).click() 
        

    def clickDrpDownSelectTaxValue(self):
                    self.driver.find_element(By.XPATH, self.drpDownSelectTaxValue_xpath).click() 
   
    
    def clickOnCheckBoxGroupPromotion(self):
                    self.driver.find_element(By.XPATH, self.checkBoxGroupPromotion_xpath).click() 
        
    def clickOnCheckBoxScanData(self):
                    self.driver.find_element(By.XPATH, self.checkboxScanData_xpath).click() 
                    
                    
    def clickOnAdd(self):
                    self.driver.find_element(By.XPATH, self.btnAdd_xpath).click() 
    
    
    def clickOnBulkSaleQty(self,bsQty):
                    self.driver.find_element(By.XPATH, self.numBulkSaleQty_xpath).send_keys(bsQty) 
    
    def clickOnnumEnterPromotionPrice(self,epPrice):
                    self.driver.find_element(By.XPATH, self.numEnterPromotionPrice_xpath).send_keys(epPrice) 
        
    
    def clickOnBulkSaleQty2(self,bsQty):
                    self.driver.find_element(By.XPATH, self.numBulkSaleQty2_xpath).send_keys(bsQty) 
    
    def clickOnnumEnterPromotionPrice2(self,epPrice):
                    self.driver.find_element(By.XPATH, self.numEnterPromotionPrice2_xpath).send_keys(epPrice) 
        
    
    def clickDeleteQtySection(self):
                    self.driver.find_element(By.XPATH, self.btnDeleteQtySection_xpath).click() 
        
    
    def clickDeleteQtySection_No(self):
                    self.driver.find_element(By.XPATH, self.btnDeleteQtySection_No_xpath).click()
        

    
    def clickDeleteQtySection_Yes(self):
                    self.driver.find_element(By.XPATH, self.btnDeleteQtySection_Yes_xpath).click()
        


 # Items Section of Manage Promotions
 
 
    def clickOnbtnItemsSection(self):
            self.driver.find_element(By.XPATH, self.btnItemsSection_xpath).click()    
 
    def clickOntxtSearch(self,txtSearch):
            self.driver.find_element(By.XPATH, self.txtSearch_xpath).send_keys(txtSearch)
 
    def clickOntxtSearch_Clear(self):
            self.driver.find_element(By.XPATH, self.txtSearchClear_xpath).click()
        
    
    def clickOnAddSelectedItemsToPromotion(self):
            self.driver.find_element(By.XPATH, self.btnAddSelectedItemsToPromotion_xpath).click()
      
    
    def clickOnAddSelectedItemsToPromotion_Ok(self):
            self.driver.find_element(By.XPATH, self.btnOk_xpath).click()
      
    
    def clickOnCheckBoxSelectAll(self):
            self.driver.find_element(By.XPATH, self.checkBoxSelectAll_xpath).click()
      
    
    def clickOnRemoveAll(self):
            self.driver.find_element(By.XPATH, self.btnRemoveAll_xpath).click()
      
    def clickOnNoBtn(self):
            self.driver.find_element(By.XPATH,self.btnClickOnNo_xpath).click()
            
            
    def clickOnYesBtn(self):
            self.driver.find_element(By.XPATH,self.btnClickOnYes_xpath).click()
    
    
            
    def clickOnAddPlusIcon(self):
            self.driver.find_element(By.XPATH,self.btnAddPlusIcon_xpath).click()
            
            
    
    #Shorting Items In Promotion Shorting
            
    def clickOnItemsInPromotionNameShorting(self):
            self.driver.find_element(By.XPATH,self.itemsInPromotionNameShorting_xpath).click()
    
            
    def clickOnItemsInPromotionPriceShorting(self):
            self.driver.find_element(By.XPATH,self.itemsInPromotionPriceShorting_xpath).click()
    
    
            
 # Categories Section of Manage Promotions
 
 
    def clickOnCategoriesSection(self):
        self.driver.find_element(By.XPATH,self.btnCategoriesSection_xpath).click()
 
    def clickOnCategoriesSearch(self,txtSearch):
        self.driver.find_element(By.XPATH,self.txtSearchCategory_xpath).send_keys(txtSearch)
        
    
    def clickOnCategoriesSearchClear(self):
        self.driver.find_element(By.XPATH,self.txtSearchCategoryClear_xpath).click()
        
    
    def clickOnshortCategoriesName(self):
        self.driver.find_element(By.XPATH,self.shortCategoriesName_xpath).click()
    
    def clickOnAddCategoryPlusIcon(self):
        self.driver.find_element(By.XPATH,self.btnAddCategoryPlusIcon_xpath).click()
    
    def clickOnRemoveCategory(self):
        self.driver.find_element(By.XPATH,self.btnRemoveCategory_xpath).click()
    
    def clickOnAddSelectedCategoryToPromotion(self):
        self.driver.find_element(By.XPATH,self.btnAddSelectedCategoryToPromotion_xpath).click()
        
    
    def clickOncheckBoxCategorySelectAll(self):
        self.driver.find_element(By.XPATH,self.checkBoxCategorySelectAll_xpath).click()
    
    def clickOnshortingCategoriesInPromotion(self):
        self.driver.find_element(By.XPATH,self.shortingCategoriesInPromotion_xpath).click()
        
        
        

 # Size Section of Manage Promotions
 
  
    def clickOnbtnSizeTab(self):
        self.driver.find_element(By.XPATH,self.btnSizeTab_xpath).click()
    
    def clickOnSizeSearch(self,txtSizeSearch):
        self.driver.find_element(By.XPATH,self.txtSearchSize_xpath).send_keys(txtSizeSearch)
        
        
    def clickOnshortSizeName(self):
        self.driver.find_element(By.XPATH,self.shortSizeName_xpath).click()    
        
    def clickOnAddSizePlusIcon(self):
        self.driver.find_element(By.XPATH,self.btnAddSizePlusIcon_xpath).click()    
        
         
    def clickOnRemoveSize(self):
        self.driver.find_element(By.XPATH,self.btnRemoveSize_xpath).click()    
        
            
    
    def clickOnAddSelectedSizesToPromotion(self):
        self.driver.find_element(By.XPATH,self.btnAddSelectedSizesToPromotion_xpath).click()
        
    
    def clickOnSizeOk(self):
        self.driver.find_element(By.XPATH,self.btnSizeOk_xpath).click()
        
    
    def clickOnCheckBoxAddSelectedAllSizesToPromotion(self):
        self.driver.find_element(By.XPATH,self.checkBoxAddSelectedAllSizesToPromotion_xpath).click()
        
    
    def clickOnCheckBoxSizeInPromotionName(self):
        self.driver.find_element(By.XPATH,self.shortingSizeInPromotionName_xpath).click()
        
        
      
       # Tags Section of Manage Promotions  
    
    def clickOnTagsTab(self):
        self.driver.find_element(By.XPATH,self.btnTagsTab_xpath).click()
        
    
    
    def clickOnTagsDrpDown(self):
        self.driver.find_element(By.XPATH,self.drpDownTags_xpath).click()
    
    def clickOnTagsDrpDownSelector(self):
        self.driver.find_element(By.XPATH,self.drpDownTagsSelector_xpath).click()
        
        
    
    def clickOnRemoveTagsOne_By_One(self):
        self.driver.find_element(By.XPATH,self.removeTagsOne_By_One_xpath).click()
        
        
    
    def clickOnremoveTagsAlls(self):
        self.driver.find_element(By.XPATH,self.removeTagsAll_xpath).click()
        
    
    def clickOnTagsSearch(self,txtSearchTags):
        self.driver.find_element(By.XPATH,self.txtSearchTags_xpath).send_keys(txtSearchTags)
        self.driver.find_element(By.XPATH, self.txtSearchTags_xpath).send_keys(Keys.ENTER)
        
    
    def clickOnTagsSearch2(self,txtSearchTags):
        self.driver.find_element(By.XPATH,self.txtSearchTags2_xpath).send_keys(txtSearchTags)
        self.driver.find_element(By.XPATH, self.txtSearchTags2_xpath).send_keys(Keys.ENTER)
    
    def clickOnTagsSearch3(self,txtSearchTags):
        self.driver.find_element(By.XPATH,self.txtSearchTags3_xpath).send_keys(txtSearchTags)
        self.driver.find_element(By.XPATH, self.txtSearchTags3_xpath).send_keys(Keys.ENTER)
        
#Press Enter Key (Not Require Right Now)

    # def pressEnterKey(self):
    #     self.driver.find_element(By.XPATH, self.txtSearchTags_xpath).send_keys(Keys.ENTER)
    
        
    
    
    
    # Customers Section of Manage Promotions  
    
    def clickOnCustomersTab(self):
        self.driver.find_element(By.XPATH,self.btnCustomers_xpath).click()

    
    
    
    
    