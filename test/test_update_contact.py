import os

from models.contact import Contact


def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update(
        Contact(
            first_name="Changed_name",
            middle_name="Changed Middle name",
            last_name="Changed Last name",
            nickname="Nickname",
            # photo=os.path.abspath('../photo.jpg'),
            title="Title", company="Company",
            address="Address",
            home_phone_num="222-22-22",
            cell_phone_num="88002000600",
            work_phone_num="200-00-00",
            fax="211-11-11", email1="email1@mail.com",
            email2="email1@mail.com",
            email3="email1@mail.com",
            homepage="www.google.com", bday="1",
            bmonth="January",
            byear="1990", aday="1", amonth="February",
            ayear="1867",
            address2="addr2",
            home_phone_2="73913121010",
            notes="some notes")
    )
    app.session.logout()


def test_update_first_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.update(
        Contact(
            first_name="2nd time Changed_name",
            middle_name='changed middle name'
        )
    )
    app.session.logout()

