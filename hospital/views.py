from django.shortcuts import render
from enquiry.models import Enquiry
from django.core.mail import send_mail,EmailMultiAlternatives
import random

def HomePage(request):
    return render(request,"Main.html")

def Appointment(request):
    n = ''
    if request.method=="POST":
        visiting =request.POST.get("department")
        gender =request.POST.get("gender")
        name =request.POST.get("name")
        dob =request.POST.get("dob")
        nationality= request.POST.get("nationality")
        aadhar =request.POST.get("Aadhar")
        country =request.POST.get("country")
        state =request.POST.get("state")
        city =request.POST.get("city")
        mobile =request.POST.get("mobile",)
        email =request.POST.get("email")
        en = Enquiry(Visiting_Department= visiting, gender=gender, full_name=name, dob=dob, nationality=nationality,aadhar_no= aadhar, Country = country, state= state,city= city, mobile= mobile,email=email)
        en.save()
       
        x= random.randint(10,50)
        n = "You have successfully booked Your appointment.Your appointment no. is{}.further information please check your mail".format(x)

        subject='APPOINTMENT BOOKING'
        message= '''<p>Dear Mr.<b>{}</b>,<br>I would like to confirm your appointment with Thomas on Tomorrow, at 6:00 PM.Your appointment number is <b>{}</b> If you have any questions or want to request changes, please contact me.
                    <br>Regards,
                    <br>Edward.<br>+1245879631</p>'''.format(name,x)
        from_email='medimax252525@gmail.com'
        recipient_list=[email]
        msg = EmailMultiAlternatives(subject,message,from_email,recipient_list,)
        msg.content_subtype='html'
        msg.send()   
        fail_silently=False
    return render(request,"Appointment.html",{'n':n})

