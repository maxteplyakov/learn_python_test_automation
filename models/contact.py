from sys import maxsize


class Contact:

    def __init__(
            self,
            first_name=None, middle_name=None, last_name=None,
            nickname=None, photo=None,
            title=None, company=None, address=None,
            home_phone_num=None, cell_phone_num=None, work_phone_num=None,
            fax=None, email1=None, email2=None, email3=None, homepage=None,
            bday=None, bmonth=None, byear=None,
            aday=None, amonth=None, ayear=None,
            address2=None, home_phone_2=None, notes=None, id=None,
            all_phones_from_homepage=None,
            all_phones_from_viewpage=None,
            all_emails_from_homepage=None
    ):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home_phone_num = home_phone_num
        self.cell_phone_num = cell_phone_num
        self.work_phone_num = work_phone_num
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.home_phone_2 = home_phone_2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_phones_from_viewpage = all_phones_from_viewpage
        self.all_emails_from_homepage = all_emails_from_homepage

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (
                self.id is None or other.id is None or self.id == other.id
               ) and self.first_name == other.first_name and\
               self.last_name == other.last_name
