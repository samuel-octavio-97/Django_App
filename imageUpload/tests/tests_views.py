from django.test import TestCase, Client
from imageUpload.models import Image
from django.urls import resolve, reverse
from imageUpload.views import uploadImage, listImages
import json


class testeViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.image1 = Image.objects.create(
            name="test",
            image_file="1.png"
        )

    def test_post(self):
        response = self.client.post(self.detail_url, {
            'name': "test",
            'image_file': "1.png"
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.image1.name, 'test')
