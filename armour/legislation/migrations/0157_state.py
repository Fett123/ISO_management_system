# Generated by Django 2.2 on 2020-07-07 11:05

from django.db import migrations
def load_state(apps, schema_editor):
    LegistationTopicsResponse = apps.get_model("legislation", "LegistationTopicsResponse")
    for c in LegistationTopicsResponse.objects.all():
        repyes = c.topicresponsekeyp.filter(response__in=[1]).distinct().count()
        repno = c.topicresponsekeyp.filter(response__in=[0]).distinct().count()
        repall = repyes+repno
        if c.isostandard:
            kp = c.isostandard.kpoints.filter(published=True).distinct().count()
        elif c.req:
            kp = c.req.reqpoints.filter(published=True).distinct().count()

        if repyes >= kp:
            status = 3
        elif repall>=kp and repno>0:
            status = 1
        else:
            status = 2

        c.status = status
        c.save()

class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0156_auto_20200707_1057'),
    ]

    operations = [
        migrations.RunPython(load_state),
    ]