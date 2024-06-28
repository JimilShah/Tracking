from django.contrib import admin
from django.urls import path
from Bloodbank import views
import Bloodbank
urlpatterns = [
    path("",views.index,name='Bloodbank'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact_view,name='contact')
] 