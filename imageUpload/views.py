from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Sam. This is an image upload app")
