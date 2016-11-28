from helpers.helper import Helper
from locators.locators import CustomerLocators as cl


customer = {"First Name": "Rustam",
            "Last Name": "Nafikov"
            }


class UserPage(Helper):
    def assert_we_on_page(self, page_name):
        self.assert_page_loaded(page_name, cl.MY_PROFILE)
        fname = customer.get("First Name")
        lname = customer.get("Last Name")
        self.assert_text_present("Hi, %s %s" % (fname, lname), cl.GREETING_TEXT)

    def search_for_tour(self, name):
        self.click(cl.TOURS)
        self.type(name, cl.LOCATION)
        elem = self.get_element(cl.LOCATION_OPTION)
        elem.click()
        self.select_from_drop_down(1, cl.ADULTS)
        self.select_from_drop_down("Private", cl.TOURTYPE)
        self.click(cl.SEARCH)

        self.assert_text_present("Rustam's New Tour", cl.LISTED_TOUR)
        return self.get_element(cl.LISTED_TOUR)

    def book_tour(self, name, tour_name):
        self.assert_text_present(tour_name, cl.LISTED_TOUR)

        self.click(cl.LISTED_TOUR)
        self.click(cl.BOOK_NOW_BUTTON)
        self.click(cl.CONFIRM_BOOKING)
        self.assert_page_loaded("Invoice", cl.CUSTOMER_DETAIL)
        self.assert_text_present(name, cl.CUSTOMER_DETAIL)

    def assert_booking_succeeded(self, tour_name):
        self.click(cl.USER_MENU)
        self.click(cl.USER_SETTINGS)
        self.assert_text_present(tour_name, cl.USER_BOOKINGS)



