#!/usr/bin/env python
'''

A simple script using sparqllib and rdflib to retrieve a JSON representation
of some information about Barack Obama from dbpedia.
'''

from sparqllib import Query
from rdflib import BNode, Literal
from rdflib.namespace import FOAF
from pprint import pprint

if __name__ == "__main__":
    # construct the query variables (the explict names are optional)
    obama, relation, value = BNode("Obama"), BNode("relation"), BNode("value")

    # construct the query itself, selecting the relation and value variables
    q = Query(result_vars=[relation, value])

    # get everyone with the name Barack Obama
    q.add(subject=obama, relationship=FOAF.name,
          object=Literal("Barack Obama", lang="en"))

    # get every relation these people have to any object
    q.add(subject=obama, relationship=relation, object=value)

    # limit the results to the first 50 distince pairs
    q.result_limit = 50

    print(str(q))
    print(pprint(q.execute()))
