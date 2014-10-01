import rdflib
import SPARQLWrapper
import enum
from sparqllib.triple import Triple
from sparqllib.querycomponent import QueryComponent

class Query:
    ''' Representation of a SPARQL Query.

    Attributes:
      method (QueryMethod):    Determines the SPARQL query method (e.g., SELECT, CONSTRUCT)
      result_vars (list):      A list of BNodes to be selected from the query results
      default_url (string):    Default remote SPARQL url used when 'execute' is called
      result_format:           format of values returned by 'execute'
      result_limit (int):      Number of results to return from 'execute'
      distinct_results (bool): Add 'DISTINCT' to QueryMethod.SELECT queries
    '''

    class Method(enum.Enum):
        SELECT = 0
        CONSTRUCT = 1

    def __init__(self, result_vars=[], default_url="http://dbpedia.org/sparql"):
        self._children = []
        self.method = Query.Method.SELECT
        self.result_vars = result_vars
        self.default_url = default_url
        self.result_format = SPARQLWrapper.JSON
        self.result_limit = None
        self.distinct_results = True

    def _serialize_prefix(self):
        return ""

    def _serialize_result_clause(self):
        result_clause = self.method.name + " "

        if self.distinct_results:
            result_clause += "DISTINCT "

        if self.result_vars:
            for result_var in self.result_vars:
                result_clause += "?{} ".format(str(result_var))
        else:
            result_clause += "* "
        result_clause += "WHERE {\n"
        return result_clause

    def _serialize_query_pattern(self):
        query_pattern = ""
        for child in self._children:
            query_pattern += child.serialize()
        return query_pattern

    def __str__(self):
        prefix = self._serialize_prefix()
        result_clause = self._serialize_result_clause()
        query_pattern = self._serialize_query_pattern()
        tail = "}"

        if self.result_limit:
            tail += " LIMIT " + str(self.result_limit)

        return prefix + result_clause + query_pattern + tail

    def add(self, component):
        ''' Add a new component to the SPARQL query

        Args:
          component: a triple, union, filter or other sparqllib QueryComponent object

        '''
        if not isinstance(component, QueryComponent):
            component = Triple(*component)
        self._children.append(component)

    def execute(self, sparql_url=None):
        ''' Run this query against the given URL and return the results

        Note:
          If sparql_url is None, default_url will be used
        '''
        if sparql_url is None:
            sparql_url = self.default_url

        sparql = SPARQLWrapper.SPARQLWrapper(sparql_url)
        sparql.setQuery(str(self))
        sparql.setReturnFormat(self.result_format)
        return sparql.query().convert()
