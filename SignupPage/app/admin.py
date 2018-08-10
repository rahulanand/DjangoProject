from django.contrib import admin
from . models import Person
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'timestamp', 'gender']
	#list_display_links = ["updated"]
	list_filter = ["first_name"]
	class Meta:
		model = Person
admin.site.register(Person, PostModelAdmin)
