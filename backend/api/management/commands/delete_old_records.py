from django.core.management.base import BaseCommand, CommandError
from api.models import secret
from datetime import datetime, timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = 'Deletes old records from the password database.'

    def handle(self, *args, **options):
        time_threshold = datetime.now(tz=timezone.utc) - timedelta(hours=1)
        secret.objects.filter(created_at__lt=time_threshold).delete()
        self.stdout.write('Deleted old records from the databases')
        # self.stdout.write(time_threshold)
