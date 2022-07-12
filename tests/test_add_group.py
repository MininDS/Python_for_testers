# -*- coding: utf-8 -*-
from models.group import Group
from fixtures.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    # Main test scenario - open site, login, create group, return to groups page and logout
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="Test", header="testtest", footer="testtesttest"))
    app.session.logout()


def test_add_empty_group(app):
    # Slave test scenario - open site, login, create group with empty forms, return to groups page and logout
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()