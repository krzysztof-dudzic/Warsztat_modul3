# Generated by Django 3.1.7 on 2021-04-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_app', '0002_auto_20210418_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=True, max_length=255, unique=True),
        ),
    ]
