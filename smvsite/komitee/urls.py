from django.urls import path

from . import views

urlpatterns = [
    path('<str:article_name>', views.blogEntry, name='komitee'),
]
