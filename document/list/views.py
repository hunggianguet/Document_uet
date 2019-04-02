from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage
# Create your views here.

def display_student(request):
    query = request.GET.get("q")
    students = Student.objects.all()
    tieude=request.GET.get("tieude")

    if query  :
        if tieude=="hoten":
            students = Student.objects.filter(name__icontains=query)
            paginator = Paginator(students, 20)  # Show 20 students per page
            page = request.GET.get('page')
            students = paginator.get_page(page)
        if tieude=="detai":
            students = Student.objects.filter(topic__icontains=query)
            paginator = Paginator(students, 20)  # Show 20 students per page
            page = request.GET.get('page')
            students = paginator.get_page(page)
        if tieude=="masv":
            students = Student.objects.filter(id_student__icontains=query)
            paginator = Paginator(students, 20)  # Show 20 students per page
            page = request.GET.get('page')
            students = paginator.get_page(page)
        return render(request, 'list/list.html', {'students':students})
    else:
        return render(request, 'list/searchpage.html', {'students':students})

def view(request):
    query = request.GET.get("q")
    students = Student.objects.all()
    tieude = request.GET.get("tieude")
    paginator = Paginator(students, 20)  # Show 20 students per page
    page = request.GET.get('page')
    students = paginator.get_page(page)

    if query:
        if tieude == "hoten":
            students = Student.objects.filter(name__icontains=query)
            paginator = Paginator(students, 20)  # Show 20 students per page
            page = request.GET.get('page')
            students = paginator.get_page(page)
        if tieude == "detai":
            students = Student.objects.filter(topic__icontains=query)
            paginator = Paginator(students, 20)  # Show 20 students per page
            page = request.GET.get('page')
            students = paginator.get_page(page)
        if tieude == "masv":
            students = Student.objects.filter(id_student__icontains=query)
            paginator = Paginator(students, 20)  # Show 20 students per page
            page = request.GET.get('page')
            students = paginator.get_page(page)
    return render(request, 'list/list.html', {'students': students})

def kltn(request):
    query = request.GET.get("q")
    students = Student.objects.filter(topic_type__icontains='kltn')
    tieude = request.GET.get("tieude")
    paginator = Paginator(students, 20)  # Show 20 students per page
    page = request.GET.get('page')
    students = paginator.get_page(page)
    if tieude == "hoten":
        students = Student.objects.filter(name__icontains=query)&Student.objects.filter(topic_type__icontains='kltn')
        paginator = Paginator(students, 20)  # Show 20 students per page
        page = request.GET.get('page')
        students = paginator.get_page(page)
    if tieude == "detai":
        students = Student.objects.filter(topic__icontains=query)&Student.objects.filter(topic_type__icontains='kltn')
        paginator = Paginator(students, 20)  # Show 20 students per page
        page = request.GET.get('page')
        students = paginator.get_page(page)
    if tieude == "masv":
        students = Student.objects.filter(id_student__icontains=query)&Student.objects.filter(topic_type__icontains='kltn')
        paginator = Paginator(students, 20)  # Show 20 students per page
        page = request.GET.get('page')
        students = paginator.get_page(page)
    return render(request, 'list/list.html', {'students': students})

def nckh(request):
    students = Student.objects.filter(topic_type__icontains='nckh')
    query = request.GET.get("q")
    tieude = request.GET.get("tieude")
    paginator = Paginator(students, 20)  # Show 20 students per page
    page = request.GET.get('page')
    students = paginator.get_page(page)
    if tieude == "hoten":
        students = Student.objects.filter(name__icontains=query)&Student.objects.filter(topic_type__icontains='nckh')
        paginator = Paginator(students, 20)  # Show 20 students per page
        page = request.GET.get('page')
        students = paginator.get_page(page)
    if tieude == "detai":
        students = Student.objects.filter(topic__icontains=query)&Student.objects.filter(topic_type__icontains='nckh')
        paginator = Paginator(students, 20)  # Show 20 students per page
        page = request.GET.get('page')
        students = paginator.get_page(page)
    if tieude == "masv":
        students = Student.objects.filter(id_student__icontains=query)&Student.objects.filter(topic_type__icontains='nckh')
        paginator = Paginator(students, 20)  # Show 20 students per page
        page = request.GET.get('page')
        students = paginator.get_page(page)
    return render(request, 'list/list.html', {'students': students})

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
