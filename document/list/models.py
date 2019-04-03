from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    id_student= models.IntegerField(null=True)
    name = models.CharField(max_length=300, null=True)
    birth_date = models.DateField(null=True)
    academic_year = models.CharField(max_length=300, null=True)
    topic = models.CharField(max_length=100, null=True)
    TOPIC_TYPE = (
                ('KLTN','Khóa luận tốt nghiệp'),
                ('NCKH','Nghiên cứu khoa học')
    )
    topic_type=models.CharField(max_length=4,null=True,choices=TOPIC_TYPE)
    tutor = models.CharField(max_length=300, null=True)
    reviewer = models.CharField(max_length=300, null=True)
    work_unit = models.CharField(max_length=300, null=True)
    file = models.FileField(upload_to='media')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name == None:
            return " NAME IS NULL"
        return self.name
