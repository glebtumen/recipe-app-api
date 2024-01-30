"""
Django command to wait for db to be available
"""


import time
from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django comman for wait"""
    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting for 1 sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))