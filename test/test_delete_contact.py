from models.contact import Contact
from time import sleep


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='John', last_name='Doe'))
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    sleep(1) # без этой строчки new_contact_list начинает присваиваться раньше, чем в браузере открывается домашняя страница, соответсвенно, не может найти на ней элементы
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    old_contacts_list[0:1] = []
    assert old_contacts_list == new_contacts_list
