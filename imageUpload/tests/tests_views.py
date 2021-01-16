from django.test import TestCase
from imageUpload.models import Image
from django.urls import resolve, reverse
from imageUpload.views import uploadImage

# Create your tests here.


class tester(TestCase):

    def test_uploadImage(self):
        url = reverse('uploadImage')
        self.assertEquals(resolve(url).func, uploadImage)
