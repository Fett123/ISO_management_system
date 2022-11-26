# Generated by Django 2.2 on 2019-04-26 00:37

from django.db import migrations

def load_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    s = Site.objects.all()
    if not s:
        s = Site(name="example.com",domain="example.com")
        s.save()
    else:
        s = s[0]

    PriceSettings = apps.get_model("legislation", "PriceSettings")

    h = PriceSettings.objects.create(site=s)

class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0007_pricesettings'),
    ]

    operations = [
        migrations.RunPython(load_site),
    ]
