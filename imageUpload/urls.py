from django.urls import path
from imageUpload import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('detail/<int:id>', views.image_Detail, name='detail'),
    path('list', views.list_Images, name='list'),
    path('add', views.upload_Image, name='uploadImage'),
]
