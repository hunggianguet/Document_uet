from django import forms
from .models import *

class StudentForm(forms.ModelForm):
        class Meta:
            model = Student
            fields = ('id', 'id_student', 'name', 'birth_date', 'academic_year', 'topic', 'tutor', 'reviewer', 'work_unit')
