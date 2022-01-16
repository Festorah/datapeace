from django.db import models


class Profile(models.Model):
	first_name = models.CharField(max_length=50, blank=True)
	last_name = models.CharField(max_length=50, blank=True)
	company_name = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=50, blank=True)
	state = models.CharField(max_length=50, blank=True)
	zip = models.IntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	web = models.CharField(max_length=200, blank=True)
	age = models.IntegerField(blank=True, null=True)



	def __str__(self):
		return f"{self.first_name} Profile"