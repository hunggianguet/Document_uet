from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *
# Create your views here.

def display_document(request):
        documents = Document.objects.all()
        key_word=''

        if 'search' in request.GET:
            key_word = request.GET['search']
            documents = documents.filter(Q(name__icontains=key_word)|Q(birth_date__icontains=key_word)|Q(topic__icontains=key_word)|Q(grade__icontains=key_word)|Q(tutor__icontains=key_word)|Q(reviewer__icontains=key_word))

        context = {
            'documents': documents,
            'key_word': key_word
            }
        return render(request, 'list/list.html', context)

def add_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_document')

    else:
        form = DocumentForm()
        return render(request, 'list/add_document.html', {'form' : form})

def edit_info(request, pk):
    document = get_object_or_404(Document, pk=pk)

    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('display_document')
    else:
        form = DocumentForm(instance=document)

        return render(request, 'list/edit_info.html', {'form' : form})

def delete_document(request, pk):
    Document.objects.filter(id=pk).delete()

    documents = Document.objects.all()

    return redirect('display_document')
