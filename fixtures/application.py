from selenium import webdriver
from fixtures.session import SessionHelper
from fixtures.group import GroupHelper
from fixtures.contact import ContactHelper

class Application:
    # Main fixture - contains links on Helper-classes for tests
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_main_page(self):
        # Open main page
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def destroy(self):
        # Close browser-window
        self.wd.quit()