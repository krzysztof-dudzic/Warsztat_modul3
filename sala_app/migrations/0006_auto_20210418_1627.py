# Generated by Django 3.1.7 on 2021-04-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_app', '0005_auto_20210418_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.SmallIntegerField(),
        ),
    ]
