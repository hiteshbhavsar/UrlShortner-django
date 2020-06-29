from django.core.management.base import BaseCommand,CommandError
from ... import models


class Command(BaseCommand):
    help='Used for refreshing codes'

    def add_arguments(self, parser):
        parser.add_argument('number',type=int)

    def handle(self,*args,**options):
        print(options)
        return models.KirrURL.objects.refresh_shortcodes()