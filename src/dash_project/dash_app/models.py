from django.db import models

class Company(models.Model):
	name = models.CharField(max_length=120)
	net_worth = models.IntegerField()

	def __str__(self):
		return self.name