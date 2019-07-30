# Generated by Django 2.2.3 on 2019-07-30 20:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_books_app', '0005_book_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='website_alternative_way',
            field=models.URLField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='website',
            field=models.TextField(null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
