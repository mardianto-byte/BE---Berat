from django.test import TestCase, Client
from .models import Berat

# Create your tests here.
class TestURL(TestCase):
    def setUp(self):
        self.berat = Berat.objects.create(
            tanggal="2022-08-15",
            berat_max= 50,
            berat_min= 48,
        )

    def test_berat_url_is_exist(self):
        response = Client().get('/berat/')
        self.assertEqual(response.status_code,200)

    def test_berat_use_template(self):
        response = Client().get('/berat/')
        self.assertTemplateUsed(response,'berat_register/berat_form.html')
    
    