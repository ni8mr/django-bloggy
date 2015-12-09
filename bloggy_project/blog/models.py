from django.db import models

# Create your models here.

class Post(models.Model):
	# primary_key id (uuid) needs not to be defined
	created_at = models.DateTimeField(auto_now_add = True)
	# created_at will be created automatically but the
	# following are need to be added explicitly 
	title = models.CharField(max_length=100)
	content = models.TextField()


