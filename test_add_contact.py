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
        wd = self.wd

        self.open_main_page(wd)
        self.login(wd)
        self.init_contact_creation(wd)
        self.fill_first_name_pole(wd)
        self.fill_second_name_pole(wd)
        self.fill_last_name_pole(wd)
        self.fill_nickname_pole(wd)
        self.fill_title_pole(wd)
        self.fill_company_pole(wd)
        self.fill_address_pole(wd)
        self.fill_home_pole(wd)
        self.fill_mobile_phone_pole(wd)
        self.fill_work_pole(wd)
        self.fill_fax_pole(wd)
        self.fill_email1_pole(wd)
        self.fill_email2_pole(wd)
        self.fill_email3_pole(wd)
        self.fill_homepage_pole(wd)
        self.select_birtday_date(wd)
        self.select_anniversary_date(wd)
        self.fill_address2_pole(wd)
        self.fill_home2_pole(wd)
        self.fill_notes_form(wd)
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

    def fill_notes_form(self, wd):
        # Fill notes form
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys("notes_test")

    def fill_home2_pole(self, wd):
        # Fill home2 pole
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys("home2_test")

    def fill_address2_pole(self, wd):
        # Fill address2 form
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys("address_test")

    def select_anniversary_date(self, wd):
        # Select anniversary date values
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text("2")
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text("February")
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys("2000")

    def select_birtday_date(self, wd):
        # Select birthday date values
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text("1")
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text("January")
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys("1900")

    def fill_homepage_pole(self, wd):
        # Fill homepage pole
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys("homepage_test")

    def fill_email3_pole(self, wd):
        # Fill email3 pole
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys("email3_test")

    def fill_email2_pole(self, wd):
        # Fill email2 pole
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys("email2_test")

    def fill_email1_pole(self, wd):
        # Fill email1 pole
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys("email_test")

    def fill_fax_pole(self, wd):
        # Fill fax pole
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys("fax_test")

    def fill_work_pole(self, wd):
        # Fill work pole
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys("work_test")

    def fill_mobile_phone_pole(self, wd):
        # Fill mobile phone pole
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys("mobile_test")

    def fill_home_pole(self, wd):
        # Fill home pole
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys("home_test")

    def fill_address_pole(self, wd):
        # Fill address pole
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys("address_test")

    def fill_company_pole(self, wd):
        # Fill company pole
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys("company_test")

    def fill_title_pole(self, wd):
        # Fill title pole
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys("title_test")

    def fill_nickname_pole(self, wd):
        # Fill nickname pole
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys("nick_test")

    def fill_last_name_pole(self, wd):
        # Fill last name pole
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys("last_test")

    def fill_second_name_pole(self, wd):
        # Fill second name pole
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys("middle_test")

    def fill_first_name_pole(self, wd):
        # Fill first name pole
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys("first_test")

    def init_contact_creation(self, wd):
        # Init contact creation
        wd.find_element(By.XPATH, '//*[@id="nav"]/ul/li[2]/a').click()

    def login(self, wd):
        # Login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
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