# Generated by Django 2.2 on 2020-06-16 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0147_auto_20200616_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='vat',
        ),
    ]