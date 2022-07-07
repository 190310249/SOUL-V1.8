from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('support/', views.support_us, name='support'),
    path('join_us/', views.join_us, name='join_us'),
    path('projects/', views.projects, name='projects'),
    path('projectswemp/', views.projectswemp, name='projectswemp'),
    path('projectsinnov/', views.projectsinnov, name='projectsinnov'),
    path('projectshc/', views.projectshc, name='projectshc'),
    path('projectsenv/', views.projectsenv, name='projectsenv'),
    path('projectsed/', views.projectsed, name='projectsed'),
    path('projectscorpo/', views.projectscorpo, name='projectscorpo'),
    path('projectsany/', views.projectsany, name='projectsany'),
    # path('', views.ProductView.as_view(), name="home"),
    # path('product-detail', views.product_detail, name='product-detail'),
    # path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    # path('paymentdone/', views.payment_done, name='paymentdone'),
    # path('contact', views.contact, name='contact'),


    # path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    # path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),    
    # path("password-reset/", auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    # path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name="password_reset_done"),
    # path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),
    # path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name="password_reset_complete"),
    # path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
