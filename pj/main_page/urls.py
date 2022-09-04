from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_page'),
    path('disciplines/', views.disciplines, name='disciplines'),
]
