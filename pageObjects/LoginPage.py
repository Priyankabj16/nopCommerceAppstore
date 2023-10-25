from selenium.webdriver.common.by import By

class Login:
    lnkFrontEnd_xpath = "//span[normalize-space()='Frontend']"
    lnkLogin_xpath = "//a[normalize-space()='Log in']"
    email_xpath = "//input[@id='Email']"
    password_xpath = "//input[@id='Password']"
    login_xpath = "//button[normalize-space()='Log in']"
    logout_xpath = "//a[normalize-space()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    def clickFrontEnd(self):
        self.driver.find_element(By.XPATH, self.lnkFrontEnd_xpath).click()

    def clickLoginlink(self):
        self.driver.find_element(By.XPATH, self.lnkLogin_xpath).click()

    def enterEmail(self, username):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
