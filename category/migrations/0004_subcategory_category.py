# Generated by Django 4.2.20 on 2025-04-23 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0003_subcategory_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="subcategory",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sub_categories",
                to="category.category",
            ),
            preserve_default=False,
        ),
    ]
