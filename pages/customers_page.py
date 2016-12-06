from helpers.helper import Helper
from locators.locators import DashboardLocators as db

new_customer = {"rustam":
                {db.FNAME_FIELD : "Rustam",
                 db.LNAME_FIELD: "Nafikov",
                 db.EMAIL_FIELD: "testtest@gmail.com",
                 db.PWD_FIELD: "123456"
                 }
                }


class CustomersPage(Helper):
    def assert_we_on_customers_management_page(self, page_name):
        self.assert_page_loaded(page_name, db.CUSTOMERS_MGMT_TAB)

    def search_customer(self, email):
        self.click(db.SEARCH_BUTTON)
        self.type(email, db.SEARCH_FIELD)
        self.click(db.GO_BUTTON)
        return self.get_element(db.CUSTOMER_TABLE)

    def add_new_customer(self, name, email):
        table_element = self.search_customer(email)
        while True:
            if email in table_element.text:
                raise AssertionError("Customer already exist")
            else:
                assert "Entries not found." in table_element.text, "It seems there are returned results"
            break

        self.click(db.ADD_BUTTON)

        for i, k in new_customer.get(name).iteritems():
                self.type(k, i)
        self.select_from_drop_down("Albania", db.COUNTRY_LIST_DROP_DOWN)

        self.click(db.SUBMIT_BUTTON)

    def assert_customer_exist(self, email):
        assert email in self.search_customer(email).text, "Customer does not exist"
        self.click(db.RESET_BUTTON)


