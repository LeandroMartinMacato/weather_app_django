from django.test import TestCase
from .models import Location

# Create your tests here.
# To test run "python maange.py test"

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code , 200)


class ModelTest(TestCase):
    def test_model_str(self):
        name = Location.objects.create(name="Manila")
        self.assertEqual(str(name), "Manila")

    def test_Location_address_none(self):
        name = Location.objects.create(name="Manila")
        self.assertEqual(name.address , None)

    def test_Location_lat_is_none(self):
        name = Location.objects.create(name="Manila")
        self.assertEqual(name.lat , None)

    def test_Location_long_is_none(self):
        name = Location.objects.create(name="Manila")
        self.assertEqual(name.long , None)
