from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils.html import json_script
# from rest_framework.decorators import api_view
# from rest_framework.serializers import Serializer
# from .forms import JoinUsForm
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.timezone import datetime
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

def home(request):
    homeslider = Home_slider.objects.all()
    # homeslider = homeslider1[::-1]
    Home_recentventure = Home_recentventures.objects.all().order_by('Home_recentventures_date').reverse()
    even = event.objects.filter(ev_status="Upcoming").order_by('ev_date')
    testmo = Home_testimonials.objects.filter(verification="Accepted").order_by('Home_testimonials_date').reverse()

    if request.method == "POST":
        if "email1" in request.POST:
            email = request.POST.get('email1')
            contact = Home_monthlyupdate(Home_joinus_email=email)
            contact.save()
        else:
            contact1=Home_joinus()
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email2')
            loc = request.POST.get('your_location')
            desc = request.POST.get('brief_info')
            contact1 = Home_joinus(Home_joinus_name=name, Home_joinus_email=email, Home_joinus_phone=phone, Home_joinus_location=loc, Home_joinus_desc=desc)
            contact1.save()
    return render(request, 'app/home.html', {'homeslider':homeslider, 'Home_recentventures':Home_recentventure, 'Event':even, 'Testmo':testmo})

def about(request):
    aboutslider = About_slider.objects.all().reverse()
    aboutvol = About_volunteer.objects.all().reverse()
    return render(request, 'app/about.html', {'aboutslider':aboutslider, 'aboutvol':aboutvol})

    
    
def support_us(request):
    return render(request, 'app/support_us.html')

def join_us(request):
    if request.method == "POST":
        vol=volunteer()
        name = request.POST.get('name1')
        email = request.POST.get('email3')
        gender = request.POST.get('gender')
        wpn = request.POST.get('wphone')
        pn = request.POST.get('phone')
        blgr = request.POST.get('blood-group')
        loc = request.POST.get('your_location')
        sour = request.POST.get('source')
        ref = request.POST.get('refferer')
        he = request.POST.get('hg_education')
        prof = request.POST.get('profession')
        org = request.POST.get('org_name')
        hobby = request.POST.get('hobbyskill')
        soc = request.POST.get('soc_link')
        pngo = request.POST.get('past_ngo')
        bdate = request.POST.get('birth_date')
        quer = request.POST.get('query')            
        vol = volunteer(name=name, email=email, gender=gender, wp_number=wpn, ph_number=pn, blood_gp=blgr, Adress=loc, source=sour, refferer=ref, hg_education=he, profession=prof, org_name=org, hobbyskill=hobby, soc_link=soc, past_ngo=pngo, query=quer, birth_date=bdate)
        vol.save()
    return render(request, 'app/join_us.html')

def projects(request):
    projslider = Project_slider.objects.all()
    Proj_recentventure = Project_recentventures.objects.all().order_by('Project_recentventures_date').reverse()
    pro = Project.objects.all().order_by('pr_date').reverse()
    return render(request, 'app/projects.html', {'projslider':projslider, 'Proj_recentventure':Proj_recentventure, 'pro':pro})

def projectswemp(request):
    projslider = Project_slider.objects.all()
    Proj_recentventure = Project_recentventures.objects.filter(Project_recentventures_cat="women empowerment").order_by('Project_recentventures_date').reverse()
    pro = Project.objects.filter(pr_cat="women empowerment").order_by('pr_date').reverse()
    return render(request, 'app/projects_woemp.html', {'projslider':projslider, 'Proj_recentventure':Proj_recentventure, 'pro':pro})

def projectsinnov(request):
    projslider = Project_slider.objects.all()
    Proj_recentventure = Project_recentventures.objects.filter(Project_recentventures_cat="innovation part").order_by('Project_recentventures_date').reverse()
    pro = Project.objects.filter(pr_cat="innovation part").order_by('pr_date').reverse()
    return render(request, 'app/projects_innov.html', {'projslider':projslider, 'Proj_recentventure':Proj_recentventure, 'pro':pro})

def projectshc(request):
    projslider = Project_slider.objects.all()
    Proj_recentventure = Project_recentventures.objects.filter(Project_recentventures_cat="health & care").order_by('Project_recentventures_date').reverse()
    pro = Project.objects.filter(pr_cat="health & care").order_by('pr_date').reverse()
    return render(request, 'app/projects_hc.html', {'projslider':projslider, 'Proj_recentventure':Proj_recentventure, 'pro':pro})

def projectsenv(request):
    projslider = Project_slider.objects.all()
    Proj_recentventure = Project_recentventures.objects.filter(Project_recentventures_cat="environment").order_by('Project_recentventures_date').reverse()
    pro = Project.objects.filter(pr_cat="environment").order_by('pr_date').reverse()
    return render(request, 'app/projects_env.html', {'projslider':projslider, 'Proj_recentventure':Proj_recentventure, 'pro':pro})

def projectsed(request):
    projslider = Project_slider.objects.all()
    Proj_recentventure = Project_recentventures.objects.filter(Project_recentventures_cat="Education").order_by('Project_recentventures_date').reverse()
    pro = Project.objects.filter(pr_cat="Education").order_by('pr_date').reverse()
    return render(request, 'app/projects_ed.html', {'projslider':projslider, 'Proj_recentventure':Proj_recentventure, 'pro':pro})

def projectscorpo(request):
    projslider = Project_slider.objects.all()
    Proj_recentventure = Project_recentventures.objects.filter(Project_recentventures_cat="coordination project").order_by('Project_recentventures_date').reverse()
    pro = Project.objects.filter(pr_cat="coordination project").order_by('pr_date').reverse()
    return render(request, 'app/projects_corpo.html', {'projslider':projslider, 'Proj_recentventure':Proj_recentventure, 'pro':pro})

def projectsany(request):
    projslider = Project_slider.objects.all()
    Proj_recentventure = Project_recentventures.objects.filter(Project_recentventures_cat="Other").order_by('Project_recentventures_date').reverse()
    pro = Project.objects.filter(pr_cat="Other").order_by('pr_date').reverse()
    return render(request, 'app/projects_any.html', {'projslider':projslider, 'Proj_recentventure':Proj_recentventure, 'pro':pro})
