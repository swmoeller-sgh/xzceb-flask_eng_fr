import unittest

from translator import french_to_english, english_to_french

class TestMyModule(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("horse"), "cheval")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("agneau"), "lamb")


if __name__ == "__main__":
    unittest.main()
