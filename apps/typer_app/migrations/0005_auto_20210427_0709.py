# Generated by Django 2.2 on 2021-04-27 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typer_app', '0004_auto_20210427_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='score',
        ),
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
