import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestFitnessApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_log_workout_success(self):
        response = self.client.post('/log_workout', json={"type": "run", "duration": 30})
        self.assertEqual(response.status_code, 201)

    def test_get_workouts(self):
        response = self.client.get('/get_workouts')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
