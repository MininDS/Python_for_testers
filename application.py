from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_main_page(self):
        # Open main page
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/group.php")

    def login(self, username, password):
        # Login
        wd = self.wd
        self.open_main_page()

        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def init_group_creation(self):
        # Open groups page and init new group creation
        wd = self.wd
        wd.find_element(By.NAME, "new").click()

    def create_group(self, group):
        # Fill group form
        wd = self.wd
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
        wd = self.wd
        wd.find_element(By.XPATH, "//*[@id='content']/div/i/a").click()

    def logout(self):
        # Logout
        wd = self.wd
        wd.find_element(By.XPATH, "//*[@id='top']/form/a").click()

    def destroy(self):
        self.wd.quit()