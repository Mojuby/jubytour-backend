from unicodedata import category, decimal
from xmlrpc.client import boolean
from django.db import models
from django.template.defaultfilters import slugify
import uuid
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
my_choice = (
    ('one', 'number One'),
    ('two', 'number Two')

)

class Customer_Info(models.Model):
    boolean = models.BooleanField(default=True, verbose_name='this is a boolean field', null=True)
    char = models.CharField(verbose_name='New name', max_length=200, unique=True, help_text='added help text', null=True)
    date = models.DateField(default=timezone.now, null=True)
    decimal = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    email = models.EmailField(max_length=200, null= True)
    file = models.FileField(upload_to='uploads', blank=True, null=True)
    integer = models.IntegerField(null=True)
    positive_int = models.PositiveBigIntegerField(null=True)

    slug = models.SlugField(blank=True)
    text = models.TextField(null=True)
    url = models.URLField(max_length=200, null=True)
    uuid1 = models.UUIDField(default= uuid.uuid4, null=True)
    uuid2 = models.UUIDField(default= uuid.uuid4, primary_key=True, editable=False)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateField(auto_now_add=True, null=True)
    date_and_time = models.DateTimeField(null=True)
    choice = models.CharField(max_length=10, choices= my_choice, null=True)

    new_field = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.char



class Meal(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200,null=True, blank=True)
    category = models.CharField(max_length=200,null=True, blank=True)
    description = models.CharField(max_length=200,null=True, blank=True)
    rating = models.DecimalField(max_digits=7,null=True, decimal_places=2, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countinstock = models.IntegerField(null=True, blank=True, default=0)
    createdat = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

        