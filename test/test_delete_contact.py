import random
from time import sleep

from models.contact import Contact


def test_delete_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name='John', last_name='Doe'))
    old_contacts_list = db.get_contact_list()
    contact = random.choice(old_contacts_list)
    app.contact.delete_contact_by_id(contact.id)
    sleep(1) # без этой строчки new_contact_list начинает присваиваться раньше, чем в браузере открывается домашняя страница, соответсвенно, не может найти на ней элементы
    new_contacts_list = db.get_contact_list()
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    old_contacts_list.remove(contact)
    assert old_contacts_list == new_contacts_list
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.id_or_max) ==\
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
