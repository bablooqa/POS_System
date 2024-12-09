from selenium.webdriver.common.by import By


class Keypad:
    btn_one_xpath = "//body/div[32]/div[3]/button[1]"
    btn_two_xpath = "//body/div[32]/div[3]/button[2]"
    btn_three_xpath = "//body/div[32]/div[3]/button[3]"
    btn_four_xpath = "//body/div[32]/div[2]/button[1]"
    btn_five_xpath = "//body/div[32]/div[2]/button[2]"
    btn_six_xpath = "//body/div[32]/div[2]/button[3]"
    btn_seven_xpath = "//body/div[32]/div[1]/button[1]"
    btn_eight_xpath = "//body/div[32]/div[1]/button[2]"
    btn_nine_xpath = "//body/div[32]/div[1]/button[3]"
    btn_dicmal_xpath = "//body/div[32]/div[4]/button[1]"
    btn_dash_xpath = "//button[contains(text(),'-')]"
    btn_back_xpath = "//button[contains(text(),'|<')]"
    btn_next_xpath = "//button[contains(text(),'>|')]"
    btn_cancel_xpath = "//body/div[32]/div[3]/button[4]"
    btn_clear_xpath = "//body/div[32]/div[2]/button[4]"
    btn_enter_xpath = "//button[contains(text(),'Enter')]"

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def clickOne(self):
        self.driver.find_element(By.XPATH, self.btn_one_xpath).click()

    @staticmethod
    def clickTwo(self):
        self.driver.find_element(By.XPATH, self.btn_two_xpath).click()

    @staticmethod
    def clickThree(self):
        self.driver.find_element(By.XPATH, self.btn_three_xpath).click()

    @staticmethod
    def clickFour(self):
        self.driver.find_element(By.XPATH, self.btn_four_xpath).click()

    @staticmethod
    def clickFive(self):
        self.driver.find_element(By.XPATH, self.btn_five_xpath).click()

    @staticmethod
    def clickSix(self):
        self.driver.find_element(By.XPATH, self.btn_six_xpath).click()

    @staticmethod
    def clickSeven(self):
        self.driver.find_element(By.XPATH, self.btn_seven_xpath).click()

    @staticmethod
    def clickEight(self):
        self.driver.find_element(By.XPATH, self.btn_eight_xpath).click()

    @staticmethod
    def clickNine(self):
        self.driver.find_element(By.XPATH, self.btn_nine_xpath).click()

    @staticmethod
    def clickEnter(self):
        self.driver.find_element(By.XPATH, self.btn_enter_xpath).click()

    @staticmethod
    def clickClear(self):
        self.driver.find_element(By.XPATH, self.btn_clear_xpath).click()

    @staticmethod
    def clickCancel(self):
        self.driver.find_element(By.XPATH, self.btn_cancel_xpath).click()

    @staticmethod
    def clickBack(self):
        self.driver.find_element(By.XPATH, self.btn_back_xpath).click()

    @staticmethod
    def clickNext(self):
        self.driver.find_element(By.XPATH, self.btn_next_xpath).click()
