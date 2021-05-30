# Generated by Django 3.2 on 2021-05-30 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(default='QRCAI', max_length=5)),
                ('transactions', models.CharField(blank=True, choices=[('1', 'Inchiriere'), ('2', 'Vanzare')], max_length=10)),
                ('types', models.CharField(choices=[('1', 'Garsoniera'), ('2', 'Apartament'), ('3', 'Casa'), ('4', 'Teren')], max_length=50)),
                ('title', models.CharField(max_length=3000)),
                ('description', models.TextField(max_length=20000)),
                ('year', models.CharField(blank=True, choices=[('1', 'Inainte de 1977'), ('2', '1977 - 1990'), ('3', '1990 - 2000'), ('4', 'Dupa 2000')], max_length=50)),
                ('subdivision', models.CharField(blank=True, choices=[('1', 'Decomandat'), ('2', 'Semidecomandat'), ('3', 'Circular')], max_length=100)),
                ('rooms', models.CharField(blank=True, choices=[('1', '1 Camere'), ('2', '2 Camere'), ('3', '3 Camere'), ('4', '4+ Camere')], max_length=10)),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('surface', models.IntegerField()),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(db_index=True)),
                ('negociable', models.BooleanField(default=False)),
                ('currency', models.CharField(blank=True, choices=[('1', '€'), ('2', 'RON')], max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(blank=True, choices=[('1', 'Sector 1'), ('2', 'Sector 2'), ('3', 'Sector 3'), ('4', 'Sector 4'), ('5', 'Sector 5'), ('6', 'Sector 6')], max_length=10)),
                ('photo_main', models.ImageField(upload_to='static/admin/img/listing_photo')),
                ('photo_1', models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')),
                ('photo_2', models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')),
                ('photo_3', models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')),
                ('photo_4', models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')),
                ('photo_5', models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')),
                ('photo_6', models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Listings',
            },
        ),
    ]