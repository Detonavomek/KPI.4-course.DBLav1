from source.settings import DATABASES
from django.db import models
import os
import MySQLdb


def execute_query(query, select=False):
    db = MySQLdb.connect(
        DATABASES['default']['HOST'], DATABASES['default']['USER'],
        DATABASES['default']['PASSWORD'], DATABASES['default']['NAME'])
    cursor = db.cursor()
    if select:
        cursor.execute(query)
    else:
        cursor.execute("BEGIN;" + query + "COMMIT;")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


class MyORM():

    def __init__(self, params={}):
        self.params = params

    @classmethod
    def get(cls, _id):
        fields_data = []
        row = execute_query(
            "SELECT %s FROM %s WHERE id=%i;" % (cls.get_table_field(), cls.table_name, _id), True)[0]
        obj = cls()
        obj.id = _id
        row = [el for el in row]
        for index, item in enumerate(cls.table_fields):
            obj.params[item] = row[index]
        return obj

    @classmethod
    def get_all(cls):
        fields_data = []
        rows = execute_query(
            "SELECT id, %s FROM %s;" % (cls.get_table_field(), cls.table_name), True)
        objs = []
        for row in rows:
            obj = cls()
            print '> ', obj.params
            row = [el for el in row]
            obj.id = row.pop(0)
            for index, item in enumerate(cls.table_fields):
                print '>>> ', item
                obj.params[item] = row[index]
            objs.append(obj)
        return objs

    @classmethod
    def get_table_field(cls):
        return ', '.join(cls.table_fields)

    def get_params(self):
        fields_data = []
        for field in self.table_fields:
            field_data = '\'%s\'' % self.params[field]
            fields_data.append(field_data)
        return ', '.join(fields_data)

    def get_update_query_part(self):
        result = []
        for field in self.table_fields:
            result.append(field + "=\"%s\"" % self.params[field])
        return ', '.join(result)

    def save(self):
        if not getattr(self, 'id', None):
            execute_query("INSERT INTO %s(%s) VALUES(%s);" %
                          (self.table_name, self.get_table_field(), self.get_params()))
            self.id = execute_query(
                "SELECT id FROM %s;" % (self.table_name), True)[0][0]
        else:
            execute_query("UPDATE %s SET %s WHERE id=%s;" %
                          (self.table_name, self.get_update_query_part(), self.id))

    def delete(self):
        execute_query("DELETE FROM %s WHERE id=%i;" %
                      (self.table_name, self.id))

    def to_string(self):
        return str(self.id)


class Table1(MyORM):
    table_name = "table1"
    table_fields = ["field1", "field2", "date"]

    def to_string(self):
        return self.params['field1']


class Table2(MyORM):
    table_name = "table2"
    table_fields = ["field3", "field4", "date"]

    def to_string(self):
        return str(self.params['date']) + ": " + self.params['field4']


class Table3(MyORM):
    table_name = "table3"
    table_fields = ["table1_id", "table2_id", "field5"]

main_table = Table3
