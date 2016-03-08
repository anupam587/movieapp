from django.contrib import admin

# Register your models here.
from .models import Movie
from .models import Category
from .models import Director
from .models import Actor


class MovieAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "title", "release_date"]
	class Meta:
		model = Movie

class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "name"]
	class Meta:
		model = Category

class DirectorAdmin(admin.ModelAdmin):
	list_display = ["__unicode__" , "name"]
	class Meta:
		model = Director

class ActorAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "name", "gender"]
	class Meta:
		model = Actor


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
