# Generated by Django 2.2 on 2019-10-30 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0061_auto_20191011_0040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='legislationtopic',
            options={'ordering': ['title'], 'verbose_name': 'Legislation topic', 'verbose_name_plural': 'Legislation topics'},
        ),
    ]
