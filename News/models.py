from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
	#creating the models 
	author = models.ForeignKey('auth.User')
	topic = models.CharField(max_length=300)
	article = models.TextField()
	created_date = models.DateTimeField(default= timezone.now)
	
	image = models.ImageField(upload_to='img/%y/%m/%d',blank=True)



	def Meta():
		ordering = '-pk'
	def __str__(self):
		return self.topic


