# Generated by Django 2.2 on 2019-08-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0021_auto_20190812_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='success',
            field=models.BooleanField(default=False, verbose_name='Success'),
        ),
    ]