from django.db import models

# Create your models here. 

class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     content = models.TextField()

# class User()

# # class TodoItem(models.Model):
#     content = models.TextField()



