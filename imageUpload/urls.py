from django.urls import path
from imageUpload import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('list', views.listImages, name='list'),
    path('uploadImage', views.uploadImage, name='uploadImage'),
]
