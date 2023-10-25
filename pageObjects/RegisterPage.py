from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class register:
    lnkFrontend_xpath = "//span[normalize-space()='Frontend']"
    lnkregister_css = ".ico-register"
    genderMale_css = "#gender-male"
    genderFemale_css = "#gender-female"
    firstName_css = "#FirstName"
    lastName_css = "#LastName"
    drpdob_date_css = "select[name='DateOfBirthDay']"
    drpdob_month_css = "select[name='DateOfBirthMonth']"
    drpdob_year_css = "select[name='DateOfBirthYear']"
    email_css = "#Email"
    companyName_css = "#Company"
    password_css = "#Password"
    confirmPassword_css = "#ConfirmPassword"
    register_css = "#register-button"
    confirmedRegistermsg_css = ".result"
    btncontinue_css = ".button-1.register-continue-button"

    def __init__(self, driver):
        self.driver = driver

    def clickFrontEnd(self):
        self.driver.find_element(By.XPATH, self.lnkFrontend_xpath).click()

    def clickLinkRegister(self):
        self.driver.find_element(By.CSS_SELECTOR, self.lnkregister_css).click()

    def genderMale(self):
        self.driver.find_element(By.CSS_SELECTOR, self.genderMale_css).click()

    def genderFemale(self):
        self.driver.find_element(By.CSS_SELECTOR, self.genderFemale_css).click()

    def firstname(self, fname):
        self.driver.find_element(By.CSS_SELECTOR, self.firstName_css).send_keys(fname)

    def lastname(self, lname):
        self.driver.find_element(By.CSS_SELECTOR, self.lastName_css).send_keys(lname)

    def setdobDate(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpdob_date_css))
        drp.select_by_visible_text(value)

    def setdobMonth(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpdob_month_css))
        drp.select_by_visible_text(value)

    def setdobYear(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpdob_year_css))
        drp.select_by_visible_text(value)

    def setEmail(self, value):
        self.driver.find_element(By.CSS_SELECTOR, self.email_css).send_keys(value)

    def setCompanyName(self, value):
        self.driver.find_element(By.CSS_SELECTOR, self.companyName_css).send_keys(value)

    def setPassword(self, value):
        self.driver.find_element(By.CSS_SELECTOR, self.password_css).send_keys(value)

    def setConfirmPassword(self, value):
        self.driver.find_element(By.CSS_SELECTOR, self.password_css).send_keys(value)

    def clickRegister(self):
        self.driver.find_element(By.CSS_SELECTOR, self.lnkregister_css).click()

    def clickContinue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btncontinue_css).click()