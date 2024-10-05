from django.db import models

# Create your models here.

class Contatc(models.Model):
    name=models.CharField(max_length=225)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True )


