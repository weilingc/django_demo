from django.conf.urls import include
from django.contrib import admin
# from django.contrib.auth.views import LoginView, LogoutView #CBV
from django.urls import path

from . import views

urlpatterns = [
    path('', include('allauth.urls')), #重新導向參考 https://stackoverflow.com/questions/20138049/redirect-user-to-another-url-with-django-allauth-log-in-signal
    # path('login/', views.login, name='login-url'),
    # path('logout/', views.logout, name='logout-url'),
    # path('signup/', views.signup, name='signup-url'),
]
