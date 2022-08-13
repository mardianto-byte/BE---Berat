from django.test import TestCase

# Create your tests here.
class TestURL(TestCase):
    def setUp(self):
        self.berat = Berat.objects.create(
            tanggal="2022-08-15",
            berat_max= 50,
            berat_min= 48,
        )