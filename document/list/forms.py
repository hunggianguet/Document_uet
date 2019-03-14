from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
        class Meta:
            model = Document
            fields = ('id', 'name', 'last_name', 'birth_date', 'grade', 'topic', 'tutor', 'reviewer')
