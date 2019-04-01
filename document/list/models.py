from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    id_student= models.IntegerField(null=True)
    name = models.CharField(max_length=30, null=True)
    birth_date = models.DateField(null=True)
    academic_year = models.CharField(max_length=30, null=True)
    topic = models.CharField(max_length=100, null=True)
    tutor = models.CharField(max_length=30, null=True)
    reviewer = models.CharField(max_length=30, null=True)
    work_unit = models.CharField(max_length=30, null=True)
    file = models.FileField(upload_to='media')
    kltn = models.BooleanField(null=True)
    nckh = models.BooleanField(null=True)
