from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="todo_item")
    complete = models.CharField(max_length=300, default='not complete')
