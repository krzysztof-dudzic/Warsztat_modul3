# Generated by Django 3.1.7 on 2021-04-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_app', '0006_auto_20210418_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='projector',
            field=models.BooleanField(default=False),
        ),
    ]
