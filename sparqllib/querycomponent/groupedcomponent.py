from sparqllib.querycomponent import QueryComponent
from sparqllib.querycomponent.group import Group

class GroupedComponent(QueryComponent):
    def __init__(self, *components):
        self.components = []
        for i, component in enumerate(components):
            if isinstance(component, Group):
                self.components.append(component)
            else:
                self.components.append(Group(component))

class Union(GroupedComponent):
    def __init__(self, *components):
        super().__init__(*components)

    def serialize(self):
        serialized = ""
        for component in self.components[:-1]:
            serialized += "{0} UNION".format(component.serialize())
        serialized += "\n{0}\n".format(self.components[-1].serialize())

        return serialized

class Optional(GroupedComponent):
    def __init__(self, *components):
        super().__init__(*components)

    def serialize(self):
        serialized = ""
        if len(self.components) == 1:
            serialized = "OPTIONAL {0}\n".format(self.components[0].serialize())
        else:
            for component in self.components[:-1]:
                serialized += "{0} OPTIONAL".format(component.serialize())
            serialized += "\n{0}\n".format(self.components[-1].serialize())

        return serialized
