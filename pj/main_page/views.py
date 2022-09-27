from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
import requests
from django.contrib.auth.models import User, Group
from .models import Disciplines, DisciplinesActual, DisciplineHomeWork
# from django import forms
# from .forms import *

def main_home(request):
    return render(request, 'main_page/main_page.html')

def disciplines(request):
    return render(request, 'main_page/disciplines.html')

def discipline_page(request, discipline):
    discipline_db = Disciplines.objects.get(eng_discipline=discipline)
    homework_db = DisciplineHomeWork.objects.filter(eng_discipline=discipline)
    if not homework_db:
        homework_db = DisciplineHomeWork.objects.filter(eng_discipline='test')
    return render(request, 'main_page/discipline_page.html', {"discipline":discipline_db,"homework":homework_db})

def files(request):
    homework_db = DisciplineHomeWork.objects.all()
    return render(request, 'main_page/files.html', {"homework":homework_db})

def upload_homework(request):
    discipline_db = Disciplines.objects.all()
    return render(request, 'main_page/upload_homework.html', {"discipline":discipline_db})
