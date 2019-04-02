from django import forms
from .models import *

class StudentForm(forms.ModelForm):
        class Meta:
            model = Student
            labels = {
                "id":"Stt",
                "id_student":"Mã sinh viên",
                "name":"Họ tên",
                "birth_date":"Ngày sinh",
                "academic_year":"Lớp",
                "topic":"Đề tài",
                "tutor":"Cán bộ hướng dẫn",
                "file":"Tài liệu"
            }
            fields = ('id', 'id_student', 'name', 'birth_date', 'academic_year', 'topic','topic_type', 'tutor','file')


class PdfForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('file','name')
