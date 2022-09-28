from django.test import SimpleTestCase
from django.urls import reverse, resolve
from well_logs.models import current_year
from datetime import datetime as dt

class TestModels(SimpleTestCase):

    def test_current_year(self):
        self.assertEquals(current_year(), dt.now().year)

    # def test_world_map_resolves(self):
    #     # url = reverse('main:world_map')
    #     self.assertEquals()