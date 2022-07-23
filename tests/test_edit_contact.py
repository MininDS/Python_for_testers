# -*- coding: utf-8 -*-
from models.contact import Contact


def test_edit_first_contact_from_list(app):
    # Main test scenario - open site, login, edit first contact via general contact list, return to main page and logout using classes-helpers
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_via_contacts_list(Contact(first_name="test_edited", middle_name="test_edited", last_name="test_edited", nickname="test_edited",
                                                             title="test_edited", company="test_edited", address="test_edited", home_phone="test_edited", mobile_phone="test_edited",
                                                             work_phone="test_edited", fax="test_edited", email1="test_edited", email2="test_edited", email3="test_edited",
                                                             homepage="test_edited", birthday_day="2", birthday_month="February",
                                                             birthday_year="1901", anniversary_day="2", anniversary_month="March",
                                                             anniversary_year="2001", address2="test_edited", home2="test_edited", notes="test_edited"))
    app.session.logout()

def test_edit_first_contact_from_details(app):
    # Alternate test scenario - open site, login, edit first contact via details contact form, return to main page and logout using classes-helpers
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_via_contacts_details(Contact(first_name="test_edited", middle_name="test_edited", last_name="test_edited", nickname="test_edited",
                                                                title="test_edited", company="test_edited", address="test_edited", home_phone="test_edited", mobile_phone="test_edited",
                                                                work_phone="test_edited", fax="test_edited", email1="test_edited", email2="test_edited", email3="test_edited",
                                                                homepage="test_edited", birthday_day="2", birthday_month="February",
                                                                birthday_year="1901", anniversary_day="2", anniversary_month="March",
                                                                anniversary_year="2001", address2="test_edited", home2="test_edited", notes="test_edited"))
    app.session.logout()