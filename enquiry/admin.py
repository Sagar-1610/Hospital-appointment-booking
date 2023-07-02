from django.contrib import admin
from enquiry.models import Enquiry
# Register your models here.

class EnquiryAdi(admin.ModelAdmin):
    model = Enquiry
    list_display = ('Visiting_Department','gender','full_name','dob','nationality','aadhar_no','Country',"state","city","mobile","email")

admin.site.register(Enquiry,EnquiryAdi)
