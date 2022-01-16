from.test_setup import TestSetUp

class TestViews(TestSetUp):

	def test_users_view_list(self):
		res = self.client.get(self.users_url)

		self.assertEqual(res.status_code, 200)


	def test_create_user(self):
		res = self.client.post(self.users_url, self.user_data, format="json")

		self.assertEqual(res.status_code, 200)


	def test_get_user_detail(self):
		res = self.client.post(self.users_url, self.user_data, format="json")
		res = self.client.get(self.users_detail)
		
		self.assertEqual(res.status_code, 200)

	def test_update_user(self):
		res = self.client.post(self.users_url, self.user_data, format="json")
		res = self.client.put(self.users_detail, self.user_data, format="json")
		
		self.assertEqual(res.status_code, 200)

	def test_delete_user(self):
		res = self.client.post(self.users_url, self.user_data, format="json")
		res = self.client.delete(self.users_detail)
		
		self.assertEqual(res.status_code, 200)