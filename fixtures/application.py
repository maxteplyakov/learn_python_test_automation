from selenium import webdriver

from fixtures.session import SessionHelper
from fixtures.group import GroupHelper
from fixtures.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(1)  # если делать строго по вебинару эту строку нужно убрать, но без нее не всегда успевают прогрузиться элементы и некоторые тесты падают
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith('/addressbook/'):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
