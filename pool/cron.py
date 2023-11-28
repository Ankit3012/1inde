from django.core.management.base import BaseCommand
from pool.models import Ghadi
from datetime import date

class Command(BaseCommand):
    help = 'Create new data row for Ghadi model'

    def handle(self, *args, **kwargs):
        Ghadi.objects.create()
        self.stdout.write(self.style.SUCCESS('Successfully created new data row for Ghadi model'))
