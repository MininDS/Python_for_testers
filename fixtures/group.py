from selenium.webdriver.common.by import By

class GroupHelper:
    # Class-helper for groups - contains methods for group creation only
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # Open groups page for next user actions
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="nav"]/ul/li[3]/a').click()

    def init_group_creation(self):
        # Init new group creation on groups page
        wd = self.app.wd
        wd.find_element(By.NAME, "new").click()

    def create(self, group):
        # Fill group form
        wd = self.app.wd
        self.open_groups_page()
        #wd.get("http://localhost:8080/addressbook/group.php")
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

    def delete_first_group(self):
        # Fill group form
        wd = self.app.wd
        self.open_groups_page()
        # Select first group
        wd.find_element(By.NAME, "selected[]").click()
        # Submit deletion by appropriate button
        wd.find_element(By.NAME, "delete").click()
        # Return to groups page list again
        self.return_to_groups_page()

    def return_to_groups_page(self):
        # Return to groups page
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='content']/div/i/a").click()