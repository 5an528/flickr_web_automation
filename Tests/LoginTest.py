from Pages.LoginPage import LoginPage
from Tests.BasePage import BasePage


class LoginTest(BasePage):
    def test_login_page(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_on_login()
        loginPage.set_email("marazislam8@gmail.com")
        loginPage.click_on_next()
        loginPage.set_password("TestCase0101")
        loginPage.click_sign_in()
