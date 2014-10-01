from sparqllib.querycomponent import QueryComponent
from sparqllib.querycomponent.group import Group

class Union(QueryComponent):
    def __init__(self, *components):
        self.components = []
        for i, component in enumerate(components):
            if isinstance(component, Group):
                self.components.append(component)
            else:
                self.components.append(Group(component))

    def serialize(self):
        serialized = ""

        for component in self.components[:-1]:
            serialized += "{0} UNION".format(component.serialize())
        serialized += "\n{0}\n".format(self.components[-1].serialize())

        return serialized
