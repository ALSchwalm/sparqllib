import rdflib
from sparqllib.querycomponent import QueryComponent

class Triple(QueryComponent):
    def __init__(self, subject, relationship, object):
        self.subject = subject
        self.relationship = relationship
        self.object = object

    def _serialize_triple_component(self, component):
        ''' Convert one of the components of a Triple or Query to a string

        Converts rdflib BNodes, Literal and URIRefs to an appropriate string
        format for use in a sparql query. If 'component' is not one of these
        types, it is converted to a Literal and then serialized.
        '''
        if isinstance(component, rdflib.BNode):
            return "?" + str(component)
        if isinstance(component, rdflib.term.URIRef) or \
           isinstance(component, rdflib.Literal):

            return component.n3()
        else:
            return rdflib.Literal(component).n3()

    def serialize(self):
        return "{subject} {relationship} {object} .\n".format(
            subject=self._serialize_triple_component(self.subject),
            relationship=self._serialize_triple_component(self.relationship),
            object=self._serialize_triple_component(self.object))
