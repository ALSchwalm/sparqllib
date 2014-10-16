
import unittest
import sparqllib

class TestBasicFormatter(unittest.TestCase):
    def setUp(self):
        self.formatter = sparqllib.formatter.BasicFormatter()

    def test_newlines(self):
        self.assertEqual(self.formatter.format("{}"), "{\n}")

    def test_indentation(self):
        self.assertEqual(self.formatter.format("{test text}"), "{\n  test text\n}")
        self.assertEqual(self.formatter.format("{test\ntext}"), "{\n  test\n  text\n}")
        self.assertEqual(self.formatter.format("{{text}}"), "{\n  {\n    text\n  }\n}")

    def test_trim_whitespace(self):
        self.assertEqual(self.formatter.format("text  \n"), "text\n")

    def test_remove_duplicate_newlines(self):
        self.assertEqual(self.formatter.format("\n\n"), "\n")
        self.assertEqual(self.formatter.format("\n"), "\n")

if __name__ == '__main__':
    unittest.main()
