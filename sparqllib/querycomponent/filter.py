from sparqllib.querycomponent import QueryComponent
from sparqllib.utils import serialize_rdf_term
import enum

class RegexFilter(QueryComponent):
    def __init__(self, term, expression, options):
        self.term = term
        self.expression = expression
        self.options = options

    def serialize(self):
        return 'FILTER regex({term}, "{expression}", "{options}")'.format(
            term=serialize_rdf_term(self.term),
            expression=self.expression,
            options=self.options
        )

class CompareFilter(QueryComponent):
    class Operator(enum.Enum):
        LESS          = 0
        GREATER       = 1
        EQUAL         = 2
        NOT_EQUAL     = 3
        LESS_EQUAL    = 4
        GREATER_EQUAL = 5
        AND           = 6
        OR            = 7

    def __init__(self, *terms):
        self.terms = terms

    def _serialize_operator(self, operator):
        if isinstance(operator, CompareFilter.Operator):
            if operator == CompareFilter.Operator.LESS:            return " < "
            elif operator == CompareFilter.Operator.GREATER:       return " > "
            elif operator == CompareFilter.Operator.EQUAL:         return " = "
            elif operator == CompareFilter.Operator.NOT_EQUAL:     return " != "
            elif operator == CompareFilter.Operator.LESS_EQUAL:    return " <= "
            elif operator == CompareFilter.Operator.GREATER_EQUAL: return " >= "
            elif operator == CompareFilter.Operator.AND:           return " && "
            elif operator == CompareFilter.Operator.OR:            return " || "
        else:
            raise ValueError("Operator must be a CompareFilter.Operator")

    def serialize(self):
        serialized = ""
        for term in self.terms:
            if isinstance(term, CompareFilter.Operator):
                serialized += self._serialize_operator(term)
            else:
                serialized += serialize_rdf_term(term)
        return "FILTER({})".format(serialized)

class ExistenceFilter(QueryComponent):
    def __init__(self, *components):
        pass
