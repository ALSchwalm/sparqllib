
import unittest
import sparqllib
from rdflib import BNode, Literal
from rdflib.namespace import FOAF

class TestQuery(unittest.TestCase):
    def setUp(self):
        self.query = sparqllib.Query()

    def test_empty_query(self):
        self.assertEqual(self.query.serialize(),
                         "SELECT DISTINCT * WHERE {}")

    def test_distinct_query(self):
        self.assertEqual(self.query.serialize(),
                         "SELECT DISTINCT * WHERE {}")

        self.query.distinct_results = False
        self.assertEqual(self.query.serialize(),
                         "SELECT * WHERE {}")

    def test_result_vars(self):
        self.assertEqual(self.query.result_vars, [])

        subject, relation = BNode("subject"), BNode("relation")
        query = sparqllib.Query(result_vars=[subject])
        self.assertEqual(query.result_vars, [subject])
        self.assertEqual(query.serialize(),
                         "SELECT DISTINCT ?subject WHERE {}")

        self.query.result_vars=[subject]
        self.assertEqual(self.query.serialize(),
                         "SELECT DISTINCT ?subject WHERE {}")

    def test_result_limit(self):
        self.query.result_limit = 10
        self.assertEqual(self.query.serialize(),
                         "SELECT DISTINCT * WHERE {} LIMIT 10")

    def test_order_by(self):
        subject, relation = BNode("subject"), BNode("relation")
        self.query.add((subject, relation, Literal("Cats")))
        self.query.order_by = subject
        self.assertEqual(self.query.serialize(),
                         """SELECT DISTINCT * WHERE {?subject ?relation "Cats" .\n""" \
                         """} ORDER BY ?subject""")

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
