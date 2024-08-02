import unittest
from src.app import create_app
from src.database import db

class TaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()

    def test_get_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.client.post('/tasks', json={
            'title': 'Test Task',
            'description': 'This is a test task'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Task', response.get_json()['title'])
