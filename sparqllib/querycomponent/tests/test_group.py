
import unittest
import sparqllib
from rdflib import BNode, Literal

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.group = sparqllib.querycomponent.Group()

    def test_add(self):
        self.assertEqual(self.group.components, [])
        triple = (BNode("subject"), BNode("relation"), Literal("Cats"))
        self.group += triple
        self.assertEqual(self.group.components, [triple])

    def test_serialize(self):
        self.assertEqual(self.group.serialize(), "{}")

        triple = (BNode("subject"), BNode("relation"), Literal("Cats"))
        self.group += triple

        self.assertEqual(self.group.serialize(),
                         "{?subject ?relation \"Cats\" .\n}")
