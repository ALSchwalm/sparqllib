
import unittest
import sparqllib
from rdflib import BNode, Literal
from rdflib.namespace import FOAF

class TestQuery(unittest.TestCase):
    def setUp(self):
        self.formatter = sparqllib.formatter.BasicFormatter()
        self.query = sparqllib.Query()

    def test_empty_query(self):
        self.assertEqual(self.formatter.format(self.query),
                         "SELECT DISTINCT * WHERE {\n}")

    def test_distinct_query(self):
        self.assertEqual(self.formatter.format(self.query),
                         "SELECT DISTINCT * WHERE {\n}")

        self.query.distinct_results = False
        self.assertEqual(self.formatter.format(self.query),
                         "SELECT * WHERE {\n}")

    def test_result_limit(self):
        self.query.result_limit = 10
        self.assertEqual(self.formatter.format(self.query),
                         "SELECT DISTINCT * WHERE {\n} LIMIT 10")

    def test_order_by(self):
        subject, relation = BNode("subject"), BNode("relation")
        self.query.add((subject, relation, Literal("Cats")))
        self.query.order_by = subject
        self.assertEqual(self.formatter.format(self.query),
"""SELECT DISTINCT * WHERE {
  ?subject ?relation "Cats" .
} ORDER BY ?subject""")

    def test_indexing(self):
        triple = (BNode(), BNode(), BNode())
        self.query.add(triple)

        self.assertEqual(self.query[0], triple)

    def test_iterator(self):
        triple = (BNode(), BNode(), BNode())
        self.query.add(triple)

        elements = [element for element in self.query]
        for element in elements:
            self.assertTrue(isinstance(element, sparqllib.QueryComponent))

if __name__ == '__main__':
    unittest.main()
