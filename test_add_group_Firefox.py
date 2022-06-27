# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/group.php")
        wd.find_element(By.NAME,"user").click()
        wd.find_element(By.NAME,"user").clear()
        wd.find_element(By.NAME,"user").send_keys("admin")
        wd.find_element(By.NAME,"pass").click()
        wd.find_element(By.NAME,"pass").clear()
        wd.find_element(By.NAME,"pass").send_keys("secret")
        wd.find_element(By.XPATH,"//input[@value='Login']").click()
        wd.find_element(By.NAME,"new").click()
        wd.find_element(By.NAME,"group_name").click()
        wd.find_element(By.NAME,"group_name").clear()
        wd.find_element(By.NAME,"group_name").send_keys("Test")
        wd.find_element(By.NAME,"group_header").click()
        wd.find_element(By.NAME,"group_header").clear()
        wd.find_element(By.NAME,"group_header").send_keys("testtest")
        wd.find_element(By.NAME,"group_footer").click()
        wd.find_element(By.NAME,"group_footer").clear()
        wd.find_element(By.NAME,"group_footer").send_keys("testtesttest")
        wd.find_element(By.NAME,"submit").click()
        wd.find_element(By.XPATH,"//*[@id='content']/div/i/a").click()
        wd.find_element(By.XPATH,"//*[@id='top']/form/a").click()


    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()