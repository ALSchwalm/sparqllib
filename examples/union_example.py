#!/usr/bin/env python
'''

A script to demonstrate the usage of the Union QueryComponent
'''

from sparqllib import *
from rdflib import BNode, Literal
from rdflib.namespace import FOAF
from pprint import pprint

def main():
    # prepare query variables
    obama, bush, relation, value = (BNode("Obama"), BNode("Bush"),
                                    BNode("relation"), BNode("value"))

    # construct query, selecting the relations and values
    q = Query(result_vars=[relation, value])

    # create a group which will contain information about Barack Obama
    obama_values = Group((obama, FOAF.name, Literal("Barack Obama", lang="en")),
                         (obama, relation, value))

    # create a group which will contain information about George Bush
    bush_values = Group((bush, FOAF.name, Literal("George Walker Bush", lang="en")),
                        (bush, relation, value))

    # create a union of these groups and add the union to the query
    q.add(Union(obama_values, bush_values))

    # limit the query results
    q.result_limit = 50

    # print the query
    print(q)

    # perform the query and print the results
    pprint(q.execute())

if __name__ == "__main__":
    main()
