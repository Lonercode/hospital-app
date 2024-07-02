from django.contrib import admin
from .models import Appointment, BlogPosts, PricingList, DoctorsList
from django.db import models
from django_summernote.widgets import SummernoteWidget
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPosts)
class BlogPostsAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

@admin.register(PricingList)
class PricingListAdmin(admin.ModelAdmin):
    pass

@admin.register(DoctorsList)
class DoctorsListAdmin(admin.ModelAdmin):
    pass