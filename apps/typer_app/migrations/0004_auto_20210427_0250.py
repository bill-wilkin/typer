# Generated by Django 2.2 on 2021-04-27 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typer_app', '0003_session_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]