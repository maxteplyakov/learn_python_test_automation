from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

# не используется???
    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_name("submit").click()

    def update(self, contact):
        wd = self.app.wd
        # init contact creation
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_name("update").click()

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


    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
