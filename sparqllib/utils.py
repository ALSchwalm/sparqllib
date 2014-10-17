'''
This modules contains various utility functions for use by sparqllib

'''

import rdflib
import sparqllib.querycomponent

def convert_component(component):
    if not isinstance(component, sparqllib.querycomponent.QueryComponent):
        return sparqllib.querycomponent.Triple(*component)
    else:
        return component

def convert_components(components):
    ''' Construct a list of QueryComponents from 'components'

    Args:
        components: A list of QueryComponents or tuples
    '''
    converted_components = []

    for component in components:
        converted_components.append(convert_component(component))
    return converted_components

def serialize_rdf_term(term):
    ''' Convert one of the components of an rdf-triple to a string

    Converts rdflib BNodes, Literal and URIRefs to an appropriate string
    format for use in a sparql query. If 'component' is not one of these
    types, it is converted to a Literal and then serialized.
    '''
    if isinstance(term, rdflib.BNode):
        return "?" + str(term)
    if isinstance(term, rdflib.term.URIRef) or \
       isinstance(term, rdflib.Literal):
        return term.n3()
    else:
        return rdflib.Literal(term).n3()
