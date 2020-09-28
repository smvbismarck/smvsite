from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('dsgvo', views.dsgvo, name='dsgvo'),
    path('impressum', views.impressum, name='impressum')
]
