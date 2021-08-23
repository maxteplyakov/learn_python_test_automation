# -*- coding: utf-8 -*-
import os
import string
import random
import pytest

from models.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters +\
              string.digits + ' '*5        # с пробелами чаще валятся тесты
    return prefix + ''.join([random.choice(symbols) for
                             i in range(random.randrange(maxlen))])


def random_email():
    username_symbols = string.ascii_letters +\
                       string.digits +\
                       string.punctuation
    domain_symbols = string.ascii_letters + string.digits
    username = ''.join([random.choice(username_symbols) for
                        i in range(random.randrange(20))])
    domain = ''.join([random.choice(domain_symbols) for
                      i in range(random.randrange(1, 20))])
    return 'email' + username + '@' + domain + '.com'


def random_phone_num():
    symbols = string.digits + '+-()'
    return ''.join([random.choice(symbols) for
                      _ in range(random.randrange(6, 20))])


testdata = [
    Contact(
        first_name='', middle_name='', last_name='',
        nickname='', photo='',
        title='', company='', address='',
        home_phone_num='', cell_phone_num='', work_phone_num='',
        fax='', email1='', email2='', email3='', homepage='',
        bday='-', bmonth='-', byear='',
        aday='-', amonth='-', ayear='',
        address2='', home_phone_2='', notes=''
    )] + [
            Contact(
                first_name=random_string("first_name", 20),
                middle_name=random_string("middle_name", 20),
                last_name=random_string("last_name", 20),
                nickname=random_string("nickname", 20),
                photo='../photo.jpg',
                title=random_string("title", 20),
                company=random_string("company", 20),
                address=random_string("address", 50),
                home_phone_num=random_phone_num(),
                cell_phone_num=random_phone_num(),
                work_phone_num=random_phone_num(),
                fax=random_phone_num(),
                email1=random_email(),
                email2=random_email(),
                email3=random_email(),
                address2=random_string("address2", 100),
                home_phone_2=random_phone_num(),
                notes=random_string("notes", 30),
            ) for _ in range(10)
    ]


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

