from selenium.webdriver.common.by import By


class SignInPageLocators(object):
    LOGIN_BTN = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[2]/a")
    SET_EMAIL = (By.ID, "login-email")
    CLICK_EMAIL_XPATH = (By.XPATH, "//*[@id=\"login-form\"]/button")
    SET_PASS = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[3]/div/div/input")
    CLICK_SIGNIN_BTN = (By.XPATH, "//button[@data-testid='identity-form-submit-button']")


class RegistrationPageLocators(object):
    SIGNUP_BTN = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[3]/a")
    FIRST_NAME = (By.ID, "sign-up-first-name")
    LAST_NAME = (By.ID, "sign-up-last-name")
    AGE = (By.ID, "sign-up-age")
    EMAIL = (By.ID, "sign-up-email")
    PASSWORD = (By.ID, "sign-up-password")
    SIGNUP_CONFIRM = (By.XPATH, "//button[contains(.,'Sign up')]")


class SearchPageLocator(object):
    SEARCH_BAR = (By.XPATH, "//input[@id='search-field']")
    SEARCH_BTN = (By.XPATH, "//label[@aria-label='Search']")


class UploadPageLocators(object):
    SELECT_PHOTO = (By.XPATH, "//input[@id=\"choose-photos-and-videos\"]")
    UP_BTN = (By.ID, "action-publish")
    UPLOAD = (By.ID, "confirm-publish")
