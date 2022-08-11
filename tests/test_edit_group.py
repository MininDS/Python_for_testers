# -*- coding: utf-8 -*-
from models.group import Group


def test_edit_first_group_fully(app):
    # Main test scenario - open site, login, edit_first_group fully - name, header and footer, return to groups page and logout using classes-helpers
    #app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Test_edited", header="testtest_edited", footer="testtesttest_edited"))
    #app.session.logout()


def test_edit_first_group_name(app):
    # Slave test scenario - open site, login, edit_first_group name only, return to groups page and logout using classes-helpers
    #app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Test_edited_name"))
    #app.session.logout()


def test_edit_first_group_header(app):
    # Slave test scenario - open site, login, edit_first_group header only, return to groups page and logout using classes-helpers
    #app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="Test_edited_header"))
    #app.session.logout()