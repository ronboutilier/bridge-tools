from django.contrib import admin
from .models import Selection_Sets, Bridge, Element
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
#class ElementAdmin(admin.ModelAdmin):
#	fieldsets = [
#    	("ID/Date", {"fields": ["element_number", "element_published"]}),
#    	("URL", {"fields":["element_slug"]}),
#    	("Bridge", {"fields":["bridge_id"]}),
#    	("Notes", {"fields":["element_notes"]}),
#	]

#	formfield_overrides = {
#		models.TextField: {'widget': TinyMCE()}
#	}

#admin.site.register(Bridge)
#admin.site.register(Trip)
#admin.site.register(Element, ElementAdmin)


