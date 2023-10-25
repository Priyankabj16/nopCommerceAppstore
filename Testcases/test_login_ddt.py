import faulthandler
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities import XlUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test002_DDT_Login:
    faulthandler.disable()
    baseURL = ReadConfig.getURL()
    path = "Testdata/loginddt.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self):
        self.logger.info("  Test_003_login_ddt test")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = XlUtils.getRowcount(self.path, 'Sheet1')
        print("number of rows in Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.user = XlUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XlUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XlUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.enterEmail(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

        if self.driver.title == "nopCommerce demo store" and self.exp == "Pass":
            self.logger.info("  Login Test Passed")
            self.act = XlUtils.writeData(self.path, 'Sheet1', r, 4, 'Pass')
            self.lp.clickLogout()
        elif self.driver.title != "nopCommerce demo store" and self.exp == "Fail":
            self.act = XlUtils.writeData(self.path, 'Sheet1', r, 4, 'Pass')
            self.lp.clickLogout()
