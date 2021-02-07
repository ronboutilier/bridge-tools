from django import forms
from .models import Selection_Sets, Bridge, Element
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class TripForm(forms.ModelForm):
    class Meta:
        model = Selection_Sets
        fields = ('trip_name','trip_summary','selection_set')

class InspectedForm(forms.ModelForm):
    class Meta:
        model = Bridge
        fields = ('initials',)

class TripNotesForm(forms.ModelForm):
    class Meta:
        model = Bridge
        fields = ('trip_notes',)

class NotesForm(forms.ModelForm):
    class Meta:
        model = Bridge
        fields = ('element_notes',)

class HistoryForm(forms.ModelForm):
    class Meta:
        model = Bridge
        fields = ('element_history',)
