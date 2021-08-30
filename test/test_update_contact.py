import os
import random

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


def test_update_random_contact_name(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='John', last_name='Doe'))
    old_contacts_list = db.get_contact_list()
    contact = random.choice(old_contacts_list)
    index = old_contacts_list.index(contact)
    contact_upd = Contact(
            first_name="2nd_time_Changed_name",
            last_name='changed_last_name'
        )
    app.contact.update_contact_by_id(contact.id, contact_upd)
    new_contacts_list = db.get_contact_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[index] = db.get_contact_by_id(contact.id)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == \
           sorted(new_contacts_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.id_or_max) ==\
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
