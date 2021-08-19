from models.group import Group


# def test_update_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.update(
#         Group(
#             name="Changed_name",
#             header="Changed_header",
#             footer="changed_footer"
#         )
#     )
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.get_group_list()
    group = Group(name="2nd time Changed_name")
    group.id = old_groups[0].id
    app.group.update(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == \
           sorted(new_groups, key=Group.id_or_max)

# def test_update_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.update(
#         Group(
#             header="2nd time Changed_header"
#         )
#     )
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
