# Generated by Django 3.2.5 on 2022-12-26 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_lcmembers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mcteam',
            old_name='linkedin',
            new_name='gmail',
        ),
        migrations.RenameField(
            model_name='mcteam',
            old_name='whatsapp',
            new_name='twiter',
        ),
    ]
