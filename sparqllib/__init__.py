'''
A small python library to allow programatic construction of SPARQL queries.
'''

__all__ = [
    'Query',
    'QueryComponent',
    'Triple',
    'Union',
    'Group',
    'Optional',
    'Minus',
    'BasicFormatter',
    'Formatter',
    'CompareFilter',
    'RegexFilter',
    'ExistenceFilter',
]

from sparqllib.query import Query
from sparqllib.querycomponent import *
from sparqllib.formatter import Formatter, BasicFormatter
