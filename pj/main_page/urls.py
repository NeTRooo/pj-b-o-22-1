from django.db import router
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_page'),
    re_path('^disciplines/(?P<discipline>.+)/$', views.discipline_page, name='discipline_page'),
    path('upload/', views.upload_homework, name='upload_homework'),
    path('disciplines/', views.disciplines, name='disciplines'),
    path('files/', views.files, name='files'),
]