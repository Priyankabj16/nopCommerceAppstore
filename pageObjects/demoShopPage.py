from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Demoshop:
    lnkFrontend_xpath = "//span[normalize-space()='Frontend']"
    btnComputers_xpath = "(//a[normalize-space()='Computers'])[1]"
    btndesktops_xpath = "h2[class='title'] a[title='Show products in category Desktops']"
    btnAddtocart_xpath = "(//button[@type='button'][normalize-space()='Add to cart'])" # 3
    btnItemstext_xpath = "//div[@class='item-grid']//h2[@class='product-title']" # 3
    drpProcessor_css = "#product_attribute_1"
    drpRAM_css = "#product_attribute_2"
    selectHDD1_css = "#product_attribute_3_6"
    selectHDD2_css = "#product_attribute_3_7"
    selectOS1_css = "#product_attribute_4_8"
    selectOS2_css = "#product_attribute_4_9"
    selectSoftware_css = "#product_attribute_5_10"
    btnFinalAddtocart_css = "#add-to-cart-button-1"
    btnShoppingCart_css = ".cart-label"
    shoppingcartmsg_css = ".content"
    shoppingcartmsgclose_css = "span[title='Close']"
    btnagreeterms_css = "#termsofservice"
    btncheckout_css = "#checkout"

    # Billing Address

    firstName_xpath = "//input[@id='BillingNewAddress_FirstName']"
    lastName_xpath = "//input[@id='BillingNewAddress_LastName']"
    email_xpath = "//input[@id='BillingNewAddress_Email']"
    companyName_xpath = "//input[@id='BillingNewAddress_Company']"
    drpCountryName_xpath = "//select[@id='BillingNewAddress_CountryId']"
    drpStateName_xpath = "//select[@id='BillingNewAddress_CountryId']"
    cityName_xpath = "//input[@id='BillingNewAddress_City']"
    address1_css = "#BillingNewAddress_Address1"
    zipcode_xpath = "//input[@id='BillingNewAddress_ZipPostalCode']"
    phoneNumber_xpath = "//input[@id='BillingNewAddress_PhoneNumber']"
    btnContinue1_xpath = "//button[@onclick='Billing.save()']"

    # shipping options 3
    optionShipping_xpath = "//div[@class='method-name']/input[@name='shippingoption']"
    btnContinue2_css = ".button-1.shipping-method-next-step-button"
    btnContinue3_css = "button[class='button-1 payment-method-next-step-button']"
    btnContinue4_css = ".button-1.payment-info-next-step-button"

    btnConfirm_xpath = "//button[normalize-space()='Confirm']"
    btnContinue5_xpath = "//button[normalize-space()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def clickFrontEnd(self):
        self.driver.find_element(By.XPATH, self.lnkFrontend_xpath).click()

    def clickItems(self):
        self.driver.find_element(By.XPATH, self.btnComputers_xpath).click()
        self.driver.find_element(By.XPATH, self.btndesktops_xpath).click()
        
    def cartingitemName(self):
        self.driver.find_element(By.XPATH, self.btnItemstext_xpath)

    def Addtocart(self):
        self.driver.find_element(By.XPATH, self.btnAddtocart_xpath)

    def cartItemdetails(self, value1, value2):
        drp = Select(self.driver.find_element(By.XPATH, self.drpProcessor_css))
        drp.select_by_visible_text(value1)

        drp = Select(self.driver.find_element(By.XPATH, self.drpRAM_css))
        drp.select_by_visible_text(value2)

    def selectHDD1(self):
        self.driver.find_element(By.CSS_SELECTOR, self.selectHDD1_css).click()

    def selectHDD2(self):
        self.driver.find_element(By.CSS_SELECTOR, self.selectHDD2_css).click()

    def selectOS1(self):
        self.driver.find_element(By.CSS_SELECTOR, self.selectOS1_css).click()

    def selectOS2(self):
        self.driver.find_element(By.CSS_SELECTOR, self.selectOS2_css).click()

    def selectSoftware(self):
        self.driver.find_element(By.CSS_SELECTOR, self.selectSoftware_css).click()

    def clickFinalAddtocart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btnFinalAddtocart_css).click()
        self.driver.find_element(By.CSS_SELECTOR, self.shoppingcartmsgclose_css).click()

    def clickShoppingCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btnShoppingCart_css).click()
        self.driver.find_element(By.CSS_SELECTOR, self.btnagreeterms_css).click()
        self.driver.find_element(By.CSS_SELECTOR, self.btncheckout_css).click()

    def ShippingDetails(self, fname, lname, email, cname, country, state, city, address, zipcode, phnum):
        self.driver.find_element(By.XPATH, self.firstName_xpath).send_keys(fname)
        self.driver.find_element(By.XPATH, self.lastName_xpath).send_keys(lname)
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)
        self.driver.find_element(By.XPATH, self.companyName_xpath).send_keys(cname)

        drp = Select(self.driver.find_element(By.XPATH, self.drpCountryName_xpath))
        drp.select_by_visible_text(country)

        drp = Select(self.driver.find_element(By.XPATH, self.drpStateName_xpath))
        drp.select_by_visible_text(state)

        self.driver.find_element(By.XPATH, self.cityName_xpath).send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, self.address1_css).send_keys(address)
        self.driver.find_element(By.XPATH, self.zipcode_xpath).send_keys(zipcode)
        self.driver.find_element(By.XPATH, self.phoneNumber_xpath).send_keys(phnum)
        self.driver.find_element(By.XPATH, self.btnContinue1_xpath).click()
        self.driver.find_element(By.XPATH, self.btnContinue2_css).click()
        self.driver.find_element(By.XPATH, self.btnContinue3_css).click()
        self.driver.find_element(By.XPATH, self.btnContinue4_css).click()

    def OrderConfirmation(self):
        self.driver.find_element(By.XPATH, self.btnConfirm_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btnContinue5_xpath).click()
