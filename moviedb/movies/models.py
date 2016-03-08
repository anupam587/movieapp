from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=150,blank=False,null=False)

	def __unicode__(self):
		return self.name

class Director(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200,blank=False,null=False)

	def __unicode__(self):
		return self.name

class Actor(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200,blank=False,null=False)
	gender_choices = (
		('M', 'Male'),
		('F', 'Female')
	)
	gender = models.CharField(max_length=1,choices=gender_choices)

	def __unicode__(self):
		return self.name

class Movie(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200,blank=False,null=False)
	release_date = models.DateField(blank=False,null=False)
	categories = models.ManyToManyField(Category,blank=False)
	director = models.ForeignKey(Director,on_delete=models.CASCADE)
	casts = models.ManyToManyField(Actor,blank=False)
	description = models.CharField(max_length=2000,blank=True,null=False)
	ratings = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
	trailerimg = models.ImageField(upload_to='movie_img',blank=False,null=False)


	def __unicode__(self):
		return self.title


