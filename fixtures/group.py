from selenium.webdriver.common.by import By

class GroupHelper:
    # Class-helper for groups - contains methods for group creation, modification, deletion only
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

    def fill_group_form_full(self, group):
        # Fill all poles in group form
        wd = self.app.wd
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def create(self, group):
        # Fill group form
        wd = self.app.wd
        self.open_groups_page()
        # Begin creation process - open group page for poles filling
        self.init_group_creation()
        # Fill poles of group name, header and footer
        self.fill_group_form_full(group)
        # Submit group creation
        wd.find_element(By.NAME, "submit").click()
        # Return to groups page again
        self.return_to_groups_page()

    def init_group_edit(self):
        # Init new group modification on groups page
        wd = self.app.wd
        wd.find_element(By.NAME, "edit").click()

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Select first group
        wd.find_element(By.NAME, "selected[]").click()
        # Begin modification process - open selected group for poles modification
        self.init_group_edit()
        # Modify all poles of group name, header and footer
        self.fill_group_form_full(group)
        # Submit group modification
        wd.find_element(By.NAME, "update").click()
        # Return to groups page again
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