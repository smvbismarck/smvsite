from django.urls import path

from . import views

urlpatterns = [
    path('<int:article_id>', views.blogEntry, name='article'),
]
