from django.db import models

# Create your models here.

class Record(models.Model):
    desc=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)