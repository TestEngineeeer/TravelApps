"""Test framework for phptravels.net"""

import unittest
import argparse
import sys
from pages.admin_login_page import AdminLoginPage
from pages.customer_login_page import CustomerLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.customers_page import CustomersPage
from pages.tours_page import ToursPage


class Test(unittest.TestCase, AdminLoginPage, CustomerLoginPage, AdminDashboardPage, CustomersPage, ToursPage):
    def setUp(self):
        self.addCleanup(self.cleanup)
        self.driver = self.get_driver(browser)

    def cleanup(self):
        self.driver.close()

    def testAddNewCustomer(self):
        self.driver.get("http://phptravels.net/admin")

        login_page = AdminLoginPage(self.driver)
        login_page.assert_we_on_admin_login_page("Administator Login")

        admin_page = login_page.login('admin@phptravels.com', 'demoadmin')
        admin_page.assert_we_on_admin_dashboard_page("Dashboard")

        customers_page = admin_page.go_to_customers_page()
        customers_page.assert_we_on_customers_management_page("Customers Management")
        customers_page.add_new_customer("rustam", "testtest@gmail.com")
        customers_page.assert_customer_exist("testtest@gmail.com")

    def testAddNewCustomerTour(self):
        self.driver.get("http://phptravels.net/admin")

        login_page = AdminLoginPage(self.driver)
        login_page.assert_we_on_admin_login_page("Administator Login")

        admin_page = login_page.login('admin@phptravels.com', 'demoadmin')
        admin_page.assert_we_on_admin_dashboard_page("Dashboard")

        tours_page = admin_page.go_to_tours_page()
        tours_page.assert_we_on_tours_management_page("Tours Management")
        tours_page.add_new_tour("rustam", "Rustam's New Tour")
        tours_page.assert_tour_exist("Rustam's New Tour")

    def testBookTourAsNewCustomer(self):
        self.driver.get("http://phptravels.net/login")

        login_page = CustomerLoginPage(self.driver)
        login_page.assert_we_on_customer_login_page("Login")

        user_page = login_page.login("testtest@gmail.com", '123456')
        user_page.assert_we_on_user_page("My Account")
        user_page.search_for_tour("Kauai")
        user_page.book_tour("Rustam Nafikov", "Rustam's New Tour")
        user_page.assert_booking_succeeded("Rustam's New Tour")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Demo Test Framework for Travelers WebSite")
    parser.add_argument('--browser', default="firefox")
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    browser = args.browser

    sys.argv[1:] = args.unittest_args
    unittest.main()
