# Generated by Django 2.2 on 2020-04-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0043_auto_20200402_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='free',
            field=models.BooleanField(default=False, verbose_name='Free'),
        ),
    ]
