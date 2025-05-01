from django.db import models

from category.models import CommonInfo, SubCategory


class Item(CommonInfo):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    article = models.CharField(max_length=100, blank=True, null=True)
    count = models.PositiveIntegerField(default=0)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    link = models.CharField(null=True, blank=True)
    class Meta:
        db_table = 'item_tb'
        verbose_name_plural = "Товары"
        verbose_name = "Товар"


class Recall(models.Model):
    RATE_CHOICE = (
        (1, "Ужасно"),
        (2, "Плохо"),
        (3, "Хорошо"),
        (4, "Превосходно"),
    )
    full_name = models.CharField(max_length=250)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICE, null=True, blank=True)

    class Meta:
        db_table = 'rate_tb'
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"

    def __str__(self):
        return f"{self.full_name} -> {self.rate}"