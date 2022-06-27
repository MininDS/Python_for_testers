# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        # Private method for selected browser start and implicitly wait pause for exception
        self.type_of_browser = 'Chrome'

        if self.type_of_browser == 'Chrome':
            self.wd = webdriver.Chrome()
        elif self.type_of_browser == 'Firefox':
            self.wd = webdriver.Firefox()

        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        # Main test scenario - open site, login, create group, return to groups page and logout
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_group_creation(wd)
        self.create_group(wd, name="Test", header="testtest", footer="testtesttest")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        # Main test scenario - open site, login, create group, return to groups page and logout
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_group_creation(wd)
        self.create_group(wd, name="", header="", footer="")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # Logout
        wd.find_element(By.XPATH, "//*[@id='top']/form/a").click()

    def return_to_groups_page(self, wd):
        # Return to groups page
        wd.find_element(By.XPATH, "//*[@id='content']/div/i/a").click()

    def create_group(self, wd, name, header, footer):
        # Fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(footer)
        # Submit group creation
        wd.find_element(By.NAME, "submit").click()

    def init_group_creation(self, wd):
        # Open groups page and init new group creation
        wd.find_element(By.NAME, "new").click()

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
        wd.get("http://localhost:8080/addressbook/group.php")

    def is_element_present(self, how, what):
        # Private method for definition of elements' presentation on needed page
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        # Private method for alert when element is not on a page
        try: self.wd.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        # Private method - closes browser window
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
