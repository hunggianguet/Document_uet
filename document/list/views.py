from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage
# Create your views here.

students = Student.objects.all()

def display_student(request):
    global students
    students = Student.objects.all()
    query = request.GET.get("q")
    tieude = request.GET.get("tieude")
    xem = request.GET.get("xem")
    if query  :
        if tieude=="tatca":
            students = students.filter(Q(name__icontains=query)|Q(topic__icontains=query)|Q(id_student__icontains=query))

        if tieude=="hoten":
            students = students.filter(name__icontains=query)

        if tieude=="detai":
            students = students.filter(topic__icontains=query)

        if tieude=="masv":
            students = students.filter(id_student__icontains=query)

        return render(request, 'list/list.html', {'students':students})
    else:
        return render(request, 'list/searchpage.html', {'students':students})

def view(request):
    global students
    query = request.GET.get("q")
    tieude = request.GET.get("tieude")
    xem = request.GET.get("xem")
    if query:
        students = Student.objects.all()
        if tieude=="tatca":
            students = students.filter(Q(name__icontains=query)|Q(topic__icontains=query)|Q(id_student__icontains=query))

        if tieude=="hoten":
            students = students.filter(name__icontains=query)

        if tieude=="detai":
            students = students.filter(topic__icontains=query)

        if tieude=="masv":
            students = students.filter(id_student__icontains=query)

    students1 = students

    if xem=="nckh":
        students = students1.filter(topic_type="NCKH")
    if xem=="kltn":
        students = students1.filter(topic_type="KLTN")

    return render(request, 'list/list.html', {'students': students})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('view')

    else:
        form = StudentForm()
        return render(request, 'list/add_student.html', {'form' : form})

def edit_info(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = StudentForm(instance=student)

    return render(request, 'list/edit_info.html', {'form' : form})

def delete_student(request, pk):
    Student.objects.filter(id=pk).delete()

    students = Student.objects.all()

    return redirect('view')

def view_detail(request, pk):
    return render(request, 'list/upload_fl.html',{
        'students': students
    })


def upload_fl(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = StudentForm()
    return render(request, 'list/add_student.html', {
        'form': form
    })
