from django import forms
from .models import Workout, Health, Primary_Lift, Assistance_Lift_1, Assistance_Lift_2, Accessory_Lift_1, Accessory_Lift_2
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

class HealthForm(forms.ModelForm):
	class Meta:
		model = Health
		fields = ('morning_weight','morning_waist','hrv','readiness','sleep','calories','mood_night','water_night')

class PrimaryLiftForm(forms.ModelForm):
	class Meta:
		model = Primary_Lift
		fields = ('primary_exercise','primary_equipment','primary_weight','primary_reps','primary_rest','primary_difficulty','primary_notes')

class AssistanceLift1Form(forms.ModelForm):
	class Meta:
		model = Assistance_Lift_1
		fields = ('assistance_exercise_1','assistance_equipment_1','assistance_weight_1_set_1','assistance_reps_1_set_1',
			'assistance_weight_1_set_2','assistance_reps_1_set_2','assistance_weight_1_set_3','assistance_reps_1_set_3',
			'assistance_1_rest','assistance_1_difficulty','assistance_1_notes')

class AssistanceLift2Form(forms.ModelForm):
	class Meta:
		model = Assistance_Lift_2
		fields = ('assistance_exercise_2','assistance_equipment_2','assistance_weight_2_set_1','assistance_reps_2_set_1',
			'assistance_weight_2_set_2','assistance_reps_2_set_2','assistance_weight_2_set_3','assistance_reps_2_set_3',
			'assistance_2_rest','assistance_2_difficulty','assistance_2_notes')

class AccessoryLift1Form(forms.ModelForm):
	class Meta:
		model = Accessory_Lift_1
		fields = ('accessory_exercise_1','accessory_equipment_1','accessory_weight_1_set_1','accessory_reps_1_set_1',
			'accessory_weight_1_set_2','accessory_reps_1_set_2','accessory_weight_1_set_3','accessory_reps_1_set_3',
			'accessory_1_rest','accessory_1_difficulty','accessory_1_notes')

class AccessoryLift2Form(forms.ModelForm):
	class Meta:
		model = Accessory_Lift_2
		fields = ('accessory_exercise_2','accessory_equipment_2','accessory_weight_2_set_1','accessory_reps_2_set_1',
			'accessory_weight_2_set_2','accessory_reps_2_set_2','accessory_weight_2_set_3','accessory_reps_2_set_3',
			'accessory_2_rest','accessory_2_difficulty','accessory_2_notes')







