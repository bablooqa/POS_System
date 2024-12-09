from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Keyboard:

    def __init__(self, driver):
        self.driver = driver

        # copy the barcode of 1st stockcode input field

    def selectAll(self):
        self.action = ActionChains(self.driver)
        self.action.key_down(Keys.CONTROL)
        self.action.send_keys("a")
        self.action.key_up(Keys.CONTROL).perform()

    def copydata(self):
        self.action = ActionChains(self.driver)
        self.action.key_down(Keys.CONTROL)
        self.action.send_keys("c")
        self.action.key_up(Keys.CONTROL)
        self.action.perform()

        # def pasteBarcode(self):
        #     self.action=ActionChains(self.driver)
        #     self.action.send_keys(Keys.TAB)
        #     self.action.perform()

    def pasteData(self):
        self.action = ActionChains(self.driver)
        self.action.key_down(Keys.CONTROL)
        self.action.send_keys("v")
        self.action.key_up(Keys.CONTROL)
        self.action.perform()

    def pressEnter(self):
        self.action = ActionChains(self.driver)
        self.action.key_down(Keys.ENTER)
        self.action.key_up(Keys.ENTER)
        self.action.perform()

