#!/usr/bin/env python
'''

A script to demonstrate the various SPARQL filter query components by
determining the relationship between Michelle and Barack Obama
'''

from sparqllib import *
from rdflib import BNode, Literal
from rdflib.namespace import FOAF
from pprint import pprint

def main():
    # Create the necessary variables
    obama, michelle = BNode("Obama"), BNode("Michelle")
    relation, value = BNode("relation"), BNode("value")

    # Select only the relation
    q = Query(result_vars=[relation])

    # Retrieve Barack and Michelle
    q.add((obama, FOAF.name, Literal("Barack Obama", lang="en")))
    q.add((michelle, FOAF.name, Literal("Michelle Obama", lang="en")))

    # Get every relation from barack to any value
    q.add((obama, relation, value))

    # Filter such that the values much be michelle
    q.add(CompareFilter(value, CompareFilter.Operator.EQUAL, michelle))

    # Note that this could also be acheived by adding the triple
    # "?obama ?relation ?michelle" rather than filtering.

    print(q)
    pprint(q.execute())

if __name__ == "__main__":
    main()
