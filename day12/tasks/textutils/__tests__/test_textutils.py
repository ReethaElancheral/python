# textutils/__tests__/test_textutils.py

import unittest
from textutils import capitalize_text, word_count, find_keywords, DEFAULT

class TestTextUtils(unittest.TestCase):

    def test_capitalize_text(self):
        self.assertEqual(capitalize_text("hello world"), "Hello World")

    def test_word_count(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_find_keywords(self):
        self.assertEqual(find_keywords("Python is great", DEFAULT['keywords']), ['Python'])

if __name__ == '__main__':
    unittest.main()
