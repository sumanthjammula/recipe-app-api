import time
from psycopg2 import OperationalError as Psycopg2opError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.stdout.write('Waiting for Database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases = ['default'])
                db_up = True
            except (Psycopg2opError, OperationalError):
                self.stdout.write('Dataabase unavailabel, waiting for 1 sec')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Availabel'))
                