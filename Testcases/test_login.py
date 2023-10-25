import pytest
import faulthandler
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_login:
    faulthandler.disable()
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self):
        self.logger.info("  Test_002_Login")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("  Login Test has been started")
        self.lp = Login(self.driver)
        self.lp.clickFrontEnd()
        self.lp.clickLoginlink()
        self.lp.enterEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "nopCommerce demo store":
            assert True
            self.logger.info("  Login test Successful")
            self.lp.clickLogout()
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_scr.png")
            self.logger.error("  Test unsuccessful")
            self.driver.close()
            assert False
