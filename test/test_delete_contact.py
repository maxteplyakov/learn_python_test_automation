from time import sleep
from random import randrange

from models.contact import Contact


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='John', last_name='Doe'))
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    app.contact.delete_contact_by_index(index)
    sleep(1) # без этой строчки new_contact_list начинает присваиваться раньше, чем в браузере открывается домашняя страница, соответсвенно, не может найти на ней элементы
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    old_contacts_list[index:index+1] = []
    assert old_contacts_list == new_contacts_list
