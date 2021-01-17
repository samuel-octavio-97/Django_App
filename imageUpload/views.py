from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from imageUpload.forms import ImageForm
from imageUpload.models import Image
from django.contrib import messages


def upload_Image(request):
    if request.method == 'POST':
        image_name = request.POST.get("name", "")
        imageFile = request.FILES.get("image_file")

        # update image if name already exists
        obj, created = Image.objects.update_or_create(
            name=image_name,
            defaults={'image_file': imageFile},
        )
        messages.success(request, 'image uploaded successfully')
        return HttpResponseRedirect(request.path_info)
    else:
        form = ImageForm()
    return render(request, 'addImage.html', {'form': form})


def list_Images(request):
    if request.method == 'GET':
        Images = Image.objects.all()
        return render(request, 'imageList.html',
                      {'images': Images})


def image_Detail(request, id):
    image = get_object_or_404(Image, pk=id)
    return render(request, 'imageDetail.html', {'image': image})
