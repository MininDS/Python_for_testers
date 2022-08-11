# -*- coding: utf-8 -*-


def test_delete_first_contact_from_list(app):
    # Main test scenario - open site, login, delete first contact from list, return to main page and logout using classes-helpers
    #app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_via_contacts_list()
    #app.session.logout()


def test_delete_first_contact_from_form(app):
    # Alternate test scenario - open site, login, delete first contact from its edit_first_contact_via_contacts_list form, return to main page and logout using classes-helpers
    #app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_via_contacts_form()
    #app.session.logout()