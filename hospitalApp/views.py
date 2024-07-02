from django.shortcuts import render
from django.views.generic import CreateView
from .models import Appointment, BlogPosts, PricingList, DoctorsList
from .forms import AppointmentForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def appoint(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        country_code = request.POST.get('country_code')
        phoneNumber = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        everApplied = request.POST.get('everApplied')
        department = request.POST.get('department')
        procedure = request.POST.get('procedure')
        appointmentDate = request.POST.get('appointmentDate')
        
        appointment = Appointment(firstName = firstName, lastName = lastName, email = email,
                                  dob = dob, gender = gender, country_code = country_code, phoneNumber = phoneNumber,
                                  address = address, everApplied = everApplied, department = department,
                                  procedure = procedure, appointmentDate = appointmentDate)
       
        if AppointmentForm(request.POST).is_valid():
            appointment.save()
            success_message = "successfully sent!"
            return render(request, 'appoint.html', {'form': AppointmentForm, 'message': success_message})
        else:
            error_message = "There was an error"
            return render(request, 'appoint.html', {'form': AppointmentForm, 'message': error_message})
    return render(request, 'appoint.html', {'form': AppointmentForm})

def price(request):
    pricingStuff = PricingList.objects.all()
    return render(request, 'pricing.html', {'pricingStuff': pricingStuff })

def about(request):
    return render(request, 'about.html')

def doctors(request):
    doctorsInfo = DoctorsList.objects.all()
    return render(request, 'doctors.html', {'doctorsInfo': doctorsInfo})


def blogList(request):
    posts = BlogPosts.objects.all()
    return render(request, 'blogList.html', {'posts': posts})


def blogPost(request, title):
    posts = BlogPosts.objects.get(title=title)
    return render(request, 'blogPost.html', {'posts': posts})

