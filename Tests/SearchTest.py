from Pages.LoginPage import LoginPage
from Pages.SearchPage import SearchPage
from Tests.BasePage import BasePage


class SearchTest(BasePage):

    def test_search_page(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_on_login()
        loginPage.set_email("marazislam8@gmail.com")
        loginPage.click_on_next()
        loginPage.set_password("TestCase0101")
        loginPage.click_sign_in()
        
        search = SearchPage(self.driver)
        search.click_on_searchBar("Harry Porter")
        search.click_on_searchBtn()