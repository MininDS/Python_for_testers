# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    # Main test scenario - open site, login, create group, return to groups page and logout using classes-helpers
    #app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Test", header="testtest", footer="testtesttest"))
    #app.session.logout()


def test_add_empty_group(app):
    # Slave test scenario - open site, login, create group with empty forms, return to groups page and logout using classes-helpers
    #app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    #app.session.logout()