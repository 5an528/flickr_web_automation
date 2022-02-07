from Pages.RegistationPage import RegistrationPage
from Tests.BasePage import BasePage


class RegistrationTest(BasePage):

    def test_registration_page(self):
        registration = RegistrationPage(self.driver)
        registration.click_on_signup()
        registration.enter_first_name("Miraz")
        registration.enter_last_name("Islam")
        registration.enter_age("20")
        registration.enter_email("marazislam8@gmail.com")
        registration.enter_password("TestCase01")
        registration.click_on_signUp_btn()
