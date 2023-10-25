import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.demoShopPage import Demoshop
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_shop:
    faulthandler.disable()
    baseURL = ReadConfig.getURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_shop(self):
        self.logger.info("  Test_004_shop")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("  Login test has started")
        self.lp = Login(self.driver)
        self.lp.clickFrontEnd()
        self.lp.clickLoginlink()
        self.lp.enterEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("  Login test Completed")
        self.logger.info("  Shopping Process has been started")
        self.sp = Demoshop(self.driver)
        self.sp.clickItems()
        Itemname = self.sp.cartingitemName()
        itemnames = Itemname.text
        i = -1
        for item in itemnames:
            i = i + 1
            if item == "Build your own computer":
                self.sp.Addtocart()[i].click()

        self.sp.cartItemdetails("2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00]",
                                "8GB [+$60.00]")
        self.sp.selectHDD1()
        self.sp.selectOS1()
        self.sp.clickFinalAddtocart()
        self.sp.clickShoppingCart()
        self.logger.info("  Entering the Shipping Details")
        self.sp.ShippingDetails("Admin", "admin", "admin@gmail.com",
                                "abc", "India","Other", "Shivs",
                                "#1313", "50056", "1234567891")
        self.sp.OrderConfirmation()
        self.logger.info("  Successfully entered details")

        self.msg = self.driver.find_element(By.CSS_SELECTOR, ".result").text

        print(self.msg)
        if 'Your order is confirmed' in self.msg:
            assert True
            self.sp.clickContinue()
            self.lp.clickLogout()
            self.driver.close()
            self.logger.info("  Successfully completed the shopping")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_shop.png")
            self.logger.error(" Test Unsuccessful")
            self.sp.clickContinue()
            self.lp.clickLogout()
            self.driver.close()
            assert False
