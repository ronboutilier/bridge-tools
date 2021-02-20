from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Exercises
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.staticfiles.storage import staticfiles_storage
import os, math
from django.conf import settings

def homepage(request):
	return render(request, 'main/homepage.html')

def health_metrics(request):
	if request.method == 'POST':
		instance = Exercises.objects.get(health_date=health_date)
		form = HealthForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
	return render(request, 'main/health_metrics.html')











def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")


	form = NewUserForm
	return render(request,
		"main/ronboutilier_register.html",
		context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")


	form = AuthenticationForm()
	return render(request,
				  "main/ronboutilier_login.html",
				  {"form":form})
