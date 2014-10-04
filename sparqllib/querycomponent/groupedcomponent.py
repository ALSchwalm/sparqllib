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

    def _serialize(self, name):
        serialized = ""
        if len(self.components) == 1:
            serialized = "{0} {1}\n".format(name, self.components[0].serialize())
        else:
            for component in self.components[:-1]:
                serialized += "{0} {1}".format(component.serialize(), name)
            serialized += "\n{0}\n".format(self.components[-1].serialize())

        return serialized


class Union(GroupedComponent):
    def __init__(self, *components):
        super().__init__(*components)

    def serialize(self):
        #TODO error on union with one component?
        return self._serialize("UNION")

class Optional(GroupedComponent):
    def __init__(self, *components):
        super().__init__(*components)

    def serialize(self):
        return self._serialize("OPTIONAL")

class Minus(GroupedComponent):
    def __init__(self, *components):
        super().__init__(*components)

    def serialize(self):
        return self._serialize("MINUS")
