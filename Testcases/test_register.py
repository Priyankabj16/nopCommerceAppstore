import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from pageObjects.RegisterPage import register
from utilities.readProperties import ReadConfig


class Test_001_Register:
    faulthandler.disable()
    baseURL = ReadConfig.getURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("  Test_001_Register")
        self.logger.info("  Registration Process has been started")
        self.rs = register(self.driver)
        self.rs.clickFrontEnd()
        self.rs.clickLinkRegister()
        self.rs.genderMale_css()
        self.rs.firstname("Admin")
        self.rs.lastname("admin")
        self.rs.setdobDate("16")
        self.rs.setdobMonth("January")
        self.rs.setdobYear("2000")
        self.rs.setEmail("admin@gmail.com")
        self.rs.setCompanyName("abc")
        self.rs.setPassword("admin123")
        self.rs.setConfirmPassword("admin123")
        self.rs.clickRegister()

        self.msg = self.driver.find_element(By.CSS_SELECTOR, ".result").text

        print(self.msg)
        if 'Your registration completed' in self.msg:
            assert True
            self.rs.clickContinue()
            self.driver.close()
            self.logger.info("  Successfully completed the registration")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_registration.png")
            self.logger.error(" Test Unsuccessful")
            self.driver.close()
            assert False
