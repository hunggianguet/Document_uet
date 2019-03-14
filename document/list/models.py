from django.db import models

# Create your models here.
class Document(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=30, null=True)
    last_name= models.CharField(max_length=30, null=True)
    birth_date = models.DateField(null=True,blank=True)
    grade = models.CharField(max_length=30, null=True)
    topic = models.CharField(max_length=100, null=True)
    tutor = models.CharField(max_length=30, null=True)
    reviewer = models.CharField(max_length=30, null=True)
