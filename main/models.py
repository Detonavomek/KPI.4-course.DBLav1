from source.settings import DATABASES
from django.db import models
import os
import MySQLdb
#import xml.etree.ElementTree as ET


def execute_query(query):
    db = MySQLdb.connect(
        DATABASES['default']['HOST'], DATABASES['default']['USER'],
        DATABASES['default']['PASSWORD'], DATABASES['default']['NAME'])
    cursor = db.cursor()
    print query
    cursor.execute("BEGIN;" + query + "COMMIT;")
    result = cursor.fetchall()
    print result
    cursor.close()
    db.close()
    return result


class MyORM():

    def __init__(self, params):
        self.params = params

    def get_table_field(self):
        return ', '.join(self.table_fields)

    def get_params(self):
        fields_data = []
        for field in self.table_fields:
            field_data = '\'%s\'' % self.params[field]
            fields_data.append(field_data)
        return ', '.join(fields_data)

    def insert(self):
        execute_query("INSERT INTO %s(%s) VALUES(%s);" %
                      (self.table_name, self.get_table_field(), self.get_params()))


class Account(MyORM):
    table_name = "Laba1_account"
    table_fields = ["amount", "manager", "dateCreating"]


class Pet(MyORM):
    table_name = "Laba1_pet"
    table_fields = ["name", "age", "specie"]
