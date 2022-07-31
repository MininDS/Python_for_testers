from selenium.webdriver.common.by import By

class GroupHelper:
    # Class-helper for groups - contains methods for group creation, modification, deletion only
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # Open groups page for next user actions
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="nav"]/ul/li[3]/a').click()

    def return_to_groups_page(self):
        # Return to groups page
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='content']/div/i/a").click()

    def init_group_creation(self):
        # Init new group creation on groups page
        wd = self.app.wd
        wd.find_element(By.NAME, "new").click()

    def create(self, group):
        # Fill group form
        wd = self.app.wd
        self.open_groups_page()
        # Begin creation process - open group page for poles filling
        self.init_group_creation()
        # Fill poles of group name, header and footer
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element(By.NAME, "submit").click()
        # Return to groups page again
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        # Select first group in the list of groups
        wd.find_element(By.NAME, "selected[]").click()

    def init_group_edit(self):
        # Init new group modification on groups page
        wd = self.app.wd
        wd.find_element(By.NAME, "edit").click()

    def fill_group_form(self, group):
        # Fill all poles in group form
        wd = self.app.wd
        # Fill in Group name
        self.change_field_value("group_name", group.name)
        # Fill in Group header
        self.change_field_value("group_header", group.header)
        # Fill in Group footer
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        # Fill required Group field - name, header footer, which are given from fill_group_form method with given name, header or footer also
        wd = self.app.wd
        # Define that given Group pole is not empty from fill_group_form method and test-scenario
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # Select first group
        self.select_first_group()
        # Begin modification process - open selected group for poles modification
        self.init_group_edit()
        # Modify all poles of group name, header and footer
        self.fill_group_form(new_group_data)
        # Submit group modification
        wd.find_element(By.NAME, "update").click()
        # Return to groups page again
        self.return_to_groups_page()

    def delete_first_group(self):
        # Fill group form
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # Submit deletion by appropriate button
        wd.find_element(By.NAME, "delete").click()
        # Return to groups page list again
        self.return_to_groups_page()

