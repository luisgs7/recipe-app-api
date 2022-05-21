"""
Sample tests
"""
from django.test import SimpleTestCase

from app.calc import add


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = add(5, 6)

        self.assertEqual(res, 11)
