from models.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.update(
        Group(
            name="Changed_name",
            header="Changed_header",
            footer="changed_footer"
        )
    )


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.update(
        Group(
            name="2nd time Changed_name"
        )
    )


def test_update_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.update(
        Group(
            header="2nd time Changed_header"
        )
    )
