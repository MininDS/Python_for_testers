# -*- coding: utf-8 -*-
from models.group import Group


def test_edit_first_group(app):
    # Main test scenario - open site, login, edit first group, return to groups page and logout using classes-helpers
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Test_edited", header="testtest_edited", footer="testtesttest_edited"))
    app.session.logout()
