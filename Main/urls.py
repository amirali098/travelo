from django.urls import path

from . import views

app_name = "Main"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),


]

