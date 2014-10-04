'''
A small python library to allow programatic construction of SPARQL queries.
'''

__all__ = [
    'Query',
    'QueryComponent',
    'Triple',
    'Union',
    'Group',
    'Optional'
]

from sparqllib.query import Query
from sparqllib.querycomponent import *
