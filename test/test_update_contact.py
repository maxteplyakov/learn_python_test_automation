import os
from random import randrange

from models.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='John', last_name='Doe'))
    app.contact.update_first_contact(
        Contact(
            first_name="Changed_name",
            middle_name="Changed_Middle_name",
            last_name="Changed_Last_name",
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


def test_update_random_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='John', last_name='Doe'))
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    contact = Contact(
            first_name="2nd_time_Changed_name",
            last_name='changed_last_name'
        )
    contact.id = old_contacts_list[index].id
    app.contact.update_contact_by_index(index, contact)
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[index] = contact
    assert sorted(old_contacts_list, key=Contact.id_or_max) == \
           sorted(new_contacts_list, key=Contact.id_or_max)
