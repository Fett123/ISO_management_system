# Generated by Django 2.2 on 2019-10-11 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0060_auto_20191011_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='legistationtopicsresponse',
            name='req',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reqreply', to='legislation.Requirments'),
        ),
        migrations.AlterField(
            model_name='legistationtopicsresponse',
            name='legtopic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ltopicreply', to='legislation.LegislationTopic'),
        ),
    ]
