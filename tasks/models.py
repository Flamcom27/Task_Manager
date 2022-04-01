from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=300)
    date = models.DateField(auto_now_add=True) 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    done = models.BooleanField(default=False) 

    def __str__(self):
        return self.title