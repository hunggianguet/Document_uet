from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.utils.timezone import now
# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    id_student= models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True) # họ và tên đệm
    last_name = models.CharField(max_length=50, null=True)
    birth = models.CharField(max_length=25, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True)
    academic_year = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    TOPIC_TYPE = (
                ('KLTN','Khóa luận tốt nghiệp'),
                ('NCKH','Nghiên cứu khoa học')
    )
    topic_type=models.CharField(max_length=255,null=True, blank=True,choices=TOPIC_TYPE)
    tutor = models.CharField(max_length=255, null=True, blank=True)
    reviewer = models.CharField(max_length=255, null=True, blank=True)
    work_unit = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='media', null=True, blank=True)
    upload_date = models.DateTimeField(default=now, auto_now_add=False)
    summary = models.TextField(null=True, blank=True)

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.name, self.last_name)


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None