from Locators.locators import UploadPageLocators
from Pages.HomePage import HomePage


class UploadPhotoPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = UploadPageLocators
        super(UploadPhotoPage, self).__init__(driver)

    def set_choose_photo(self, photo):
        self.find_element(*self.locator.SELECT_PHOTO).send_keys(photo)

    def upload_btn(self):
        self.find_element(*self.locator.UP_BTN).click()

    def upload(self):
        self.find_element(*self.locator.UPLOAD).click()
