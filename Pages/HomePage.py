from telnetlib import EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class HomePage(object):
    def __init__(self, driver, base_url=""):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_all_element(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            var = EC.visibility_of_all_elements_located
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def get_Text(self, locator):
        return self.driver.locator.text

    def sendkeys(self, path, value):
        self.driver.find_element(path).send_keys(value)

    def rightClick(self, locator):
        element = self.find_element(locator)
        rightclick = ActionChains(self.driver).move_to_element(element)
        rightclick.context_click().perform()
        # actionChains.move_to_element(*self.find_element(*self.locator.catalog)).perform()
        # actionChains.context_click().perform()

    def acceptAlertMsg(self):
        obj = self.driver.switch_to.alert
        obj.accept()

    # def selectFromDropdown(self, path, value):
    #     select_fr = Select(self.driver.find_element(path))
    #     select_fr.select_by_value(value)
    def Accept_Alert(self):
        self.driver.switch_to.alert.accept()

    def javaScriptAccept_alert(self):
        self.driver.execute_script("window.confirm = function(){return true;}")

    def isDisplayed(self, *locator):
        return self.driver.find_element(*locator).is_displayed()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, data, *locator):
        self.driver.find_element(*locator).send_keys(data)

    def change_frame(self, locator):
        self.driver.switch_to.frame(locator)

    def wait(self, time):
        self.driver.implicitly_wait(time)

    def change_to_default_frame(self):
        self.driver.switch_to.default_content()

    #  wait till visibility_of_element_located
    def wait_till_visibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.visibility_of_element_located(*locator))
        return element