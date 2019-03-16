from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *
# Create your views here.

def display_student(request):
        students = Student.objects.all()
        key_word=''

        if 'search' in request.GET:
            key_word = request.GET['search']
            students = students.filter(Q(name__icontains=key_word)|Q(birth_date__icontains=key_word)|Q(topic__icontains=key_word)|Q(grade__icontains=key_word)|Q(tutor__icontains=key_word)|Q(reviewer__icontains=key_word))

        context = {
            'students': students,
            'key_word': key_word
            }
        return render(request, 'list/list.html', context)

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_student')

    else:
        form = StudentForm()
        return render(request, 'list/add_student.html', {'form' : form})

def edit_info(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('display_student')
    else:
        form = StudentForm(instance=student)

        return render(request, 'list/edit_info.html', {'form' : form})

def delete_student(request, pk):
    Student.objects.filter(id=pk).delete()

    students = Student.objects.all()

    return redirect('display_student')
