import mysql.connector

from models.group import Group
from models.contact import Contact


class DbFixture():
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(
            host=host, database=name, user=user, password=password,
            autocommit=True
        )

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT group_id, group_name, group_header, group_footer "
                "FROM group_list"
            )
            for row in cursor:
                (id, name, header, footer) = row
                list.append(
                    Group(id=str(id), name=name, header=header, footer=footer)
                )
        finally:
            cursor.close()
        return list

    def get_group_by_id(self, id):
        group = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT group_id, group_name, group_header, group_footer "
                "FROM group_list "
                f"WHERE group_id={id}"
            )
            # group = Group(id=str(id), name=name, header=header, footer=footer)
            for row in cursor:
                (id, name, header, footer) = row
                group = Group(
                    id=str(id), name=name, header=header, footer=footer
                )
        finally:
            cursor.close()
        return group


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT id, firstname, lastname, address, email "
                "FROM addressbook "
                "WHERE deprecated='0000-00-00 00:00:00'"
            )
            for row in cursor:
                (id, firstname, lastname, address, email) = row
                list.append(
                    Contact(
                        id=str(id),
                        first_name=firstname,
                        last_name=lastname,
                        address=address,
                        email1=email
                    )
                )
        finally:
            cursor.close()
        return list

    def get_contact_by_id(self, id):
        contact = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT id, firstname, lastname, address, email "
                "FROM addressbook "
                "WHERE deprecated='0000-00-00 00:00:00' AND id=%s" % id
            )
            for row in cursor:
                (id, firstname, lastname, address, email) = row
                contact = Contact(
                        id=str(id),
                        first_name=firstname,
                        last_name=lastname,
                        address=address,
                        email1=email
                    )
        finally:
            cursor.close()
        return contact

    def destroy(self):
        self.connection.close()
