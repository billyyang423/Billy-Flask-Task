import unittest
import app
import json

class MyTests(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
    ##your playground starts
    def test_hello(self):
        self.assertEqual(app.hello(), 'hello')
    def test_health(self):
        response = self.app.get("/health")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], "ok")
    def test_api_get_users(self):
        response = self.app.get("/api/users")
        data = response.get_json()
        users_data = response.get_json(app.get_users)
        self.assertEqual(data, users_data)
    def test_api_get_user(self):
        response = self.app.get("/api/users/1")
        data = response.get_json()
        self.assertEqual(data['user_id'], 1)
    def test_api_add_user(self):
        response = self.app.post('/api/users/add', json = {
            'name': 'David',
            'email': 'david@example.com',
            'phone': '8008580085',
            'address': 'Milky-Fuq-Yourself-Way',
            'country': 'Latveria'
        })
        data = response.get_json()
        self.assertEqual(data['user_id'], 5)
    def test_api_update_user(self):
        response = self.app.put('/api/users/update', json = {
            'name': 'David',
            'email': 'david@new.com',
            'phone': '13371507',
            'address': 'That-Was-Rude-Blvd',
            'country': 'Latveria',
            'user_id': 5
        })
        data = response.get_json()
        self.assertEqual(data['address'], 'That-Was-Rude-Blvd')
    def test_api_delete_user(self):
        response = self.app.delete('/api/users/delete/2')
        data = response.get_json()
        self.assertEqual(data['status'], 'User deleted successfully')
    ##your playground ends

if __name__=="__main__":
    unittest.main()