from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # Login
        wd = self.app.wd
        self.app.open_main_page()

        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        # Logout
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='top']/form/a").click()