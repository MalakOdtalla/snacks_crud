from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Snack
# Create your tests here.

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Malak', email='malakodtalla@hotmail.com',
            password='Odtalla1993'
        )
        self.snack = Snack.objects.create(
            title="Cheese puff",
            description="A puffed corn snack, coated with a mixture of cheese or cheese-flavored powders[",
            purchaser=self.user,
        )

    def test_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home.html')

    def test_details_view(self):
        response = self.client.get(reverse('Snack_detail', args=[self.snack.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_update_view(self):
        response = self.client.post(reverse('Snack_update', args=[self.snack.id]), {
            'title': 'Cheese puff',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cheese puff')

    def test_create_view(self):
        response = self.client.post(reverse('Snack_create'), {
            'title': 'Nachos',
            'purchaser': self.user,
            'description': 'Fried corn tortillas covered with melted cheddar cheese, pickled jalapeño peppers, and other toppings',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nachos')
        self.assertContains(response, 'Fried corn tortillas covered with melted cheddar cheese, pickled jalapeño peppers, and other toppings')
        self.assertContains(response, 'Malak')

    def test_delete_view(self):
        response = self.client.get(reverse('Snack_delete', args='1'))
        self.assertNotContains(response, 'Nachos')


