from django.db import models

class Owner(models.Model):
	name = models.CharField(max_length=100)
	num_memes = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Meme(models.Model):
	owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
	caption = models.CharField(max_length=100)
	url = models.URLField(max_length=300)
	timestamp = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.caption