from django.http import HttpResponse
from django.shortcuts import render, redirect
from imageUpload.forms import ImageForm
from imageUpload.models import Image


def uploadImage(request):
    if request.method == 'POST':
        image_name = request.POST.get("name", "")
        imageFile = request.FILES.get("image_file")
        obj, created = Image.objects.update_or_create(
            name=image_name,
            defaults={'image_file': imageFile},

        )
        form = ImageForm(request.POST, request.FILES)
        return redirect('uploadImage')

    else:
        form = ImageForm()
    return render(request, 'addImage.html', {'form': form})
