from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.staticfiles.storage import staticfiles_storage
import os, math
from django.conf import settings

def homepage(request):
        return render(request, 'main/steamroller_homepage.html')

