# Generated by Django 2.2 on 2019-04-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0013_auto_20190426_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Default'),
        ),
    ]