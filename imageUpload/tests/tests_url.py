from django.test import TestCase
from django.urls import resolve, reverse
from imageUpload.views import upload_Image, list_Images, image_Detail

# Create your tests here.


class testeURL(TestCase):

    def test_uploadImage(self):
        url = reverse('uploadImage')
        self.assertEquals(resolve(url).func, upload_Image)

    def test_listImage(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, list_Images)

    def test_imageDetail(self):
        url = reverse('detail', args=['1'])
        self.assertEquals(resolve(url).func, image_Detail)
