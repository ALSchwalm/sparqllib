'''
A small python library to allow programatic construction of SPARQL queries.
'''

__all__ = [
    'Query',
    'QueryComponent',
    'Triple'
]

from sparqllib.query import Query
from sparqllib.triple import Triple
from sparqllib.querycomponent import QueryComponent
