# Generated by Django 3.1.7 on 2021-04-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_app', '0003_auto_20210418_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]