# Generated by Django 2.2 on 2021-01-29 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0162_auto_20210129_1405'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LegistationSpecQuestion',
            new_name='LegislationSpecQuestion',
        ),
    ]