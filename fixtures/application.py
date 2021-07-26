from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from fixtures.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def create_contact(self, contact):

        wd = self.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()

        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)

        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)

        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)

        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        # couldn't create contact with photo.
        # DB column type is string - it didnt even designed to storage photos
        # driver.find_element_by_name("photo").clear()
        # driver.find_element_by_name("photo").send_keys(contact.photo)

        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)

        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)

        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone_num)

        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.cell_phone_num)

        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone_num)

        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)

        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)

        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)

        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)

        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        Select(wd.find_element_by_name("bday")).select_by_visible_text(
            contact.bday
        )

        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(
            contact.bmonth
        )

        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(
            contact.aday
        )

        Select(wd.find_element_by_name("amonth")).select_by_visible_text(
            contact.amonth
        )

        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)

        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home_phone_2)

        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def destroy(self):
        self.wd.quit()