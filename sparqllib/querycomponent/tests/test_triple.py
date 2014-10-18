
import unittest
import sparqllib
from rdflib import BNode, Literal

class TestTriple(unittest.TestCase):
    def setUp(self):
        self.subject = BNode("subject")
        self.relation = BNode("relation")
        self.object = Literal("Cats")
        self.triple = sparqllib.Triple(self.subject,
                                       self.relation,
                                       self.object)

    def test_init(self):
        with self.assertRaises(TypeError):
            sparqllib.Triple()

    def test_eq(self):
        self.assertTrue(self.triple == (self.subject, self.relation, self.object))
        self.assertTrue((self.subject, self.relation, self.object) == self.triple)
        self.assertFalse(self.triple == ())
        self.assertFalse(self.triple == (self.subject))
        self.assertFalse(self.triple == (self.subject, self.relation, "Dogs"))

    def test_serialize(self):
        self.assertEqual(self.triple.serialize(),
                         "?subject ?relation \"Cats\" .\n")

        self.triple.object = Literal("Dogs", lang='en')
        self.assertEqual(self.triple.serialize(),
                         "?subject ?relation \"Dogs\"@en .\n")

if __name__ == '__main__':
    unittest.main()
