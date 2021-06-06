from django.db import models
from datetime import datetime
from django.utils.crypto import get_random_string
import string


class Listing(models.Model):
    identifier = models.CharField(default=get_random_string(5, string.ascii_uppercase + string.digits),
                                  max_length=5)
    transactions = models.CharField(blank=True, max_length=10, choices=(
        ('1', 'Inchiriere'),
        ('2', 'Vanzare'),
    ))
    types = models.CharField(max_length=50, choices=(
        ('1', 'Garsoniera'),
        ('2', 'Apartament'),
        ('3', 'Casa'),
        ('4', 'Teren'),
    )
                             )
    title = models.CharField(max_length=3000)
    description = models.TextField(blank=False, max_length=20000)
    year = models.CharField(max_length=50, blank=True, choices=(
        ('1', 'Inainte de 1977'),
        ('2', '1977 - 1990'),
        ('3', '1990 - 2000'),
        ('4', 'Dupa 2000'),
    ))
    subdivision = models.CharField(max_length=100, blank=True, choices=(
        ('1', 'Decomandat'),
        ('2', 'Semidecomandat'),
        ('3', 'Circular'),
    ))
    rooms = models.CharField(max_length=10, blank=True, choices=(
        ('1', '1 Camere'),
        ('2', '2 Camere'),
        ('3', '3 Camere'),
        ('4', '4+ Camere'),
    ))
    bathrooms = models.IntegerField(blank=True, null=True)
    surface = models.IntegerField()
    floor = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(db_index=True)
    negociable = models.BooleanField(default=False)
    currency = models.CharField(max_length=10, blank=True, choices=(
        ('1', '€'),
        ('2', 'RON'),
    ))
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=10, blank=True, choices=(
        ('1', 'Sector 1'),
        ('2', 'Sector 2'),
        ('3', 'Sector 3'),
        ('4', 'Sector 4'),
        ('5', 'Sector 5'),
        ('6', 'Sector 6'),
    ))
    photo_main = models.ImageField(blank=False, upload_to='static/admin/img/listing_photo')
    photo_1 = models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')
    photo_2 = models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')
    photo_3 = models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')
    photo_4 = models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')
    photo_5 = models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')
    photo_6 = models.ImageField(blank=True, upload_to='static/admin/img/listing_photo')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'Listings'

    def __str__(self):
        return self.title


