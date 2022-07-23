from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactHelper:
    # Class-helper for contacts - contains methods for contact creation only
    def __init__(self, app):
        self.app = app

    def go_to_main_page(self):
        # Return to main page
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="content"]/div/i/a[2]').click()

    def go_to_home_page(self):
        # Go to home page of application
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="nav"]/ul/li[1]/a').click()

    def init_contact_creation(self):
        # Init contact creation
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="nav"]/ul/li[2]/a').click()

    def fill_contact_form_full(self, contact):
        # Fill all poles in contact form
        wd = self.app.wd
        # Fill firstname pole
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.first_name)
        # Fill middlename pole
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
        # Fill lastname pole
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.last_name)
        # Fill nickname pole
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        # Fill title pole
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        # Fill company pole
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        # Fill address pole
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        # Fill home phone pole
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home_phone)
        # Fill mobile phone pole
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        # Fill work phone pole
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work_phone)
        # Fill fax pole
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        # Fill email1 pole
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email1)
        # Fill email2 pole
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        # Fill email3 pole
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        # Fill homepage pole
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        # Select birthday date values
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.birthday_day)
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.birthday_month)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.birthday_year)
        # Select anniversary date values
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.anniversary_year)
        # Fill address2 form
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        # Fill home2 pole
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(contact.home2)
        # Fill notes form
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)

    def create(self, contact):
        # Fill contact form entirely
        wd = self.app.wd
        self.go_to_home_page()
        self.init_contact_creation()
        # Fill contact form with data
        self.fill_contact_form_full(contact)
        # Submit contact creation
        self.submit_contact_creation()
        # Return to main page again
        self.go_to_main_page()

    def submit_contact_creation(self):
        # Submit contact creation
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="content"]/form/input[21]').click()

    def submit_contact_update(self):
        # Submit contact update
        wd = self.app.wd
        wd.find_element(By.NAME, "update").click()

    def submit_contact_deletion_via_contacts_list(self):
        # Submit contact deletion in modal browser-form
        wd = self.app.wd
        wd.switch_to.alert.accept()

    def init_first_contact_delete_via_contacts_list(self):
        # Init contact deletion - click on delete button
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="content"]/form[2]/div[2]/input').click()

    def delete_first_contact_via_contacts_list(self):
        # Select first contact in the general list and delete it
        wd = self.app.wd
        self.go_to_home_page()
        # Select first contact in contacts list
        wd.find_element(By.NAME, "selected[]").click()
        # Click on delete button on home page
        self.init_first_contact_delete_via_contacts_list()
        # Submit selected contact deletion via modal form in browser
        self.submit_contact_deletion_via_contacts_list()
        # Return to home page of application again
        self.go_to_home_page()

    def init_first_contact_edit_from_list(self):
        # Init contact edit_first_contact_via_contacts_list - click on edit_first_contact_via_contacts_list button on general contacts list
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="maintable"]/tbody/tr[2]/td[8]/a/img').click()

    def init_first_contact_edit_from_details(self):
        # Init contact edit_first_contact_via_contacts_list - click on details button and modify button in that menu
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="maintable"]/tbody/tr[2]/td[7]/a/img').click()
        wd.find_element(By.NAME, "modifiy").click()

    def delete_first_contact_via_contacts_form(self):
        # Delete contact via edit_first_contact_via_contacts_list-form
        wd = self.app.wd
        self.go_to_home_page()
        # Open first contacts edit_first_contact_via_contacts_list form
        self.init_first_contact_edit_from_list()
        # Click on delete button on edit_first_contact_via_contacts_list form
        wd.find_element(By.XPATH, '//*[@id="content"]/form[2]/input[2]')
        # Return to home page with contacts list again
        self.go_to_home_page()

    def edit_first_contact_via_contacts_list(self, contact):
        # Edit contact form entirely via contacts list
        wd = self.app.wd
        self.go_to_home_page()
        # Begin contact edit_first_contact_via_contacts_list process from main page
        self.init_first_contact_edit_from_list()
        # Edit contact - fill contact form with new data
        self.fill_contact_form_full(contact)
        # Submit contact update
        self.submit_contact_update()
        # Return to main page again
        self.go_to_home_page()

    def edit_first_contact_via_contacts_details(self, contact):
        # Edit contact form entirely via details form
        wd = self.app.wd
        self.go_to_home_page()
        # Begin contact edit_first_contact_via_contacts_list process from details page
        self.init_first_contact_edit_from_details()
        # Edit contact - fill contact form with new data
        self.fill_contact_form_full(contact)
        # Submit contact update
        self.submit_contact_update()
        # Return to main page again
        self.go_to_home_page()