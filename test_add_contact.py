# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        # Private method for selected browser start and implicitly wait pause for exception
        self.type_of_browser = 'Chrome'
        if self.type_of_browser == 'Chrome':
            self.wd = webdriver.Chrome()
        elif self.type_of_browser == 'Firefox':
            self.wd = webdriver.Firefox()

        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        # Main test scenario - open site, login, create contact with all parameters, return to main page and logout
        wd = self.wd

        self.open_main_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_contact_creation(wd)
        self.fill_first_name_pole(wd, first_name="first_test")
        self.fill_second_name_pole(wd, middle_name="middle_test")
        self.fill_last_name_pole(wd, last_name="last_test")
        self.fill_nickname_pole(wd, nickname="nick_test")
        self.fill_title_pole(wd, title="title_test")
        self.fill_company_pole(wd, company="company_test")
        self.fill_address_pole(wd, address="address_test")
        self.fill_home_pole(wd, home="home_test")
        self.fill_mobile_phone_pole(wd, mobile_phone="mobile_test")
        self.fill_work_pole(wd, work="work_test")
        self.fill_fax_pole(wd, fax="fax_test")
        self.fill_email1_pole(wd, email1="email1_test")
        self.fill_email2_pole(wd, email2="email2_test")
        self.fill_email3_pole(wd, email3="email3_test")
        self.fill_homepage_pole(wd, homepage="homepage_test")
        self.select_birtday_date(wd, birthday_day="1", birthday_month="January", birthday_year="1900")
        self.select_anniversary_date(wd, anniversary_day="2", anniversary_month="February", anniversary_year="2000")
        self.fill_address2_pole(wd, address2="address2_test")
        self.fill_home2_pole(wd, home2="home2_test")
        self.fill_notes_form(wd, notes="notes_test")
        self.submit_contact_creation(wd)
        self.return_to_main_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # Logout
        wd.find_element(By.XPATH, '//*[@id="top"]/form/a').click()

    def return_to_main_page(self, wd):
        # Return to main page
        wd.find_element(By.XPATH, '//*[@id="content"]/div/i/a[2]').click()

    def submit_contact_creation(self, wd):
        # Submit contact creation
        wd.find_element(By.XPATH, '//*[@id="content"]/form/input[21]').click()

    def fill_notes_form(self, wd, notes):
        # Fill notes form
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(notes)

    def fill_home2_pole(self, wd, home2):
        # Fill home2 pole
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(home2)

    def fill_address2_pole(self, wd, address2):
        # Fill address2 form
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(address2)

    def select_anniversary_date(self, wd, anniversary_day, anniversary_month, anniversary_year):
        # Select anniversary date values
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(anniversary_day)
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(anniversary_month)
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(anniversary_year)

    def select_birtday_date(self, wd, birthday_day, birthday_month, birthday_year):
        # Select birthday date values
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(birthday_day)
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(birthday_month)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(birthday_year)

    def fill_homepage_pole(self, wd, homepage):
        # Fill homepage pole
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(homepage)

    def fill_email3_pole(self, wd, email3):
        # Fill email3 pole
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(email3)

    def fill_email2_pole(self, wd, email2):
        # Fill email2 pole
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(email2)

    def fill_email1_pole(self, wd, email1):
        # Fill email1 pole
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(email1)

    def fill_fax_pole(self, wd, fax):
        # Fill fax pole
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(fax)

    def fill_work_pole(self, wd, work):
        # Fill work pole
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(work)

    def fill_mobile_phone_pole(self, wd, mobile_phone):
        # Fill mobile phone pole
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(mobile_phone)

    def fill_home_pole(self, wd, home):
        # Fill home pole
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(home)

    def fill_address_pole(self, wd, address):
        # Fill address pole
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(address)

    def fill_company_pole(self, wd, company):
        # Fill company pole
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(company)

    def fill_title_pole(self, wd, title):
        # Fill title pole
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(title)

    def fill_nickname_pole(self, wd, nickname):
        # Fill nickname pole
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(nickname)

    def fill_last_name_pole(self, wd, last_name):
        # Fill last name pole
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(last_name)

    def fill_second_name_pole(self, wd, middle_name):
        # Fill second name pole
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(middle_name)

    def fill_first_name_pole(self, wd, first_name):
        # Fill first name pole
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(first_name)

    def init_contact_creation(self, wd):
        # Init contact creation
        wd.find_element(By.XPATH, '//*[@id="nav"]/ul/li[2]/a').click()

    def login(self, wd, username, password):
        # Login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_main_page(self, wd):
        # Open main page
        wd.get("http://localhost:8080/addressbook/")

    def is_element_present(self, how, what):
        # Private method for definition of elements' presentation on needed page
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        # Private method for alert when element is not on a page
        try:
            self.wd.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        # Private method - closes browser window
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()