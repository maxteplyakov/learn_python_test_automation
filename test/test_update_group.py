from models.group import Group


def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.update(
        Group(
            name="Changed_name",
            header="Changed_header",
            footer="changed_footer"
        )
    )
    app.session.logout()