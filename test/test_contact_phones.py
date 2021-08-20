import re
from time import sleep
from random import randrange

from models.contact import Contact


def test_phones_on_home_page(app):
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_homepage.all_phones_from_homepage == \
           merge_phones_like_on_homepage(contact_from_editpage)


def test_phones_on_contact_view_page(app):
    contact_from_viewpage = app.contact.get_contact_from_viewpage(0)
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_viewpage.all_phones_from_viewpage == \
           merge_phones_like_on_viewpage(contact_from_editpage)


def test_random_contact_info_on_homepage_editpage(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(
                first_name='John', last_name='Doe',
                home_phone_num='1111111',
                cell_phone_num='2222222',
                work_phone_num='3333333',
                home_phone_2='4444444',
                email1='somemail@mail.kz',
                address='3rd builders st.'
            )
        )
    index = randrange(app.contact.count())
    contact_from_homepage = app.contact.get_contacts_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)

    assert contact_from_homepage.first_name == \
           contact_from_editpage.first_name
    assert contact_from_homepage.last_name == \
           contact_from_editpage.last_name
    assert contact_from_homepage.address == \
           contact_from_editpage.address
    assert contact_from_homepage.all_phones_from_homepage == \
           merge_phones_like_on_homepage(contact_from_editpage)
    assert contact_from_homepage.all_emails_from_homepage == \
           merge_emails_like_on_homepage(contact_from_editpage)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(
        filter(
            lambda x: x != '', map(
                lambda x: clear(x), filter(
                    lambda x: x is not None,
                    [
                        contact.home_phone_num,
                        contact.cell_phone_num,
                        contact.work_phone_num,
                        contact.home_phone_2
                    ]
                )
            )
        )
    )


def merge_phones_like_on_viewpage(contact):
    return ''.join(
        [
            contact.home_phone_num,
            contact.cell_phone_num,
            contact.work_phone_num,
            contact.home_phone_2
        ]
    )


def merge_emails_like_on_homepage(contact):
    return "\n".join(
        filter(
            lambda x: x != '' and x is not None, (
                [
                    contact.email1,
                    contact.email2,
                    contact.email3
                ]
            )
        )
    )
