from Pages.LoginPage import LoginPage
from Pages.SearchPage import SearchPage
from Pages.UploadPhotoPage import UploadPhotoPage
from Tests.BasePage import BasePage


class UploadPhotoTest(BasePage):

    def test_upload_photo_page(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_on_login()
        loginPage.set_email("marazislam8@gmail.com")
        loginPage.click_on_next()
        loginPage.set_password("TestCase0101")
        loginPage.click_sign_in()

        uploadPhoto = UploadPhotoPage(self.driver)
        uploadPhoto.set_choose_photo("C:\Users\Lenovo\Pictures\Screenshots\up.png")
        uploadPhoto.upload_btn()
        uploadPhoto.upload()
