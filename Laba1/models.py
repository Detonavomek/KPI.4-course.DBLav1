from django.db import models
import os
#from django.conf import settings
#from django.shortcuts import render
#import xml.etree.ElementTree as ET 
import MySQLdb
from Laba1DB import settings
# from django.core.settings import my_account as account

def execute_query(query):
	db = MySQLdb.connect(settings.my_account['host'],settings.my_account['user'],
		settings.my_account['password'],settings.my_account['db'])
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
	
# class Pet(models.Model):
# 	name = models.CharField(max_length=15)
# 	age = models.IntegerField(default=0)
# 	specie = models.CharField(max_length=15)

# class Job(models.Model):
# 	name = models.CharField(max_length = 20)
# 	salary = models.IntegerField(default=0)

# class Human(models.Model):
# 	account = models.ForeignKey(Account)
# 	job = models.ForeignKey(Job)
# 	pet = models.ForeignKey(Pet)
# 	name = models.CharField(max_length=20)
# 	age = models.IntegerField(default=0)
