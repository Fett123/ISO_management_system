# Generated by Django 2.2 on 2020-06-22 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0062_auto_20200622_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='tax',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='VAT'),
        ),
    ]
