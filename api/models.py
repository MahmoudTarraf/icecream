from django.db import models
from datetime import datetime,date

class Note(models.Model):
    body= models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    
    def __str__(self) :
        return self.body[0:50]
    class Meta:
        ordering=['-updated']