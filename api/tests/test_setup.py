from rest_framework.test import APITestCase

from django.urls import reverse 

class TestSetUp(APITestCase):


	def setUp(self):
		self.users_url = reverse('users')
		self.users_detail = reverse('user-detail', kwargs={'id':1})


		self.user_data = {
			"id": 1,
			"first_name": "James",
			"last_name": "Butt",
			"company_name": "Benton, John B Jr",
			"city": "New Orleans",
			"state": "LA",
			"zip_code": 70116,
			"email": "jbutt@gmail.com",
			"web": "http://www.bentonjohnbjr.com",
			"age": 70
		}

		return super().setUp()

	def tearDown(self):
		return super().tearDown()