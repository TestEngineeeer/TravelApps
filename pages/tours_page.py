from helpers.helper import Helper
from locators.locators import DashboardLocators as db

new_tour = {"rustam":
            {db.TOURNAME_FIELD: "Rustam's New Tour",
             db.TOUR_MAX_ADULT: 1,
             db.TOUR_ADULT_PRICE: 1000
             }
            }


class ToursPage(Helper):
    def assert_we_on_page(self, page_name):
        self.assert_page_loaded(page_name, db.TOURS_MGMT_TAB)

    def search_tour(self, tour_name):
        self.click(db.SEARCH_BUTTON)
        self.type(tour_name, db.SEARCH_FIELD)
        self.click(db.GO_BUTTON)

        return self.get_element(db.CUSTOMER_TABLE)

    def add_new_tour(self, customer_name, tour_name):
        table_element = self.search_tour(tour_name)
        while True:
            if tour_name in table_element.text:
                raise AssertionError("Tour already exist")
            else:
                assert "Entries not found." in table_element.text
                assert tour_name not in table_element.text
            break

        self.click(db.ADD_BUTTON)
        self.select_from_drop_down("Private", db.TOUR_TYPE)
        self.select_from_drop_down("Kauai", db.TOUR_LOCATION)

        for i, k in new_tour.get(customer_name).iteritems():
                self.type(k, i)

        self.click(db.TOUR_SUBMIT_BUTTON)

    def assert_tour_exist(self, tour_name):
        assert tour_name in self.search_tour(tour_name).text, "Tour does not exist"
        self.click(db.RESET_BUTTON)

