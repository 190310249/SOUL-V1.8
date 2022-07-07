from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Contact,
    Home_slider,
    Home_recentventures,
    Home_testimonials,
    Home_joinus,
    Home_monthlyupdate,
    About_slider,
    About_volunteer,
    volunteer,
    donation,
    event,
    Project,
    Project_slider,
    Project_recentventures,

)
# HOME PAGE MODEL--STARTING

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
 list_display = ['msg_id', 'name', 'email', 'phone']

@admin.register(Home_slider)
class Home_sliderModelAdmin(admin.ModelAdmin):
 list_display = ['hs_id', 'name', 'Homeslider_link', 'Homeslider_image']

@admin.register(Home_recentventures)
class Home_recentventuresModelAdmin(admin.ModelAdmin):
 list_display = ['hrv_id', 'name', 'Home_recentventures_date', 'Home_recentventures_caption', 'Home_recentventures_image']

@admin.register(Home_testimonials)
class Home_testimonialsModelAdmin(admin.ModelAdmin):
 list_display = ['ht_id', 'name', 'Home_testimonials_date', 'Home_testimonials_designation', 'Home_testimonials_image', 'verification']

@admin.register(Home_joinus)
class Home_joinusModelAdmin(admin.ModelAdmin):
 list_display = ['hj_id', 'Home_joinus_name', 'Home_joinus_phone', 'Home_joinus_email', 'Home_joinus_location']

@admin.register(Home_monthlyupdate)
class Home_monthlyupdateModelAdmin(admin.ModelAdmin):
 list_display = ['hmu_id', 'Home_joinus_email']

# HOME PAGE MODEL--ENDING

# ABOUT PAGE MODEL--STARTING

@admin.register(About_slider)
class About_sliderModelAdmin(admin.ModelAdmin):
 list_display = ['as_id', 'name', 'Aboutslider_link', 'Aboutslider_image']
 


@admin.register(About_volunteer)
class About_volunteerModelAdmin(admin.ModelAdmin):
 list_display = ['av_id', 'name', 'Aboutvolunteer_link', 'Aboutvolunteer_image', 'volunteer_date']

# ABOUT PAGE MODEL--ENDING


# JOIN US  PAGE MODEL--STARTING

@admin.register(volunteer)
class volunteerModelAdmin(admin.ModelAdmin):
 list_display = ['v_id', 'email', 'gender', 'name', 'ph_number', 'blood_gp', 'profession', 'soc_link', 'birth_date']

# JOIN US  PAGE MODEL--ENDING

# DONATION  PAGE MODEL--STARTING

@admin.register(donation)
class donationModelAdmin(admin.ModelAdmin):
 list_display = ['don_id', 'order_id', 'name', 'ph_number', 'email', 'gender', 'profession', 'purpose','ammount', 'don_date']

# DONATION  PAGE MODEL--ENDING

# EVENT PAGE MODEL--STARTING

@admin.register(event)
class eventModelAdmin(admin.ModelAdmin):
 list_display = ['ev_id', 'ev_name', 'ev_desc', 'ev_about', 'ev_venue', 'ev_mode', 'ev_date', 'ev_time', 'ev_status','ev_link']

# EVENT PAGE MODEL--ENDING

# PROJECT PAGE MODEL--STARTING

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
 list_display = ['pr_id', 'pr_name', 'pr_cat', 'pr_mode', 'pr_date', 'pr_time', 'pr_status','pr_link']

@admin.register(Project_slider)
class Project_sliderModelAdmin(admin.ModelAdmin):
 list_display = ['ps_id', 'name', 'Projectslider_cat', 'Projectslider_link', 'Projectslider_image']

@admin.register(Project_recentventures)
class Project_recentventuresModelAdmin(admin.ModelAdmin):
 list_display = ['prv_id', 'name', 'Project_recentventures_cat', 'Project_recentventures_caption', 'Project_recentventures_date', 'Project_recentventures_image']
# PROJECT  PAGE MODEL--ENDING

























# def customer_info(self, obj):
#   link = reverse("admin:app_customer_change", args=[obj.customer.pk])
#   return format_html('<a href="{}">{}</a>', link, obj.customer.name)
 
