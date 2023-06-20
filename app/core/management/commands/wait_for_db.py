"""
Custom Django management command to wait for the database to be available.
"""
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """ Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        is_database_up = False
        while is_database_up is False:
            try:
                self.check(databases=['default'])
                is_database_up = True
            except (Psycopg2OpError, OperationalError ):
                self.stdout.write(self.style.WARNING('Database is unavailable, waiting 1 second...'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available!'))