# Generated by Django 2.2 on 2020-04-15 04:37

from django.db import migrations

def load_version(apps, schema_editor):
    LegislationVersion = apps.get_model("legislation", "LegislationVersion")
    h = LegislationVersion.objects.get(version='1.0.0')
    h.no=1
    h.published = True
    h.save()

class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0121_auto_20200415_0314'),
    ]

    operations = [
        migrations.RunPython(load_version),
    ]