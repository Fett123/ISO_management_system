# Generated by Django 2.2 on 2019-08-12 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0023_payments_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentspositions',
            old_name='locations',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='paymentspositions',
            old_name='topics',
            new_name='topic',
        ),
    ]
