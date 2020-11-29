from django.urls import path

from . import views

from django.http import HttpResponse

urlpatterns = [
    path('Project1/', views.Project1, name='Project1'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('news/', views.news, name='news'),
    path('web_portal/', views.web_portal, name='web_portal'),
    path('ourtech/', views.ourtech, name='ourtech'),
    path('testing/', views.testing, name='testing'),
]

