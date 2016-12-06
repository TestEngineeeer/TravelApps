from helpers.helper import Helper
from locators.locators import LoginPageLocators as lp
from pages.admin_dashboard_page import AdminDashboardPage


class AdminLoginPage(Helper):
    def login(self, username, password):
        self.type(username, lp.ADMIN_NAME_FIELD)
        self.type(password, lp.PASSWORD_FIELD)
        elem = self.get_element(lp.ADMIN_LOGIN_BUTTON)
        elem.click()
        return AdminDashboardPage(self.driver)

    def assert_we_on_admin_login_page(self, page_name):
        self.assert_page_loaded(page_name, lp.ADMIN_NAME_FIELD)
