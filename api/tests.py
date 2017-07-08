from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Bucketlist
# Create your tests here.


class bucketTestCase(TestCase):
    ''' this class defines the test for the Bucketlist model '''

    def setUp(self):
        self.bucketlist_name = "Become a Pokemon Master"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_for_buckelist_creation(self):
        '''Test if the bucketlist model can create a bucketlist '''
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class testForView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'name': 'GO TO Singapore'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")
        )
    def test_if_api_create_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
