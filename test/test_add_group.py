# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(
        Group(name="group1", header="group1_header", footer="group1_footer")
    )
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
