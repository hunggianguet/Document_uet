from django import forms
from .models import *

class StudentForm(forms.ModelForm):
        class Meta:
            model = Student
            labels = {
                "id":"Stt",
                "id_student":"Mã sinh viên",
                "name":"Họ và Tên đệm",
                "last_name":"Tên",
                "birth":"Ngày sinh",
                "academic_year":"Lớp",
                "topic":"Đề tài",
                "summary":"Tóm tắt đề tài",
                "topic_type":"Loại đề tài",
                "tutor":"Cán bộ hướng dẫn",
                "year": "Năm bảo vệ",
                "file":"Tài liệu"
            }
            fields = ('id', 'id_student', 'name', 'last_name', 'birth', 'academic_year', 'topic','summary','topic_type', 'tutor','year','file')

