from sparqllib.querycomponent import QueryComponent
from sparqllib.utils import convert_components

class Group(QueryComponent):
    ''' Representation of a SPARQL group element

    A SPARQL group is a curly bracket-delimited set of triples, filters, other groups,
    or query components.
    '''
    def __init__(self, *components):
        self.components = convert_components(components)

    def serialize(self):
        serialized = "{"

        for component in self.components:
            serialized += component.serialize()

        serialized += "}"
        return serialized
