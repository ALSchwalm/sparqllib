from sparqllib.querycomponent import QueryComponent
from sparqllib.triple import Triple

class Union(QueryComponent):
    def __init__(self, *components):
        self.components = []

        for component in components:
            if not isinstance(component, QueryComponent):
                self.components.append(Triple(*component))
            else:
                self.components.append(component)

    def serialize(self):
        serialized = ""

        for component in self.components[:-1]:
            serialized += "{{\n{0}}} UNION\n".format(component.serialize())
        serialized += "{{\n{0}}}\n".format(self.components[-1].serialize())

        return serialized
