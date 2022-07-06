# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

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
        self.create_contact(wd, Contact(first_name="test", middle_name="test", last_name="test", nickname="test",
                                        title="test", company="test", address="test", home_phone="test", mobile_phone="test",
                                        work_phone="test", fax="test", email1="test", email2="test", email3="test",
                                        homepage="test", birthday_day="1", birthday_month="January",
                                        birthday_year="1900", anniversary_day="1", anniversary_month="February",
                                        anniversary_year="2000", address2="test", home2="test", notes="test"))
        self.submit_contact_creation(wd)
        self.return_to_main_page(wd)
        self.logout(wd)


    def open_main_page(self, wd):
        # Open main page
        wd.get("http://localhost:8080/addressbook/")

    def login(self, wd, username, password):
        # Login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def init_contact_creation(self, wd):
        # Init contact creation
        wd.find_element(By.XPATH, '//*[@id="nav"]/ul/li[2]/a').click()

    def create_contact(self, wd, contact):
        # Fill firstname pole
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.first_name)

        # Fill middlename pole
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middle_name)

        # Fill lastname pole
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.last_name)

        # Fill nickname pole
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)

        # Fill title pole
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)

        # Fill company pole
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)

        # Fill address pole
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)

        # Fill home phone pole
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home_phone)

        # Fill mobile phone pole
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)

        # Fill work phone pole
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work_phone)

        # Fill fax pole
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)

        # Fill email1 pole
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email1)

        # Fill email2 pole
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)

        # Fill email3 pole
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)

        # Fill homepage pole
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)

        # Select birthday date values
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.birthday_day)
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.birthday_month)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.birthday_year)

        # Select anniversary date values
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.anniversary_year)

        # Fill address2 form
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)

        # Fill home2 pole
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(contact.home2)

        # Fill notes form
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)

    def submit_contact_creation(self, wd):
        # Submit contact creation
        wd.find_element(By.XPATH, '//*[@id="content"]/form/input[21]').click()

    def return_to_main_page(self, wd):
        # Return to main page
        wd.find_element(By.XPATH, '//*[@id="content"]/div/i/a[2]').click()

    def logout(self, wd):
        # Logout
        wd.find_element(By.XPATH, '//*[@id="top"]/form/a').click()

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