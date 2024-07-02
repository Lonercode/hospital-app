from django import forms
from .models import Appointment
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField

genderChoice = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('none', 'Rather not disclose')
)

departmentChoice = (
    ('physiotherapy', 'Physiotherapy'),
    ('gyneacology', 'Gyneacology'),
    ('neurology', 'Neuorology')
)

appliedChoice = (
    ('yes', 'yes'),
    ('no', 'no')
)

widget=forms.TextInput(attrs={'placeholder': ('Phone')})

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class AppointmentForm(forms.ModelForm):
    firstName = forms.CharField(label="First Name",  widget=forms.TextInput(attrs={'class':'textFields'}))
    lastName = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':'textFields'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'textFields'}))
    dob = forms.DateField(label="Date of Birth", widget=DateInput)
    gender = forms.CharField(label="Gender",
                                widget=forms.Select(choices=genderChoice, attrs={'class':'dropDowns'}))
    country_code = CountryField().formfield()
    phoneNumber = PhoneNumberField( widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        help_text='Enter without leading zero')
    
    address = forms.CharField(label="Address", widget=forms.TextInput(attrs={'class':'textFields'}))
    everApplied = forms.ChoiceField(label=" Applied before?",
        widget=forms.RadioSelect, choices=appliedChoice
    )
    department = forms.CharField(label="Department",
                                widget=forms.Select(choices=departmentChoice, attrs={'class':'dropDowns'}))
    procedure = forms.CharField(label="What procedure?", widget=forms.TextInput(attrs={'class':'textFields'}))
    appointmentDate = forms.DateTimeField(label = "Appointment Date", widget=DateTimeInput(attrs={'class':'dateStyle'}))

    class Meta:
        model = Appointment
        fields = ['firstName', 'lastName', 'email', 'dob', 'gender', 'country_code','phoneNumber', 'address',
                  'everApplied', 'department', 'procedure', 'appointmentDate']
    
