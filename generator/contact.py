import random
import string
import os.path
import json
import getopt
import sys

from models.contact import Contact


try:
    opts, args = getopt.getopt(
        sys.argv[1:], "n:f:",
        ["number of contacts", "file"]
    )
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters +\
              string.digits + ' '*5        # с пробелами чаще валятся тесты
    return prefix + ''.join([random.choice(symbols) for
                             i in range(random.randrange(maxlen))])


def random_email():
    username_symbols = string.ascii_letters +\
                       string.digits +\
                       string.punctuation
    domain_symbols = string.ascii_letters + string.digits
    username = ''.join([random.choice(username_symbols) for
                        i in range(random.randrange(20))])
    domain = ''.join([random.choice(domain_symbols) for
                      i in range(random.randrange(1, 20))])
    return 'email' + username + '@' + domain + '.com'


def random_phone_num():
    symbols = string.digits + '+-()'
    return ''.join([random.choice(symbols) for
                      _ in range(random.randrange(6, 20))])


testdata = [
    Contact(
        first_name='', middle_name='', last_name='',
        nickname='', photo='',
        title='', company='', address='',
        home_phone_num='', cell_phone_num='', work_phone_num='',
        fax='', email1='', email2='', email3='', homepage='',
        bday='-', bmonth='-', byear='',
        aday='-', amonth='-', ayear='',
        address2='', home_phone_2='', notes=''
    )] + [
            Contact(
                first_name=random_string("first_name", 20),
                middle_name=random_string("middle_name", 20),
                last_name=random_string("last_name", 20),
                nickname=random_string("nickname", 20),
                photo='../photo.jpg',
                title=random_string("title", 20),
                company=random_string("company", 20),
                address=random_string("address", 50),
                home_phone_num=random_phone_num(),
                cell_phone_num=random_phone_num(),
                work_phone_num=random_phone_num(),
                fax=random_phone_num(),
                email1=random_email(),
                email2=random_email(),
                email3=random_email(),
                address2=random_string("address2", 100),
                home_phone_2=random_phone_num(),
                notes=random_string("notes", 30),
            ) for _ in range(3)
    ]

file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../" + f
)

with open(file, "w") as output:
    output.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
