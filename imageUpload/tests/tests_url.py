from django.test import TestCase
from imageUpload.models import Image
from django.urls import resolve, reverse
from imageUpload.views import uploadImage, listImages

# Create your tests here.


class testeURL(TestCase):

    def test_uploadImage(self):
        url = reverse('uploadImage')
        self.assertEquals(resolve(url).func, uploadImage)

    def test_basic(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, listImages)
