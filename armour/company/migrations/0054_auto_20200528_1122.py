# Generated by Django 2.2 on 2020-05-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0053_auto_20200511_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Website'),
        ),
    ]