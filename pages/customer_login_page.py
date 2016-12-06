from helpers.helper import Helper
from pages.user_page import UserPage
from locators.locators import LoginPageLocators as lp


class CustomerLoginPage(Helper):
    def login(self, username, password):
        self.type(username, lp.USER_NAME_FIELD)
        self.type(password, lp.PASSWORD_FIELD)
        elem = self.get_element(lp.USER_LOGIN_BUTTON)
        elem.click()
        return UserPage(self.driver)

    def assert_we_on_customer_login_page(self, page_name):
        self.assert_page_loaded(page_name, lp.USER_NAME_FIELD)

