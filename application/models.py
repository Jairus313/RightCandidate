from django.db import models

# Create your models here.

class Candidate(models.Model):
    fname =  models.CharField(max_length=100)
    phone =  models.IntegerField()
    email =  models.CharField(max_length=100) 
    skills =  models.CharField(max_length=500)

    def __str__(self):
        return self.fname
