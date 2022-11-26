# Generated by Django 3.2.10 on 2021-12-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0184_auto_20211224_0850'),
        ('company', '0076_auto_20211223_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='plan',
            field=models.ManyToManyField(blank=True, to='legislation.Plan', verbose_name='Plan'),
        ),
    ]