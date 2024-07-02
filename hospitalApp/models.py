from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django_summernote.fields import SummernoteTextField


# Create your models here.

class Appointment(models.Model):
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    country_code = CountryField(default='US')
    phoneNumber = PhoneNumberField(blank = False, null = False, unique = True)
    address = models.CharField(max_length = 150)
    everApplied = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    procedure = models.CharField(max_length=100)
    appointmentDate = models.DateTimeField()



class BlogPosts(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='blogImages/')
    imageInPage = models.ImageField(upload_to='blogImages/')
    title =models.CharField(max_length=200)
    body = SummernoteTextField()
    created_on = models.DateTimeField(auto_now_add=True)



class PricingList(models.Model):
    pricedItem = models.CharField(max_length=200)
    price = models.IntegerField()


class DoctorsList(models.Model):
    docImage = models.ImageField(upload_to='doctorsImage/')
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    about = models.TextField()

    


