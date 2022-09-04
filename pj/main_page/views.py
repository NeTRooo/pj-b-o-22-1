from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
import requests
from django.contrib.auth.models import User, Group
# from .models import BuyStatus, PrimeStatus
# from django import forms
# from .forms import *


def main_home(request):
    return render(request, 'main_page/main_page.html')
def disciplines(request):
    return render(request, 'main_page/disciplines.html')