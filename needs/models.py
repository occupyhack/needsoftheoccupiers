from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length=255)

class State(models.Model):
	country = models.ForeignKey(Country)
	name = models.CharField(max_length=150)
	abbreviation = models.CharField(max_length=4)

class City(models.Model):
	state = models.ForeignKey(State)
	name = models.CharField(max_length=150)

class Organization(models.Model):
	city = models.ForeignKey(City)
	name = models.CharField(max_length=150)
	description = models.TextField()

class Need(models.Model):
	description = models.TextField()
	user = models.ForeignKey(User)
	organization = models.ForeignKey(Organization)
	city = models.ForeignKey(City)
	address = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	needed_by = models.DateField()
	priority = models.BooleanField()

class Item(models.Model):
	name = models.CharField(max_length=255)
	url = models.CharField(max_length=255)

class NeedItem(models.Model):
	STATUS_CHOICES = (
		('UF', 'Unfullfilled'),
		('PN', 'Pending'),
		('FU', 'Fullfilled'),
	)
	need = models.ForeignKey(Need)
	item = models.ForeignKey(Item)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES)
	user = models.ForeignKey(User)
	fulfillment_date = models.DateField()
	loan = models.BooleanField()
