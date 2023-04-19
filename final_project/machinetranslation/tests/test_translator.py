import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrenchTranslator(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestFrenchToEnglishTranslator(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(french_to_english(None), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()