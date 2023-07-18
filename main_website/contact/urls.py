from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
                  path('', views.home, name='home'),
                  path('about', views.about, name='about'),
                  path('contact-us', views.contact, name='contact-us'),
                  path('services', views.services, name='services'),
                  path('team', views.team, name='team'),

              ]
