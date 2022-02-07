import time

from Locators.locators import SignInPageLocators
from Pages.HomePage import HomePage


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = SignInPageLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_on_login(self):
        self.find_element(*self.locator.LOGIN_BTN).click()

    def set_email(self, email):
        self.find_element(*self.locator.SET_EMAIL).send_keys(email)

    def click_on_next(self):
        self.find_element(*self.locator.CLICK_EMAIL_XPATH).click()

    def set_password(self, password):
        time.sleep(3)
        self.find_element(*self.locator.SET_PASS).send_keys(password)

    def click_sign_in(self):
        self.find_element(*self.locator.CLICK_SIGNIN_BTN).click()


