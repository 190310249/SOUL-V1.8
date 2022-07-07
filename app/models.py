from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import datetime
from django.shortcuts import render
# from .models import Contact
from urllib.parse import urlparse
from django.utils.timezone import now

STATE_CHOICES = (
  ('Odisha','Odisha'),
  # ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
  # ('Andhra Pradesh','Andhra Pradesh'),
  # ('Arunachal Pradesh','Arunachal Pradesh'),
  # ('Assam','Assam'),
  # ('Bihar','Bihar'),
  # ('Chandigarh','Chandigarh'),
  # ('Chhattisgarh','Chhattisgarh'),
  # ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
  # ('Daman and Diu','Daman and Diu'),
  # ('Delhi','Delhi'),
  # ('Goa','Goa'),
  # ('Gujarat','Gujarat'),
  # ('Haryana','Haryana'),
  # ('Himachal Pradesh','Himachal Pradesh'),
  # ('Jammu & Kashmir','Jammu & Kashmir'),
  # ('Jharkhand','Jharkhand'),
  # ('Karnataka','Karnataka'),
  # ('Kerala','Kerala'),
  # ('Lakshadweep','Lakshadweep'),
  # ('Madhya Pradesh','Madhya Pradesh'),
  # ('Maharashtra','Maharashtra'),
  # ('Manipur','Manipur'),
  # ('Meghalaya','Meghalaya'),
  # ('Mizoram','Mizoram'),
  # ('Nagaland','Nagaland'),
  # ('Puducherry','Puducherry'),
  # ('Punjab','Punjab'),
  # ('Rajasthan','Rajasthan'),
  # ('Sikkim','Sikkim'),
  # ('Tamil Nadu','Tamil Nadu'),
  # ('Telangana','Telangana'),
  # ('Tripura','Tripura'),
  # ('Uttarakhand','Uttarakhand'),
  # ('Uttar Pradesh','Uttar Pradesh'),
  # ('West Bengal','West Bengal'),
)
CITY_CHOICES = (
  ('Bhubaneswar','Bhubaneswar'),
  ('Cuttack','Cuttack'),
  # ('Other','Other'),
)
# class Customer(models.Model):
#  user = models.ForeignKey(User, on_delete=models.CASCADE)
#  name = models.CharField(max_length=200)
#  locality = models.CharField(max_length=200)
#  city = models.CharField(choices=CITY_CHOICES, max_length=50)
#  zipcode = models.IntegerField()
#  state = models.CharField(choices=STATE_CHOICES, max_length=50)

#  def __str__(self):
#   # return self.user.username
#   return str(self.id)


CATEGORY_CHOICES = (
 ('G', 'GLOCERY'),
 ('S', 'SNACKS / DRINKS'),
 ('MF', 'MEALS AND FAST FOOD'),
#  ('BW', 'Bottom Wear'),
)
BRAND_CHOICES = (
 ('N', 'NON-VEG'),
 ('V', 'VEG'),
)
# class Product(models.Model):
#  title = models.CharField(max_length=100)
#  Product_quantity = models.PositiveIntegerField(default=0)
#  selling_price = models.FloatField()
#  discounted_price = models.FloatField()
#  description = models.TextField()
#  brand = models.CharField( choices=BRAND_CHOICES, max_length=100)
#  category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
#  product_image = models.ImageField(upload_to='productimg')

#  def __str__(self):
#   return str(self.id)


# class Cart(models.Model):
#  user = models.ForeignKey(User, on_delete=models.CASCADE)
#  product = models.ForeignKey(Product, on_delete=models.CASCADE)
#  quantity = models.PositiveIntegerField(default=1)

#  def __str__(self):
#   return str(self.id)
  
  # Below Property will be used by checkout.html page to show total cost in order summary
STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Not Accepted','Not Accepted'),
)

# class OrderPlaced(models.Model):
#  user = models.ForeignKey(User, on_delete=models.CASCADE)
#  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#  product = models.ForeignKey(Product, on_delete=models.CASCADE)
#  quantity = models.PositiveIntegerField(default=1)
#  ordered_date = models.DateTimeField(auto_now_add=True)
#  status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
#  locality = models.CharField(max_length=200,default='BBSR')
#  city = models.CharField(choices=CITY_CHOICES, max_length=50,default='Bhubaneswar')
#  zipcode = models.PositiveIntegerField(default=1)
#  state = models.CharField(choices=STATE_CHOICES, max_length=50,default='Odisha')


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.TextField(max_length=500, default="")


    def __str__(self):
        return self.name
# HOME PAGE MODEL--STARTING 
class Home_slider(models.Model):
    hs_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Homeslider_desc = models.TextField(max_length=100)
    Homeslider_link = models.URLField()
    Homeslider_image = models.ImageField(upload_to='Homeslider_image')

    def __str__(self):
        return self.name

class Home_recentventures(models.Model):
    hrv_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Home_recentventures_caption = models.CharField(max_length=50)
    Home_recentventures_desc = models.TextField(max_length=200)
    Home_recentventures_date = models.DateField(default=datetime.now)
    Home_recentventures_image = models.ImageField(upload_to='Homerecentventures_image')

    def __str__(self):
        return self.Home_recentventures_caption

STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Not Accepted','Not Accepted'),
)

class Home_testimonials(models.Model):
    ht_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Home_testimonials_designation = models.CharField(max_length=50)
    Home_testimonials_desc = models.TextField(max_length=210)
    Home_testimonials_date = models.DateField(default=datetime.now)
    Home_testimonials_image = models.ImageField(upload_to='Hometestimonials_image')
    verification = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Not Accepted')

    def __str__(self):
        return self.name

class Home_joinus(models.Model):
    hj_id = models.AutoField(primary_key=True)
    Home_joinus_name = models.CharField(max_length=50)
    Home_joinus_phone = models.IntegerField()
    Home_joinus_email = models.EmailField(max_length=30)
    Home_joinus_location = models.CharField(max_length=100)
    Home_joinus_desc = models.TextField(max_length=250)

    def __str__(self):
        return self.Home_joinus_name

class Home_monthlyupdate(models.Model):
    hmu_id = models.AutoField(primary_key=True)
    Home_joinus_email = models.EmailField(max_length=39)
    def __str__(self):
        return self.Home_joinus_email

# HOME PAGE MODEL--ENDING

# ABOUT PAGE MODEL--STARTING

class About_slider(models.Model):
    as_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Aboutslider_desc = models.TextField(max_length=50)
    Aboutslider_link = models.URLField()
    Aboutslider_image = models.ImageField(upload_to='Aboutslider_image')

    def __str__(self):
        return self.name

class About_volunteer(models.Model):
    av_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Aboutvolunteer_desc = models.TextField(max_length=50)
    Aboutvolunteer_link = models.URLField()
    Aboutvolunteer_image = models.ImageField(upload_to='Aboutvolunteer_image')
    volunteer_date = models.DateField()

    def __str__(self):
        return self.name

# ABOUT PAGE MODEL--ENDING

# JOINUS PAGE MODEL--STARTING
GENDER_CHOICES = (
 ('Male', 'Male'),
 ('Female', 'Female'),
 ('Transgender', 'Transgender'),
)
SOURCE_CHOICES = (
('Whatsapp', 'Whatsapp'),
 ('facebook', 'facebook'),
 ('Instagram', 'Instagram'),
 ('Twitter', 'Twitter'),
 ('youtube', 'youtube'),
 ('linkdiln', 'linkdiln'),
 ('friends', 'friends'),
 ('Other', 'Other'),
 ('Own', 'Own'),
)
PROFESSION_CHOICES = (
 ('Student', 'Student'),
 ('Job', 'Job'),
 ('Other', 'Other'),
)
class volunteer(models.Model):
 v_id = models.AutoField(primary_key=True)
 email = models.EmailField(max_length=39)
 name = models.CharField(max_length=100)
 gender = models.CharField(max_length=50,choices=GENDER_CHOICES,default='Male')
 wp_number = models.CharField(max_length=15)
 ph_number = models.CharField(max_length=15)
 blood_gp = models.CharField(max_length=10)
 Adress = models.CharField(max_length=150)
 source = models.CharField(max_length=50,choices=SOURCE_CHOICES,default='whatsapp')
 refferer = models.CharField(max_length=250, default="None")
 hg_education = models.CharField(max_length=30)
 profession = models.CharField(max_length=50,choices=PROFESSION_CHOICES,default='Student')
 org_name = models.CharField(max_length=100, default="None")
 hobbyskill = models.CharField(max_length=300, default="None")
 soc_link = models.URLField()
 past_ngo = models.CharField(max_length=100, default="None")
 query = models.TextField(max_length=100, default="None")
 birth_date = models.DateField()

 def __str__(self):
  return self.name


# JOINUS PAGE MODEL--ENDING

# DONATION PAGE MODEL--STARTING

class donation(models.Model):
 don_id = models.AutoField(primary_key=True)
 name = models.CharField(max_length=100)
 ph_number = models.CharField(max_length=15)
 email = models.EmailField(max_length=39)
 gender = models.CharField(max_length=50,choices=GENDER_CHOICES,default='Male')
 profession = models.CharField(max_length=50,choices=PROFESSION_CHOICES,default='Student')
 purpose = models.TextField(max_length=20)
 Adress = models.CharField(max_length=150)
 query = models.TextField(max_length=100)
 ammount = models.IntegerField()
 don_date = models.DateField()
 order_id = models.CharField(max_length=100)

 def __str__(self):
  return self.name

# DONATION PAGE MODEL--ENDING

# EVENT PAGE MODEL--STARTING

EVENTMODE_CHOICES = (
 ('Offline', 'Offline'),
 ('Online', 'Online'),
)
EVENTSTATUS_CHOICES = (
 ('Upcoming', 'Upcoming'),
 ('Completed', 'Completed'),
)
class event(models.Model):
 ev_id = models.AutoField(primary_key=True)
 ev_name = models.CharField(max_length=100)
 ev_desc = models.TextField(max_length=100)
 ev_about = models.TextField(max_length=500)
 ev_venue = models.CharField(max_length=100)
 ev_mode = models.CharField(max_length=50,choices=EVENTMODE_CHOICES,default='Offline')
 ev_date = models.DateField(default=now)
 ev_time = models.TimeField(default=now)
 ev_status = models.CharField(max_length=50,choices=EVENTSTATUS_CHOICES,default='Upcoming')
 ev_link = models.URLField() 


 def __str__(self):
  return self.ev_name

# EVENT PAGE MODEL--ENDING

# PROJECT PAGE MODEL--STARTING
PROJECTCAT_CHOICES = (
 ('Education', 'Education'),
 ('health & care', 'health & care'),
 ('environment', 'environment'),
 ('women empowerment', 'women empowerment'),
 ('coordination project', 'coordination project'),
 ('innovation part', 'innovation part'),
 ('Other', 'Other'),
)

class Project(models.Model):
 pr_id = models.AutoField(primary_key=True)
 pr_name = models.CharField(max_length=100)
 pr_desc = models.TextField(max_length=700)
 pr_about = models.TextField(max_length=700)
 pr_image1 = models.ImageField(upload_to='Project_image')
 pr_image2 = models.ImageField(upload_to='Project_image')
 pr_image3 = models.ImageField(upload_to='Project_image')
 pr_statisticksimg = models.ImageField(upload_to='Project_image')
 pr_date = models.DateField(default=now)
 pr_time = models.TimeField(default=now)
 pr_cat = models.CharField(max_length=50,choices=PROJECTCAT_CHOICES,default='Education')
 pr_mode = models.CharField(max_length=50,choices=EVENTMODE_CHOICES,default='Offline') 
 pr_status = models.CharField(max_length=50,choices=EVENTSTATUS_CHOICES,default='Upcoming')
 pr_link = models.URLField(default='https://sattvicsoul.org/')
 def __str__(self):
  return self.pr_name

class Project_slider(models.Model):
    ps_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Projectslider_cat = models.CharField(max_length=50,choices=PROJECTCAT_CHOICES,default='Education')
    Projectslider_desc = models.TextField(max_length=100)
    Projectslider_link = models.URLField()
    Projectslider_image = models.ImageField(upload_to='Projectslider_image')

    def __str__(self):
        return self.name

class Project_recentventures(models.Model):
    prv_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Project_recentventures_cat = models.CharField(max_length=50,choices=PROJECTCAT_CHOICES,default='Education')
    Project_recentventures_caption = models.CharField(max_length=50)
    Project_recentventures_desc = models.TextField(max_length=200)
    Project_recentventures_date = models.DateField(default=datetime.now)
    Project_recentventures_image = models.ImageField(upload_to='Projectrecentventures_image')

    def __str__(self):
        return self.name
# PROJECT PAGE MODEL--ENDING

