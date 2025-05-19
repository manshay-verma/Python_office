# views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import DocumentForm
from .models import Document

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return HttpResponse('Successfully uploaded! 🖼️✅')

def home(request):
    return render(request,'front.html')

def search_image(request):
    query = request.GET.get('q')
    image = None

    if query:
        try:
            image = Document.objects.get(title__iexact=query)
        except Document.DoesNotExist:
            image = None  # Optional: you can show "Image not found" in template

    return render(request, 'search_image.html', {'image': image})