import unittest
from unittest.mock import patch
from flask import template_rendered
from contextlib import contextmanager
from app import app
from utils import is_valid_currency

@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        with captured_templates(app) as templates:
            response = self.app.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(templates), 1)
            template, context = templates[0]
            self.assertEqual(template.name, 'form.html')

    def test_is_valid_currency(self):
        self.assertTrue(is_valid_currency('USD', {'USD', 'EUR', 'JPY'}))
        self.assertFalse(is_valid_currency('XYZ', {'USD', 'EUR', 'JPY'}))

    @patch('utils.requests.get')
    def test_convert_same_currency(self, mock_get):
        # Mock the response of requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'result': 1}

        # Call the function from utils
        from utils import convert_currency
        result = convert_currency('USD', 'USD', 1, 'https://api.exchangerate.host/convert')

        # Test if the result is as expected
        self.assertEqual(result['result'], 1)

if __name__ == '__main__':
    unittest.main()
