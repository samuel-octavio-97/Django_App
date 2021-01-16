from django.test import TestCase, Client
from imageUpload.models import Image
from django.urls import resolve, reverse


class testeViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.add = reverse('uploadImage')
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['1'])
        self.image1 = Image.objects.create(
            name="test",
            image_file="1.png"
        )

    def test_post(self):
        response = self.client.post(self.add)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.image1.name, 'test')
        self.assertEquals(self.image1.image_file, '1.png')

    def test_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'imageList.html')

    def test_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'imageDetail.html')
