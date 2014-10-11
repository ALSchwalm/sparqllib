from sparqllib.querycomponent import QueryComponent
from sparqllib.utils import serialize_rdf_term
import enum

class FunctionFilter(QueryComponent):
    def __init__(self, function, *args):
        self.function = function
        self.args = args

    def _serialize_args(self):
        serialized = []

        for arg in self.args:
            if isinstance(arg, QueryComponent):
                serialized.append(arg.serialize())
            else:
                serialized.append(serialize_rdf_term(arg))
        return ", ".join(serialized)

    def serialize(self):
        return 'FILTER {function}({args})'.format(
            function=self.function,
            args=self._serialize_args()
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
