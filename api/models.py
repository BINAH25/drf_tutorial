from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Advocate(models.Model):
    company = models.ForeignKey(Company,on_delete = models.SET_NULL,blank=True,null=True)
    username = models.CharField(max_length=200)
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.username

