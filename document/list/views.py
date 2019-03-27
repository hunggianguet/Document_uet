from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *
from django.core.files.storage import FileSystemStorage
# Create your views here.

def display_student(request):
    query = request.GET.get("q")
    students = Student.objects.all()
    if query  :
        students = Student.objects.filter(Q(id_student__icontains=query)|Q(topic__icontains=query)|Q(name__icontains=query))
    return render(request, 'list/list.html', {'students':students})

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

def view_detail(request, pk):
    return render(request, 'list/upload_fl.html',{
        'students': students
    })


def upload_fl(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_student')
    else:
        form = StudentForm()
    return render(request, 'list/add_student.html', {
        'form': form
    })
