from django.db import models
from datetime import datetime

#create your model here
class blog_post (models.Model):
    date = models.DateTimeField(default=datetime.now, blank= True)
    name = models.CharField(max_length=500)
    num = models.TextField()
    email = models.EmailField(max_length=400)
    message= models.TextField()

