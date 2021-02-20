from django.db import models
from datetime import datetime, date, time, timedelta
from django.contrib.auth.models import User
from django.utils import timezone


class Workout(models.Model):
	workout_id = models.AutoField(primary_key=True)
	health_date = models.CharField(default='workout_'+datetime.strftime(datetime.now(), '%Y_%m_%d'), max_length=100)
	Lifter = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	health_date = models.CharField(default='health_'+datetime.strftime(datetime.now(), '%Y_%m_%d'), max_length=100)
	primary_lift_date = models.CharField(default='primary_lift_'+datetime.strftime(datetime.now(), '%Y_%m_%d'), max_length=100)
	assistance_lift_1_date = models. CharField(default='assistance_lift_1_'+datetime.strftime(datetime.now(), '%Y_%m_%d'), max_length=100)
	assistance_lift_2_date = models. CharField(default='assistance_lift_2_'+datetime.strftime(datetime.now(), '%Y_%m_%d'), max_length=100)
	accessory_lift_1_date = models. CharField(default='accessory_lift_1_'+datetime.strftime(datetime.now(), '%Y_%m_%d'), max_length=100)
	accessory_ift_2_date = models. CharField(default='accessory_lift_2_'+datetime.strftime(datetime.now(), '%Y_%m_%d'), max_length=100)

	class Meta:
		verbose_name_plural = "Workouts"

	def __str__(self):
		return self.workout_id

class Health(models.Model):
	health_date = models.ForeignKey(Workout, on_delete=models.CASCADE, default=1, verbose_name="Workout")
	morning_weight = models.CharField(max_length=10)
	morning_waist = models.CharField(max_length=10)
	hrv = models.CharField(max_length=10)
	readiness = models.CharField(max_length=10)
	sleep = models.CharField(max_length=10)
	calories = models.CharField(max_length=10)
	mood_night = models.CharField(max_length=10)
	water_night = models.CharField(max_length=10)

	class Meta:
		verbose_name_plural = "Metrics"

	def __str__(self):
		return self.health_date


class Primary_Lift(models.Model):
	primary_lift_date = models.ForeignKey(Workout, on_delete=models.CASCADE, default=1, verbose_name="Workouts")
	primary_exercise = models.CharField(max_length=10)
	primary_equipment = models.ImageField(upload_to='equipment/')
	primary_weight = models.CharField(max_length=10)
	primary_reps = models.CharField(max_length=10)
	primary_rest = models.CharField(max_length=10)
	primary_difficulty = models.CharField(max_length=10)
	primary_notes = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Primary_Lifts"

	def __str__(self):
		return self.primary_lift_date

class Assistance_Lift_1(models.Model):
	assistance_1_lift_date = models.ForeignKey(Workout, on_delete=models.CASCADE, default=1, verbose_name="Workouts")
	assistance_exercise_1 = models.CharField(max_length=10)
	assistance_equipment_1 = models.ImageField(upload_to='equipment/')
	assistance_weight_1_set_1 = models.CharField(max_length=10)
	assistance_reps_1_set_1 = models.CharField(max_length=10)
	assistance_weight_1_set_2 = models.CharField(max_length=10)
	assistance_reps_1_set_2 = models.CharField(max_length=10)
	assistance_weight_1_set_3 = models.CharField(max_length=10)
	assistance_reps_1_set_3 = models.CharField(max_length=10)
	assistance_1_rest = models.CharField(max_length=10)
	assistance_1_difficulty = models.CharField(max_length=10)
	assistance_1_notes = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Assistance_1_Lifts"

	def __str__(self):
		return self.assistance_1_lift_date

class Assistance_Lift_2(models.Model):
	assistance_2_lift_date = models.ForeignKey(Workout, on_delete=models.CASCADE, default=1, verbose_name="Workouts")
	assistance_exercise_2 = models.CharField(max_length=10)
	assistance_equipment_2 = models.ImageField(upload_to='equipment/')
	assistance_weight_2_set_1 = models.CharField(max_length=10)
	assistance_reps_2_set_1 = models.CharField(max_length=10)
	assistance_weight_2_set_2 = models.CharField(max_length=10)
	assistance_reps_2_set_2 = models.CharField(max_length=10)
	assistance_weight_2_set_3 = models.CharField(max_length=10)
	assistance_reps_2_set_3 = models.CharField(max_length=10)
	assistance_2_rest = models.CharField(max_length=10)
	assistance_2_difficulty = models.CharField(max_length=10)
	assistance_2_notes = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Assistance_2_Lifts"

	def __str__(self):
		return self.assistance_2_lift_date


class Accessory_Lift_1(models.Model):
	accessory_1_lift_date = models.ForeignKey(Workout, on_delete=models.CASCADE, default=1, verbose_name="Workouts")
	accessory_exercise_1 = models.CharField(max_length=10)
	accessory_equipment_1 = models.ImageField(upload_to='equipment/')
	accessory_weight_1_set_1 = models.CharField(max_length=10)
	accessory_reps_1_set_1 = models.CharField(max_length=10)
	accessory_weight_1_set_2 = models.CharField(max_length=10)
	accessory_reps_1_set_2 = models.CharField(max_length=10)
	accessory_weight_1_set_3 = models.CharField(max_length=10)
	accessory_reps_1_set_3 = models.CharField(max_length=10)
	accessory_1_rest = models.CharField(max_length=10)
	accessory_1_difficulty = models.CharField(max_length=10)
	accessory_1_notes = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Accessory_1_Lifts"

	def __str__(self):
		return self.accessory_1_lift_date

class Accessory_Lift_2(models.Model):
	accessory_2_lift_date = models.ForeignKey(Workout, on_delete=models.CASCADE, default=1, verbose_name="Workouts")
	accessory_exercise_2 = models.CharField(max_length=10)
	accessory_equipment_2 = models.ImageField(upload_to='equipment/')
	accessory_weight_2_set_1 = models.CharField(max_length=10)
	accessory_reps_2_set_1 = models.CharField(max_length=10)
	accessory_weight_2_set_2 = models.CharField(max_length=10)
	accessory_reps_2_set_2 = models.CharField(max_length=10)
	accessory_weight_2_set_3 = models.CharField(max_length=10)
	accessory_reps_2_set_3 = models.CharField(max_length=10)
	accessory_2_rest = models.CharField(max_length=10)
	accessory_2_difficulty = models.CharField(max_length=10)
	accessory_2_notes = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Accessory_2_Lifts"

	def __str__(self):
		return self.accessory_2_lift_date



class Exercises(models.Model):
	exercise_name = models.CharField(max_length=100)
	exercise_type = models.CharField(max_length=100, default="accessory")
	movement_type = models.CharField(max_length=100, default="none")
	exercise_PR_increment = models.CharField(max_length=100)
	recovery = models.CharField(max_length=100, default="1")

	class Meta:
		verbose_name_plural = "Exercises"

	def __str__(self):
		return self.exercise_name

