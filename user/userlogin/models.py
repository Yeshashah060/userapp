from django.db import models

# Create your models here.

class usermodel(models.Model):
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=40)
	emailid = models.EmailField(max_length=140)
	contactno = models.IntegerField()

	def __str__(self):
		return self.username