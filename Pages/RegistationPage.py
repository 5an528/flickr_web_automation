from Locators.locators import RegistrationPageLocators
from Pages.HomePage import HomePage


class RegistrationPage(HomePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = RegistrationPageLocators
        super(RegistrationPage, self).__init__(driver)

    def click_on_signup(self):
        self.find_element(*self.locator.SIGNUP_BTN).click()

    def enter_first_name(self, name):
        self.find_element(*self.locator.FIRST_NAME).send_keys(name)

    def enter_last_name(self, last):
        self.find_element(*self.locator.LAST_NAME).send_keys(last)

    def enter_age(self, age):
        self.find_element(*self.locator.AGE).send_keys(age)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_on_signUp_btn(self):
        self.find_element(*self.locator.SIGNUP_CONFIRM).click()
