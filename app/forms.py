from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms.widgets import Select
from django.utils.translation import gettext, gettext_lazy as _
from .models import volunteer
from django.contrib.auth import password_validation

# class CustomerRegistrationForm(UserCreationForm):
#  password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#  password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#  email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
#  class Meta:
#   model = User
#   fields = ['username', 'email', 'password1', 'password2']
#   labels = {'email': 'Email'}
#   widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

# class LoginForm(AuthenticationForm):
#  username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
#  password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

# class MyPasswordChangeForm(PasswordChangeForm):
#  old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True,  'class':'form-control'}))
#  new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
#  new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))

# class MyPasswordResetForm(PasswordResetForm):
#  email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))

# class MySetPasswordForm(SetPasswordForm):
#  new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
#  new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))

# class CustomerProfileForm(forms.ModelForm):
#   class Meta:
#     model = Customer
#     fields = ['name', 'locality', 'city', 'state', 'zipcode']
#     widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}), 'city':forms.Select(attrs={'class':'form-control'}), 
#     'state':forms.Select(attrs={'class':'form-control'}),
#     'zipcode':forms.NumberInput(attrs={'class':'form-control'})}

# class JoinUsForm(forms.ModelForm):
    
#     class Meta:
#         model = volunteer
#         fields = ['email', 'name', 'gender', 'whatsappnumber', 'phonenumber', 'bloodgroup', 'adress', 'source', 'refferer', 'education', 'profession', 'orgname', 'hobby', 'sociallink', 'pastngo', 'query', 'birthdate']
#         labels = {'email': 'Email'}
#         widgets = {'email':forms.EmailInput(attrs={'class':'form-control'}),
#                    'name':forms.TextInput(attrs={'class':'form-control'}),
#                    'gender':forms.Select(attrs={'class':'form-control'}),
#                    'whatsappnumber':forms.TextInput(attrs={'class':'form-control'}),
#                    'phonenumber  ':forms.TextInput(attrs={'class':'form-control'}),
#                    'bloodgroup':forms.Select(attrs={'class':'form-control'}),
#                    'adress':forms.TextInput(attrs={'class':'form-control'}),
#                    'source':forms.Select(attrs={'class':'form-control'}),
#                    'refferer':forms.TextInput(attrs={'class':'form-control'}),
#                    'education':forms.TextInput(attrs={'class':'form-control'}),
#                    'profession':forms.Select(attrs={'class':'form-control'}),
#                    'orgname':forms.TextInput(attrs={'class':'form-control'}),
#                    'hobby':forms.TextInput(attrs={'class':'form-control'}),
#                    'sociallink':forms.TextInput(attrs={'class':'form-control'}),
#                    'pastngo':forms.TextInput(attrs={'class':'form-control'}),
#                    'query':forms.TextInput(attrs={'class':'form-control'}),
#                    'birthdate':forms.DateInput(attrs={'class':'form-control'}),}

