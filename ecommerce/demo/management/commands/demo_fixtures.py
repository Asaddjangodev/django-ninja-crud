from django.core.management import call_command
from django.core.management.base import BaseComand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command('makemigrations')
        call_command('migrate')
        call_command('loaddata', 'db_admin_fixture.json')
