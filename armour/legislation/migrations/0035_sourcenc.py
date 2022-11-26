# Generated by Django 2.2 on 2019-09-10 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0034_auto_20190909_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceNC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'NC Sources',
                'verbose_name_plural': 'NC Sources',
            },
        ),
    ]
