# Generated by Django 2.2 on 2020-07-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0069_payments_refundreason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='refundreason',
        ),
        migrations.AddField(
            model_name='company',
            name='version',
            field=models.CharField(max_length=1000, null=True),
        )
    ]