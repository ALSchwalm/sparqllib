
import unittest
import sparqllib
from rdflib import BNode, Literal

class TestFunctionFilter(unittest.TestCase):
    def setUp(self):
        self.function = "regex"
        self.args = [Literal("Obama")]
        self.filter = sparqllib.querycomponent.FunctionFilter(
            self.function,
            self.args
        )

    def test_serialize(self):
        self.assertEqual(self.filter.serialize(),
                         "FILTER regex(\"Obama\")")

        self.filter.args.append(Literal("i"))
        self.assertEqual(self.filter.serialize(),
                         "FILTER regex(\"Obama\", \"i\")")


class TestCompareFilter(unittest.TestCase):
    def setUp(self):
        self.left = BNode("age")
        self.operator = sparqllib.querycomponent.CompareFilter.Operator.LESS
        self.right = 100
        self.filter = sparqllib.querycomponent.CompareFilter(
            self.left, self.operator, self.right
        )


if __name__ == '__main__':
    unittest.main()
