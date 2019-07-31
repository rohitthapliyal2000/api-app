from django.db import models

class Bank(models.Model):
	ifsc = models.CharField(max_length=20)
	bank_id = models.IntegerField()
	branch = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	bank_name = models.CharField(max_length=100)
