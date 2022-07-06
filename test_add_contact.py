# -*- coding: utf-8 -*-
from contact import Contact
from application_add_contact import ApplicationAddContact
import pytest


@pytest.fixture
def app(request):
    fixture = ApplicationAddContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    # Main test scenario - open site, login, create contact, return to main page and logout
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="test", middle_name="test", last_name="test", nickname="test",
                                        title="test", company="test", address="test", home_phone="test", mobile_phone="test",
                                        work_phone="test", fax="test", email1="test", email2="test", email3="test",
                                        homepage="test", birthday_day="1", birthday_month="January",
                                        birthday_year="1900", anniversary_day="1", anniversary_month="February",
                                        anniversary_year="2000", address2="test", home2="test", notes="test"))
    app.logout()