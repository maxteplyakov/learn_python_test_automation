# -*- coding: utf-8 -*-
import pytest, os

from contact import Contact
from fixtures.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(
        Contact(
            first_name="First name",
            middle_name="Middle name",
            last_name="Last name",
            nickname="Nickname",
            photo=os.path.abspath('../photo.jpg'),
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
    app.logout()
