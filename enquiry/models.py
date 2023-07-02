from django.db import models

# Create your models here.

class Enquiry(models.Model):
    Visiting_Department =models.CharField(max_length=70)
    gender = models.CharField(max_length=20,choices=(("Male","Male"),("Female","Female"),("Transgender","Transgender"),("Ambiguous","Ambiguous")))
    full_name = models.CharField(max_length=50)
    dob = models.DateField()
    nationality = models.CharField(max_length=50)
    aadhar_no = models.IntegerField()
    Country = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    mobile = models.IntegerField()
    email = models.CharField(max_length=80)
