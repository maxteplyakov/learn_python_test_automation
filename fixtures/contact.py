import re

from selenium.webdriver.support.ui import Select
from models.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def open_contact_for_update_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_for_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def update_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_for_update_by_index(index)
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def update_first_contact(self, contact):
        self.update_contact_by_index(0, contact)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.set_field_value("firstname", contact.first_name)
        self.set_field_value("middlename", contact.middle_name)
        self.set_field_value("lastname", contact.last_name)

        self.set_field_value("lastname", contact.last_name)
        self.set_field_value("nickname", contact.nickname)

        # couldn't create contact with photo.
        # DB column type is string - it didnt even designed to storage photos
        # driver.find_element_by_name("photo").clear()
        # driver.find_element_by_name("photo").send_keys(contact.photo)

        self.set_field_value("title", contact.title)
        self.set_field_value("company", contact.company)
        self.set_field_value("address", contact.address)
        self.set_field_value("home", contact.home_phone_num)
        self.set_field_value("mobile", contact.cell_phone_num)
        self.set_field_value("work", contact.work_phone_num)
        self.set_field_value("fax", contact.fax)
        self.set_field_value("email", contact.email1)
        self.set_field_value("email2", contact.email2)
        self.set_field_value("email3", contact.email3)
        self.set_field_value("homepage", contact.homepage)

        self.choose_value("bday", contact.bday)
        self.choose_value("bmonth", contact.bmonth)
        self.set_field_value("byear", contact.byear)

        self.choose_value("aday", contact.aday)
        self.choose_value("amonth", contact.amonth)
        self.set_field_value("ayear", contact.ayear)

        self.set_field_value("address2", contact.address2)
        self.set_field_value("phone2", contact.home_phone_2)
        self.set_field_value("notes", contact.notes)

    def choose_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(
                value
            )
        else:
            pass

    def set_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cache = []
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name('input').get_attribute(
                    'value'
                )
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contacts_cache.append(
                    Contact(
                        last_name=last_name,
                        first_name=first_name,
                        id=id,
                        all_phones_from_homepage=all_phones,
                        all_emails_from_homepage=all_emails
                    )
                )
        return list(self.contacts_cache)

    def get_contact_info_from_editpage(self, index):
        self.open_contact_for_update_by_index(index)
        wd = self.app.wd
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone_num = wd.find_element_by_name("home").get_attribute("value")
        work_phone_num = wd.find_element_by_name("work").get_attribute("value")
        cell_phone_num = wd.find_element_by_name("mobile").get_attribute("value")
        home_phone_2 = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(
            first_name=first_name,
            last_name=last_name,
            id=id,
            home_phone_num=home_phone_num,
            cell_phone_num=cell_phone_num,
            work_phone_num=work_phone_num,
            home_phone_2=home_phone_2,
            email1=email1,
            email2=email2,
            email3=email3

        )

    def get_contact_from_viewpage(self, index):
        wd = self.app.wd
        self.open_contact_for_view_by_index(index)
        text = wd.find_element_by_id("content").text
        # home_phone_num = re.search("H: (.*)", text).group(1)
        # work_phone_num = re.search("W: (.*)", text).group(1)
        # cell_phone_num = re.search("M: (.*)", text).group(1)
        # home_phone_2 = re.search("P: (.*)", text).group(1)
        all_phones = []
        for phone_type in ['H:', 'M:', 'W:', 'P:']:
            try:
                all_phones.append(re.search(f"{phone_type} (.*)", text).group(1))
            except:
                pass
        return Contact(
            all_phones_from_viewpage=''.join(all_phones)
        )
