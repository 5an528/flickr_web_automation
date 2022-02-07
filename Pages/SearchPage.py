import time

from Locators.locators import SearchPageLocator
from Pages.HomePage import HomePage


class SearchPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = SearchPageLocator
        super(SearchPage, self).__init__(driver)

    def click_on_searchBar(self, search):
        time.sleep(5)
        self.find_element(*self.locator.SEARCH_BAR).send_keys(search)

    def click_on_searchBtn(self):
        self.find_element(*self.locator.SEARCH_BTN).click()