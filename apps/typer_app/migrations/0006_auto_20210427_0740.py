# Generated by Django 2.2 on 2021-04-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typer_app', '0005_auto_20210427_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='accuracy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='session',
            name='wpm',
            field=models.IntegerField(),
        ),
    ]
