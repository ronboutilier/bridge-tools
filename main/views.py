from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Selection_Sets, Bridge, Element
from .forms import NotesForm, HistoryForm, InspectedForm, TripNotesForm, TripForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, TripForm
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.staticfiles.storage import staticfiles_storage
import os, math
from django.conf import settings


def trip_handler(request,trip):
	if request.user.is_authenticated:
		selection_set = Selection_Sets.objects.get(trip_name=trip).selection_set ###selection set file
		trip_name = Selection_Sets.objects.get(trip_name=trip).trip_name
		trip_summary = Selection_Sets.objects.get(trip_name=trip).trip_summary
		lead = Selection_Sets.objects.get(trip_name=trip).lead
		co = Selection_Sets.objects.get(trip_name=trip).co
		start = Selection_Sets.objects.get(trip_name=trip).start
		end = Selection_Sets.objects.get(trip_name=trip).end
		with selection_set.open('r') as f:
			selection_set = f.readlines()
		f.close()
		FHWA_bridge_list = open(os.path.join(settings.STATIC_ROOT, '_bridge_list.txt')) ##FHWA bridge list file
		FHWA_bridge_information = []
		for line in FHWA_bridge_list:
			FHWA_bridge_information.append(line)
		WSBIS_bridge_list = open(os.path.join(settings.STATIC_ROOT, '_WSBIS_bridge_list.txt')) ##WSDOT bridge list
		WSBIS_bridge_information = []
		for line in WSBIS_bridge_list:
			WSBIS_bridge_information.append(line)
		bridge_id = []
		structure_id = []
		inspected_form = []
		status = []
		initials = []
		route = []
		milepost = []
		name = []
		trip_notes = []
		trip_notes_form = []
		lattitude = []
		longitude = []	
		for s,structure_no in enumerate(selection_set):
			for WSDOT_info in WSBIS_bridge_information:
				if structure_no[0:8] in WSDOT_info:
					bridge_id.append(WSDOT_info.split('\t')[1])
					milepost.append(WSDOT_info.split('\t')[4])
					name.append(WSDOT_info.split('\t')[2])
					structure_id.append(structure_no[0:8])
					break
			for FHWA_info in FHWA_bridge_information:
				if structure_no[0:8] in FHWA_info:
					route.append(int(FHWA_info[23:26]))
					lat_deg = float(FHWA_info[129:131])
					lat_min = float(FHWA_info[131:133])/60.0
					lat_sec = float(FHWA_info[133:135])/3600.0
					lattitude.append(lat_deg+lat_min+lat_sec)
					lon_deg = float(FHWA_info[137:140])
					lon_min = float(FHWA_info[140:142])/60.0
					lon_sec = float(FHWA_info[142:144])/3600.0
					longitude.append(lon_deg+lon_min+lon_sec)


					break

			inspected_form.append(InspectedForm())
			trip_notes_form.append(TripNotesForm())

			try:
				instance = Bridge.objects.get(structure_id=structure_no[0:8])
			except:
				instance = Bridge(structure_id=structure_no[0:8])
				instance.trip_name = Selection_Sets.objects.get(trip_name=trip)
				instance.save()
			status.append(instance.inspected)
			initials.append(instance.initials)
			trip_notes.append(instance.trip_notes)


		bridge_total = len(bridge_id)
		bridge = zip(bridge_id,structure_id,inspected_form,status,initials,route,milepost,name,trip_notes_form,trip_notes,lattitude,longitude)
		return [bridge, FHWA_bridge_information, bridge_total, trip_name, trip_summary, lead, co, start, end]
	else:
		messages.error(request, "You must be logged in to view this content")
		return redirect("homepage")

def delete_trip(request, trip):
	if request.method == 'POST':
		trip = Selection_Sets.objects.get(trip_name=trip)
		trip.delete()
	return redirect("homepage")



def bridge_model(request, trip, structure_id):
	bridge = bridge_handler(request,trip,structure_id)[0]    
	spans = bridge_handler(request,trip,structure_id)[1]
	length = bridge_handler(request,trip,structure_id)[2]
	deck_width = bridge_handler(request,trip,structure_id)[3]
	notes_form = bridge_handler(request,trip,structure_id)[4]
	history_form = bridge_handler(request,trip,structure_id)[5]
	elements = bridge_handler(request,trip,structure_id)[6]
	histories = bridge_handler(request,trip,structure_id)[7]
	trip = bridge_handler(request,trip,structure_id)[8]
	structure_id = bridge_handler(request,trip,structure_id)[9]

	
	return render(request, 'main/bridge_model.html',{
		'bridge':bridge,
		'spans':spans,
		'length':length,
		'deck_width':deck_width,
		'elements':elements,
		'histories':histories,
		'trip':trip,
		'structure_id':structure_id,
		})


def inspected(request,trip,structure_id):
	if request.method == 'POST':
		instance = Bridge.objects.get(structure_id=structure_id)
		form = InspectedForm(request.POST, instance=instance)
		if form.is_valid():
			form.save(commit=False)
			instance.inspected = True
			instance.save()
		

	bridge = trip_handler(request,trip)[0]
	bridge_total = trip_handler(request,trip)[2]
	spans = 0				

	return render(request, 'main/trip.html',{
		'bridge':list(bridge),
		'spans':spans,
		'bridge_total':bridge_total,
		'trip':trip,
		})

def cover_sheet(request,trip):
	bridge = trip_handler(request,trip)[0]
	bridge_total = trip_handler(request,trip)[2]
	trip_name = trip_handler(request,trip)[3]
	trip_summary = trip_handler(request,trip)[4]
	lead = trip_handler(request,trip)[5]
	co = trip_handler(request,trip)[6]
	start = trip_handler(request,trip)[7]
	end = trip_handler(request,trip)[8]
	return render(request, 'main/includes/cover_sheet.html',{
		'bridge':list(bridge),
		'bridge_total':bridge_total,
		'trip_name':trip_name,
		'trip_summary':trip_summary,
		'lead':lead,
		'co':co,
		'start':start,
		'end':end,
		})

def checkout_check(request,trip):
	bridge = trip_handler(request,trip)[0]


def trip_notes(request,trip,structure_id):
	if request.method == 'POST':
		instance = Bridge.objects.get(structure_id=structure_id)
		form = TripNotesForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()

	bridge = trip_handler(request,trip)[0]
	bridge_total = trip_handler(request,trip)[2]
	spans = 0				

	return render(request, 'main/trip.html',{
		'bridge':list(bridge),
		'spans':spans,
		'bridge_total':bridge_total,
		'trip':trip,
		})


def bridge_handler(request,trip,structure_id):
	bridge = trip_handler(request,trip)[0]
	FHWA_bridge_information = trip_handler(request,trip)[1]
	for FHWA_info in FHWA_bridge_information:
		if structure_id in FHWA_info:
			spans = int(FHWA_info[207:210])
			length = math.ceil(0.328084*float(FHWA_info[222:228]))
			deck_width = math.ceil(0.328084*float(FHWA_info[238:242]))




	elements = []
	histories = []

	element_ids = []
	history_ids = []

	element_names = []
	history_names = []

	bridge_notes = 0
	history = 0

	notes_form = 0
	history_form = 0

	try:
		bridge_notes = Bridge.objects.get(structure_id=structure_id).element_notes
		with bridge_notes.open('r') as f:
			bridge_notes = f.readlines()
		f.close()
		for line in bridge_notes:
			if ' - ' in line:
				element_ids.append(int(line[0:4].replace('-','')))
				element_names.append(line[4::].replace('-',''))
		elements = zip(element_ids,element_names)



		try:
			history = Bridge.objects.get(structure_id=structure_id).element_history
			with history.open('r') as f:
				history = f.readlines()
			f.close()
			for line in history:
				if ' - ' in line:
					history_ids.append(int(line[0:4].replace('-','')))
					history_names.append(line[4::].replace('-',''))
			histories = zip(history_ids,history_names)

		except:
			if request.method == 'POST':
				instance = Bridge.objects.get(structure_id=structure_id)
				history_form = HistoryForm(request.POST, request.FILES, instance=instance)
				if history_form.is_valid():
					history_form.save(commit=False)
					instance.trip_name = Selection_Sets.objects.get(trip_name=trip)
					instance.save()
			else:
				history_form = HistoryForm()


	except:
		if request.method == 'POST':
			instance = Bridge.objects.get(structure_id=structure_id)
			notes_form = NotesForm(request.POST, request.FILES, instance=instance)
			if notes_form.is_valid():
				notes_form.save(commit=False)
				instance.trip_name = Selection_Sets.objects.get(trip_name=trip)
				instance.save()

		else:
			notes_form = NotesForm()

	return [bridge, spans, length, deck_width, notes_form, history_form, elements, histories, trip, structure_id, bridge_notes, history]


def bridge_space(request, trip):
	bridge = trip_handler(request,trip)[0]
	bridge_total = trip_handler(request,trip)[2]
	spans = 0

	return render(request, 'main/trip.html',{
		'bridge':list(bridge),
		'spans':spans,
		'bridge_total':bridge_total,
		'trip':trip,
		})
	
def bridge_view(request, trip, structure_id):
	bridge = bridge_handler(request,trip,structure_id)[0]    
	spans = bridge_handler(request,trip,structure_id)[1]
	length = bridge_handler(request,trip,structure_id)[2]
	deck_width = bridge_handler(request,trip,structure_id)[3]
	notes_form = bridge_handler(request,trip,structure_id)[4]
	history_form = bridge_handler(request,trip,structure_id)[5]
	elements = bridge_handler(request,trip,structure_id)[6]
	histories = bridge_handler(request,trip,structure_id)[7]
	trip = bridge_handler(request,trip,structure_id)[8]
	structure_id = bridge_handler(request,trip,structure_id)[9]

	
	return render(request, 'main/trip.html',{
		'bridge':bridge,
		'spans':spans,
		'length':length,
		'deck_width':deck_width,
		'notes_form':notes_form,
		'history_form':history_form,
		'elements':elements,
		'histories':histories,
		'trip':trip,
		'structure_id':structure_id,
		})


def element_view(request, trip, structure_id, element_id):
	bridge = bridge_handler(request,trip,structure_id)[0]
	spans = bridge_handler(request,trip,structure_id)[1]
	length = bridge_handler(request,trip,structure_id)[2]
	deck_width = bridge_handler(request,trip,structure_id)[3]
	notes_form = bridge_handler(request,trip,structure_id)[4]
	history_form = bridge_handler(request,trip,structure_id)[5]
	elements = bridge_handler(request,trip,structure_id)[6]
	histories = bridge_handler(request,trip,structure_id)[7]
	trip = bridge_handler(request,trip,structure_id)[8]
	structure_id = bridge_handler(request,trip,structure_id)[9]
	bridge_notes = bridge_handler(request,trip,structure_id)[10]
	history = bridge_handler(request,trip,structure_id)[11]
	element_notes = []
	for i,line in enumerate(bridge_notes):
		if str(element_id) in line and " - " in line:
			element_line = i
			break
	for i,line in enumerate(bridge_notes):
		if i > element_line and " - " not in line:
			element_notes.append(line)
		if i > element_line and " - " in line:
			break
	history_notes = []
	for i,line in enumerate(history):
		if str(element_id) in line and " - " in line:
			element_line = i
			break
	for i,line in enumerate(history):
		if i > element_line and " - " not in line:
			history_notes.append(line)
		if i > element_line and " - " in line:
			break


	return render(request, 'main/trip.html',{
		'bridge':bridge,
		'spans':spans,
		'length':length,
		'deck_width':deck_width,
		'notes_form':notes_form,
		'history_form':history_form,
		'elements':elements,
		'histories':histories,
		'trip':trip,
		'structure_id':structure_id,
		'element_id':element_id,
		'element_notes':element_notes,
		'history_notes':history_notes,
		})


def homepage(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = TripForm(request.POST, request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.inspector = request.user
				instance.save()
				return redirect('homepage')
		else:
			form = TripForm()
		return render(request, 'main/trips.html',{
			'form':form,
			'trips': Selection_Sets.objects.filter(inspector=request.user)
			})
	else:
		return render(request, 'main/trips.html')


def getting_started(request):
    return render(request, 'main/getting_started.html')




def bridge_mechanics(request):
	return render(request, 'main/bridge_mechanics.html')

def truss_analysis(request):
        return render(request, 'main/includes/truss_analysis.html')

def reinforced_concrete(request):
        return render(request, 'main/includes/reinforced_concrete.html')

def prestressed_concrete(request):
        return render(request, 'main/includes/prestressed_concrete.html')



def ubit_videos(request):
	return render(request, 'main/ubit_tutorials.html')


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")


	form = NewUserForm
	return render(request,
		"main/register.html",
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
				  "main/login.html",
				  {"form":form})


