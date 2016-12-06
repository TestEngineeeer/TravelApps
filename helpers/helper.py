from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

TIMEOUT = 20
SLEEP_TIME = 0.5

class Helper(object):
    def __init__(self, driver):
        self.driver = driver

    def get_driver(self, browser):
        """ Get driver for a specified browser
        Args:
             browser: firefox/chrome
        Return:
             driver
        """
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser =="chrome":
            self.driver = webdriver.Chrome("/path/to/chromedriver")
        return self.driver

    def get_element(self, locator):
        """ Locate and return element
        Args:
            locator: locator
        Return:
            element
        """
        return WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """ Click on element
        Args:
            locator: locator
        Return:
            element
        """
        element = self.get_element(locator)
        element.click()
        time.sleep(SLEEP_TIME)
        return element

    def type(self, text, locator):
        """ Type text on specified locator
        Args:
            text: text (e.g. "Hello")
            locator: locator
        """
        self.get_element(locator).send_keys(text)

    def select_from_drop_down(self, text, locator):
        """ Type text on drop-down list and select
        Args:
            text: text (e.g. "USA")
            locator: locator
        """
        element = self.get_element(locator)

        # Scroll to element so it is in viewport
        self.driver.execute_script("return arguments[0].scrollIntoView(false);", element)
        self.click(locator)
        self.type(text, locator)
        element.send_keys(Keys.RETURN)

    def assert_page_loaded(self, page_name, locator):
        """ Assert page is loaded
        Args:
            page_name: e.g. "Login"
            locator: locator
        """
        assert self.get_element(locator).is_displayed(), "Expected element was not present on this page"
        assert self.driver.title == page_name, "Expected page [%s] was not loaded" % page_name

    def assert_text_present(self, word, locator):
        """ Assert text is present
        Args:
            word: e.g. "Welcome"
            locator: locator
        """
        time.sleep(SLEEP_TIME)
        element = self.get_element(locator)
        assert word in element.text, "Text [%s] was not found" % word
