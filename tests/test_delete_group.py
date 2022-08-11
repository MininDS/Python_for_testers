# -*- coding: utf-8 -*-

def test_delete_first_group(app):
    # Main test scenario - open site, login, delete first group in the list, return to groups page and logout using classes-helpers
    #app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    #app.session.logout()