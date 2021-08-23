# -*- coding: utf-8 -*-
import pytest

from models.contact import Contact


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) ==\
           sorted(new_contacts_list, key=Contact.id_or_max)


# def test_add_contact(app):
#     old_contacts_list = app.contact.get_contacts_list()
#     contact = Contact(
#             first_name="Firstname",
#             middle_name="Middlename",
#             last_name="Lastname",
#             nickname="Nickname",
#             photo=os.path.abspath('../photo.jpg'),
#             title="Title", company="Company",
#             address="Address",
#             home_phone_num="222-22-22",
#             cell_phone_num="88002000600",
#             work_phone_num="200-00-00",
#             fax="211-11-11", email1="email1@mail.com",
#             email2="email1@mail.com",
#             email3="email1@mail.com",
#             homepage="www.google.com", bday="1",
#             bmonth="January",
#             byear="1990", aday="1", amonth="February",
#             ayear="1867",
#             address2="addr2",
#             home_phone_2="73913121010",
#             notes="some notes"
#     )
#     app.contact.create(contact)
#     new_contacts_list = app.contact.get_contacts_list()
#     assert len(old_contacts_list) + 1 == len(new_contacts_list)
#     old_contacts_list.append(contact)
#     assert sorted(old_contacts_list, key=Contact.id_or_max) ==\
#            sorted(new_contacts_list, key=Contact.id_or_max)


#
# Contact(
#             first_name="Firstname",
#             middle_name="Middlename",
#             last_name="Lastname",
#             nickname="Nickname",
#             photo=os.path.abspath('../photo.jpg'),
#             title="Title", company="Company",
#             address="Address",
#             home_phone_num="222-22-22",
#             cell_phone_num="88002000600",
#             work_phone_num="200-00-00",
#             fax="211-11-11", email1="email1@mail.com",
#             email2="email1@mail.com",
#             email3="email1@mail.com",
#             homepage="www.google.com", bday="1",
#             bmonth="January",
#             byear="1990", aday="1", amonth="February",
#             ayear="1867",
#             address2="addr2",
#             home_phone_2="73913121010",
#             notes="some notes"
#     )

