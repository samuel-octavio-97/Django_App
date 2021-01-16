from django.http import HttpResponse
from django.shortcuts import render, redirect
from imageUpload.forms import ImageForm
from imageUpload.models import Image


def uploadImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect('uploadImage')

    else:
        form = ImageForm()
    return render(request, 'addImage.html', {'form': form})
