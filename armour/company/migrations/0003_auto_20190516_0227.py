# Generated by Django 2.2 on 2019-05-16 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Company'},
        ),
    ]
