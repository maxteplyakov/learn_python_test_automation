import re


def test_phones_on_home_page(app):
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_homepage.all_phones_from_homepage ==\
           merge_phones_like_on_homepage(contact_from_editpage)


def test_phones_on_contact_view_page(app):
    contact_from_viewpage = app.contact.get_contact_from_viewpage(0)
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_viewpage.all_phones_from_viewpage ==\
        merge_phones_like_on_viewpage(contact_from_editpage)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != '', map(lambda x: clear(x),
        filter(lambda x: x is not None, (
            [
            contact.home_phone_num,
            contact.cell_phone_num,
            contact.work_phone_num,
            contact.home_phone_2
            ]
        )
    ))))


def merge_phones_like_on_viewpage(contact):
    return ''.join(
        [
            contact.home_phone_num,
            contact.cell_phone_num,
            contact.work_phone_num,
            contact.home_phone_2
        ]
    )
