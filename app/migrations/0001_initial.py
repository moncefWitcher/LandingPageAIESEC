# Generated by Django 3.2.5 on 2022-11-15 17:38

import app.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('picture', models.ImageField(blank=True, upload_to=app.models.upload_path)),
                ('venue_address', models.TextField()),
                ('venue_address_LINK_maps', models.TextField()),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('registration_link_form', models.TextField()),
                ('time', models.IntegerField()),
                ('AIESECERS_or_youth', models.BooleanField()),
                ('link_page', models.TextField()),
                ('limited_places_OR_nonlimited', models.BooleanField()),
                ('city_name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joinAIESC', models.TextField()),
                ('beApartner', models.TextField()),
                ('EP', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('Answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LCs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('vision', models.TextField()),
                ('picture', models.ImageField(blank=True, upload_to=app.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='MC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('why', models.TextField()),
                ('how', models.TextField()),
                ('what', models.TextField()),
                ('vision', models.TextField()),
                ('picture', models.ImageField(blank=True, upload_to=app.models.upload_path)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='social_media_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.TextField()),
                ('insta', models.TextField()),
                ('linkedin', models.TextField()),
                ('facebook', models.TextField()),
                ('departents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MCTEAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('picture', models.ImageField(blank=True, upload_to=app.models.upload_path)),
                ('whatsapp', models.TextField()),
                ('insta', models.TextField()),
                ('linkedin', models.TextField()),
                ('facebook', models.TextField()),
                ('deparment', models.TextField()),
                ('mcParent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mc')),
            ],
        ),
    ]
