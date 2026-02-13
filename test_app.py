import unittest
from app import app  # Novera ki Flask app ko import kar raha hai

class TestSentinel(unittest.TestCase):
    def setUp(self):
        # App ko testing mode mein dalne ke liye
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Check karna ke kya home page load ho raha hai (200 OK) [cite: 62]
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Check karna ke response mein 'Sentinel' ka lafz mojood hai [cite: 64]
        # (Ye verify karega ke sahi dashboard open hua hai)
        self.assertIn(b'Sentinel', response.data)

if __name__ == '__main__':
    unittest.main()
