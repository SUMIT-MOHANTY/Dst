import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.ai_service import AIService

class TestAIService(unittest.TestCase):
    def setUp(self):
        self.ai_service = AIService()
    
    def test_validate_request_valid(self):
        result = self.ai_service.validate_request({'prompt': 'Hello'})
        self.assertTrue(result)
    
    def test_validate_request_invalid(self):
        result = self.ai_service.validate_request({})
        self.assertFalse(result)
    
    def test_validate_request_null(self):
        result = self.ai_service.validate_request(None)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
