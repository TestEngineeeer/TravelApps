from helpers.helper import Helper
from locators.locators import DashboardLocators as db
from pages.customers_page import CustomersPage
from pages.tours_page import ToursPage


class AdminDashboardPage(Helper):
    def assert_we_on_page(self, page_name):
        self.assert_page_loaded(page_name, db.ACCOUNTS_BUTTON)

    def go_to_customers_page(self):
        self.click(db.ACCOUNTS_BUTTON)
        self.click(db.CUSTOMERS_BUTTON)
        return CustomersPage(self.driver)

    def go_to_tours_page(self):
        self.click(db.TOURS_BUTTON)
        self.click(db.TOURS_BUTTON2)
        return ToursPage(self.driver)

