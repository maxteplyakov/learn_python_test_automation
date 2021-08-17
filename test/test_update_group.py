from models.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update(
        Group(
            name="Changed_name",
            header="Changed_header",
            footer="changed_footer"
        )
    )
    app.session.logout()


def test_update_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.update(
        Group(
            name="2nd time Changed_name"
        )
    )
    app.session.logout()


def test_update_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.update(
        Group(
            header="2nd time Changed_header"
        )
    )
    app.session.logout()
