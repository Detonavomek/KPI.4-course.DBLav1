from django.core.management.base import BaseCommand, CommandError
#import settings
import MySQLdb

from Laba1.start_data import start_data

my_account = {
    'host': 'localhost',
    'user': 'root',
    'password': 'letsykao',
    'db': 'DBLaba1',
}

def fill_db(account, start_data):
	db = MySQLdb.connect(my_account['host'],my_account['user'],
		my_account['password'],my_account['db'])
	# db = MySQLdb.connect(host=account['host'], user=account['user'], password=account['password'], db=account['db'])
	cursor = db.cursor()
	cursor.execute(start_data)
	cursor.close()
	db.close()

class Command(BaseCommand):
	help = ''

	def handle(self, *args, **options):
		fill_db(my_account, start_data)    