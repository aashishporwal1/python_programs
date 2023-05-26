from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=100,blank=True)
	content=models.CharField(max_length=100,blank=True)
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title