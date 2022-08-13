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
    
    def test_berat_list_exist(self):
        response = Client().get('/berat/list')
        self.assertEqual(response.status_code,200)
    
    def test_berat_list_use_template(self):
        response = Client().get('/berat/list')
        self.assertTemplateUsed(response,'berat_register/berat_list.html')
    
    def test_update_berat(self):
        data = {
            'tanggal':"2022-08-15",
            "berat_max": 50,
            "berat_min": 50,
        }
        response = self.client.post('/berat/1/', data)
        self.assertEqual(response.status_code,302)
        
    def test_post_berat(self):
        data = {
            'tanggal':"2022-08-15",
            "berat_max": 50,
            "berat_min": 50,
        }
        response = self.client.post('/berat/0/', data)
        self.assertEqual(response.status_code,302)
    
    def test_berat_update_use_temp(self):
        response = Client().get('/berat/1/')
        self.assertTemplateUsed(response,'berat_register/berat_form.html')

    def test_delete_berat(self):
        response = Client().get('/berat/delete/1/')
        self.assertEqual(response.status_code,302)