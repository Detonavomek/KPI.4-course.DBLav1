from django.core.management.base import BaseCommand, CommandError
from source.settings import DATABASES
import MySQLdb

from main.start_data import start_data


def fill_db(start_data):
    db = MySQLdb.connect(DATABASES['default']['HOST'], DATABASES['default']['USER'],
                         DATABASES['default']['PASSWORD'], DATABASES['default']['NAME'])
    cursor = db.cursor()
    cursor.execute(start_data)
    cursor.close()
    db.close()


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        fill_db(start_data)
