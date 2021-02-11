from django.db import models
import datetime
from django.contrib.auth.models import User

class Selection_Sets(models.Model):
	trip_name = models.CharField(max_length=200)
	selection_set = models.FileField(upload_to='selection_sets/')
	trip_summary = models.CharField(max_length=200)	
	inspector = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	lead = models.CharField(max_length=3,default="xxx")
	co = models.CharField(max_length=3,default = "xxx")
	start = models.DateField(default=datetime.date.today)
	end = models.DateField(default=datetime.date.today) 


	class Meta:
		verbose_name_plural = "Sets"

	def delete(self, *args, **kwargs):
		self.selection_set.delete()	
		super().delete(*args, **kwargs)

	def __str__(self):
		return self.trip_name



class Bridge(models.Model):
	structure_id = models.CharField(max_length=200)
	inspected = models.BooleanField(default=False)
	initials = models.CharField(max_length=3)
	trip_notes = models.CharField(max_length=200, default='enter details here')
	element_notes = models.FileField(upload_to='notes/')
	element_history = models.FileField(upload_to='history/',blank=False,null=True)
	trip_name = models.ForeignKey(Selection_Sets, on_delete=models.CASCADE, default=1, verbose_name="Set")

	class Meta:
		verbose_name_plural = "Bridge"

	def __str__(self):
		return self.structure_id

class Element(models.Model):   ###multiple files
	photo_id = models.CharField(max_length=200)
	photos = models.ImageField(upload_to='photos/')
	structure_id = models.ForeignKey(Bridge, on_delete=models.CASCADE, default=1, verbose_name="Bridge")

	def __str__(self):
		return self.photo_id

	class Meta:
		verbose_name_plural = "Element"

