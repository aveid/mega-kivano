from django.core.management.base import BaseCommand

from category.models import SubCategory
from constants import SUB_CATEGORY_DATA
from messages import CREATE_SUB_CATEGORY_SUCCESS_MESSAGE


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.create_sub_categories()

    def create_sub_categories(self):
        SubCategory.objects.bulk_create(SUB_CATEGORY_DATA)
        self.stdout.write(
            self.style.SUCCESS(CREATE_SUB_CATEGORY_SUCCESS_MESSAGE)
        )