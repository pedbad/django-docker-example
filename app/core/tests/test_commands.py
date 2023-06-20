"""
Test custom Django management commands.
"""

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

from psycopg2 import OperationalError as psycopg2Error
from unittest.mock import patch

@patch('core.management.commands.wait_for_db.Command.check')  # Mocking the check method of the wait_for_db command
class CommandTests(SimpleTestCase):
    """ Test wait_for_db command. """

    def test_wait_for_db_ready(self, patched_check):
        """ Test waiting for database when the database is ready. """
        patched_check.return_value = True  # Mocking the return value of the check method to indicate database readiness

        call_command('wait_for_db')  # Calling the wait_for_db command

        patched_check.assert_called_once_with(database=['default'])  # Asserting that the check method was called with the correct arguments
        

