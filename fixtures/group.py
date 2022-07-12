from selenium.webdriver.common.by import By

class GroupHelper:
    # Class-helper for groups - contains methods for group creation only
    def __init__(self, app):
        self.app = app

    def init_group_creation(self):
        # Open groups page and init new group creation
        wd = self.app.wd
        wd.find_element(By.NAME, "new").click()

    def create(self, group):
        # Fill group form
        wd = self.app.wd
        self.init_group_creation()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        # Return to groups page
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='content']/div/i/a").click()