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

        #Open main page
        wd.get("http://localhost:8080/addressbook/")

        # Login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value='Login']").click()


        # Init contact creation
        wd.find_element(By.XPATH, '//*[@id="nav"]/ul/li[2]/a').click()

        # Fill contact form fully
        # Fill first name pole
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys("first_test")

        # Fill second name pole
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys("middle_test")

        # Fill last name pole
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys("last_test")

        # Fill nickname pole
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys("nick_test")

        # Fill title pole
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys("title_test")

        # Fill company pole
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys("company_test")

        # Fill address pole
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys("address_test")

        # Fill home pole
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys("home_test")

        # Fill mobile phone pole
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys("mobile_test")

        # Fill work pole
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys("work_test")

        # Fill fax pole
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys("fax_test")

        # Fill emails poles
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys("email_test")
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys("email2_test")
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys("email3_test")

        # Fill homepage pole
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys("homepage_test")

        # Select birthday date values
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text("1")
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text("January")
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys("1900")

        # Select anniversary date values
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text("2")
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text("February")
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys("2000")

        # Fill address form
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys("address_test")

        # Fill home pole
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys("home2_test")

        # Fill notes form
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys("notes_test")

        # Submit contact creation
        wd.find_element(By.XPATH, '//*[@id="content"]/form/input[21]').click()

        # Return to main page
        wd.find_element(By.XPATH, '//*[@id="content"]/div/i/a[2]').click()

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