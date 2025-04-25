from django.core.management.base import BaseCommand, CommandError

from category.models import Category
from constants import CATEGORY_DATA
from messages import CREATE_CATEGORY_MESSAGE, CREATE_CATEGORY_SUCCESS_MESSAGE


class Command(BaseCommand):
    help = CREATE_CATEGORY_MESSAGE

    def handle(self, *args, **kwargs):
        self.create_categories()

    def create_categories(self):
        Category.objects.bulk_create(CATEGORY_DATA)
        self.stdout.write(
            self.style.SUCCESS(CREATE_CATEGORY_SUCCESS_MESSAGE)
        )