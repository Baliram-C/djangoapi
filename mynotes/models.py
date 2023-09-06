from django.db import models

# Create your models here.
class Mynotes(models.Model):
	name = models.CharField(max_length=200)
	language = models.CharField(max_length=100)
	price = models.CharField(max_length=10)

### for changing the name 
	def __str__(self):
		return self.name
