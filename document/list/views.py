from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def display_student(request):
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

@login_required(login_url='/list')
def view(request):
    students = Student.objects.all()
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

    if xem=="NCKH":
        students = students.filter(topic_type="NCKH")
    if xem=="KLTN":
        students = students.filter(topic_type="KLTN")

    return render(request, 'list/list.html', {'students': students})

@login_required(login_url='/list')
def kltn(request):
    query = request.GET.get("q")
    students = Student.objects.filter(topic_type__icontains='KLTN')
    tieude = request.GET.get("tieude")
    if tieude == "tatca":
        students = Student.objects.filter(Q(name__icontains=query) | Q(topic__icontains=query) | Q(id_student__icontains=query))&Student.objects.filter(topic_type__icontains='kltn')

    if tieude == "hoten":
        students = Student.objects.filter(name__icontains=query)&Student.objects.filter(topic_type__icontains='KLTN')

    if tieude == "detai":
        students = Student.objects.filter(topic__icontains=query)&Student.objects.filter(topic_type__icontains='KLTN')

    if tieude == "masv":
        students = Student.objects.filter(id_student__icontains=query)&Student.objects.filter(topic_type__icontains='KLTN')


    return render(request, 'list/list.html', {'students': students})

@login_required(login_url='/list')
def nckh(request):
    query = request.GET.get("q")
    students = Student.objects.filter(topic_type__icontains='NCKH')
    tieude = request.GET.get("tieude")
    if tieude == "tatca":
        students = Student.objects.filter(Q(name__icontains=query) | Q(topic__icontains=query) | Q(id_student__icontains=query))&Student.objects.filter(topic_type__icontains='nckh')

    if tieude == "hoten":
        students = Student.objects.filter(name__icontains=query)&Student.objects.filter(topic_type__icontains='NCKH')

    if tieude == "detai":
        students = Student.objects.filter(topic__icontains=query)&Student.objects.filter(topic_type__icontains='NCKH')

    if tieude == "masv":
        students = Student.objects.filter(id_student__icontains=query)&Student.objects.filter(topic_type__icontains='NCKH')

 
    return render(request, 'list/list.html', {'students': students})

@staff_member_required(login_url='/list')
def edit_info(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bạn vừa thực hiện sửa thông tin thành công')
            return redirect('display_student')
        messages.success(request, 'Vui lòng kiểm tra lại thông tin')

    else:
        form = StudentForm(instance=student)

    return render(request, 'list/edit_info.html', {'form' : form})

@staff_member_required(login_url='/list')
def delete_student(request, pk):
    Student.objects.filter(id=pk).delete()

    students = Student.objects.all()
    messages.success(request, 'Bạn vừa thực hiện xóa thành công')
    return redirect('display_student')

@staff_member_required(login_url='/list')
def upload_fl(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm sinh viên thành công')
            return redirect('display_student')
    else:
        form = StudentForm()
    return render(request, 'list/add_student.html', {
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Đăng kí thành công, hãy đăng nhập để tiếp tục')
            return redirect('/login')
    else:
        form = UserCreationForm()

    return render(request,'registration/register.html',{'form':form})

def ajax(request):
    object_list = Student.objects.all() #or any kind of queryset
    json = serializers.serialize('json', object_list)
    return HttpResponse(json, content_type='application/json')

