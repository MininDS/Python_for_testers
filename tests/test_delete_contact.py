# -*- coding: utf-8 -*-
from models.contact import Contact


def test_delete_first_contact(app):
    # Main test scenario - open site, login, delete first contact, return to main page and logout using classes-helpers
    app.session.login(username="admin", password="secret")
    app.contact.delete_via_contacts_list()
    app.session.logout()