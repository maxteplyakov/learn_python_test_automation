import random

from models.group import Group
from models.contact import Contact


def test_add_random_contact_to_random_group(app, db_orm):
    if len(db_orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name='John', last_name='Doe'))
    if len(db_orm.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    contact = random.choice(db_orm.get_contact_list())
    group = random.choice(db_orm.get_group_list())
    old_contacts_in_group = db_orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = db_orm.get_contacts_in_group(group)
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) ==\
           sorted(new_contacts_in_group, key=Contact.id_or_max)


def test_delete_random_contact_from_random_group(app, db_orm):
    if len(db_orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name='John', last_name='Doe'))
    if len(db_orm.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    group = random.choice(db_orm.get_group_list())
    if len(db_orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(db_orm.get_contact_list())
        app.contact.add_contact_to_group(contact, group)
    old_contacts_in_group = db_orm.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group(contact, group)
    new_contacts_in_group = db_orm.get_contacts_in_group(group)
    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == \
           sorted(new_contacts_in_group, key=Contact.id_or_max)
