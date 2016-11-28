from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    ADMIN_NAME_FIELD = (By.NAME, "email")
    USER_NAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    ADMIN_LOGIN_BUTTON = (By.XPATH, "html/body/div[1]/form[1]/button")
    USER_LOGIN_BUTTON = (By.XPATH, "//*[@id='loginfrm']/div[4]/button")

class CustomerLocators(object):
    GREETING_TEXT = (By.XPATH, "html/body/div[3]/div[1]/div/div[1]/h3")
    MY_PROFILE = (By.XPATH, "html/body/div[3]/div[3]/div/div[1]/ul/li[2]/a")
    TOURS = (By.XPATH, "html/body/div[2]/div/div/div[2]/ul[1]/li[4]/a")
    LOCATION = (By.XPATH, "html/body/div[5]/div[2]/div/div[2]/form/div[1]/div/div/input")
    LOCATION_OPTION = (By.XPATH, "html/body/div[5]/div[2]/div/div[2]/form/div[1]/div/div/div[2]/div/div/ul/li[3]/a")
    CHECKIN = (By.XPATH, "//*[@id='tchkin']/div/input")
    ADULTS = (By.XPATH, "//*[@id='adults']")
    TOURTYPE = (By.XPATH, "//*[@id='tourtype']")
    SEARCH = (By.XPATH, "html/body/div[5]/div[2]/div/div[2]/form/div[5]/div/button")
    LISTED_TOUR = (By.XPATH, "html/body/div[5]/div[3]/div/table/tbody/tr/td/div/div[2]/div/div[2]/h4/a/b")
    BOOK_NOW_BUTTON = (By.XPATH, "//*[@id='OVERVIEW']/div/div[1]/div[2]/div[2]/div/form/div[4]/button")
    CONFIRM_BOOKING = (By.XPATH, "html/body/div[3]/div/div/div[1]/div/div[2]/div[5]/button")
    CUSTOMER_DETAIL = (By.XPATH, "html/body/div[3]/div/div[7]/div[2]/p")
    USER_MENU = (By.XPATH, "html/body/div[2]/div/div/div[2]/ul[2]/li[2]/a")
    USER_SETTINGS = (By.XPATH, "html/body/div[2]/div/div/div[2]/ul[2]/li[2]/ul/li[1]/a")
    USER_BOOKINGS = (By.XPATH, "//*[@id='bookings']/div[2]/div[1]/a/b")

class DashboardLocators(object):
    ACCOUNTS_BUTTON = (By.XPATH, "//*[@id='social-sidebar-menu']/li[4]/a/span")
    CUSTOMERS_BUTTON = (By.XPATH, "//*[@id='Accounts']/li[3]/a")

    CUSTOMERS_MGMT_TAB = (By.XPATH, "//*[@id='content']/div/div[1]")

    CUSTOMER_TABLE = (By.XPATH, "//*[@id='content']/div/div[2]")

    SEARCH_BUTTON = (By.XPATH, "//*[@id='content']/div/div[2]/div/div/div[1]/div[3]/a")
    SEARCH_FIELD = (By.NAME, "phrase")
    GO_BUTTON = (By.XPATH, "//*[@id='content']/div/div[2]/div/div/div[1]/div[3]/span[1]/span/a")
    RESET_BUTTON = (By.XPATH, "//*[@id='content']/div/div[2]/div/div/div[1]/div[3]/span[1]/span/a[2]")
    ADD_BUTTON = (By.XPATH, "//*[@id='content']/div/form/button")

    FNAME_FIELD = (By.NAME, "fname")
    LNAME_FIELD = (By.NAME, "lname")
    EMAIL_FIELD = (By.NAME, "email")
    PWD_FIELD = (By.NAME, "password")
    COUNTRY_LIST_DROP_DOWN = (By.XPATH, "//*[@id='s2id_autogen1']/a/span[2]")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='content']/form/div/div[3]/button")

    TOURS_BUTTON = (By.XPATH, "//*[@id='social-sidebar-menu']/li[9]/a/span")
    TOURS_BUTTON2 = (By.XPATH, "//*[@id='Tours']/li[1]/a")
    TOURS_MGMT_TAB = (By.XPATH, "//*[@id='content']/div/div[1]")
    TOURNAME_FIELD = (By.NAME, "tourname")
    TOUR_MAX_ADULT = (By.NAME, "maxadult")
    TOUR_ADULT_PRICE = (By.NAME, "adultprice")
    TOUR_TYPE = (By.XPATH, "//*[@id='s2id_autogen1']/a/span[1]")
    TOUR_LOCATION = (By.XPATH, "//*[@id='s2id_autogen3']/a/span[1]")
    TOUR_SUBMIT_BUTTON = (By.ID, "add")

