import random

from models.group import Group


# def test_update_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.update_first_group(
#         Group(
#             name="Changed_name",
#             header="Changed_header",
#             footer="changed_footer"
#         )
#     )
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_update_random_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_idx = old_groups.index(group)
    group_upd = Group(name="2nd time Changed_name")
    app.group.update_group_by_id(group.id, group_upd)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[group_idx] = db.get_group_by_id(group.id)
    assert sorted(old_groups, key=Group.id_or_max) == \
           sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) ==\
               sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_update_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.update_first_group(
#         Group(
#             header="2nd time Changed_header"
#         )
#     )
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
