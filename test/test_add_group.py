# -*- coding: utf-8 -*-
import allure

from models.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    # assert len(old_groups) + 1 == app.group.count()
    with allure.step(
            'then the new group list is equal '
            'to the old list with the added group'
    ):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) ==\
               sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == \
#            sorted(new_groups, key=Group.id_or_max)

