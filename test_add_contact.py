# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, os
from  contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)


    def test_add_contact(self):
        driver = self.driver
        self.get_home_page(driver)
        self.login(driver)
        self.create_contact(driver,
                            Contact(first_name="First name",
                                    middle_name="Middle name",
                                    last_name="Last name",
                                    nickname="Nickname",
                                    photo=os.path.abspath('photo.jpg'),
                                    title="Title", company="Company",
                                    address="Address",
                                    home_phone_num="222-22-22",
                                    cell_phone_num="88002000600",
                                    work_phone_num="200-00-00",
                                    fax="211-11-11", email1="email1@mail.com",
                                    email2="email1@mail.com",
                                    email3="email1@mail.com",
                                    homepage="www.google.com", bday="1",
                                    bmonth="January",
                                    byear="1990", aday="1", amonth="February",
                                    ayear="1867",
                                    address2="addr2",
                                    home_phone_2="73913121010",
                                    notes="some notes")
        )
        driver.find_element_by_link_text("home").click()
        self.logout(driver)

    def get_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def create_contact(self, driver, contact):
        # init contact creation
        driver.find_element_by_link_text("add new").click()

        # fill contact form
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.first_name)

        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middle_name)

        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)

        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)

        # couldn't create contact with photo.
        # DB column type is string - it didnt even designed to storage photos
        # driver.find_element_by_name("photo").clear()
        # driver.find_element_by_name("photo").send_keys(contact.photo)

        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)

        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)

        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)

        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.home_phone_num)

        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.cell_phone_num)

        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.work_phone_num)

        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)

        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email1)

        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.email2)

        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.email3)

        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(contact.homepage)

        Select(driver.find_element_by_name("bday")).select_by_visible_text(
            contact.bday
        )

        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(
            contact.bmonth
        )

        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.byear)


        Select(driver.find_element_by_name("aday")).select_by_visible_text(
            contact.aday
        )


        Select(driver.find_element_by_name("amonth")).select_by_visible_text(
            contact.amonth
        )

        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(contact.ayear)

        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(contact.address2)

        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(contact.home_phone_2)

        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.notes)

        # submit form
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
