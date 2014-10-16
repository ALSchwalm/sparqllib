import rdflib
from sparqllib.querycomponent import QueryComponent
from sparqllib.utils import serialize_rdf_term

class Triple(QueryComponent):
    def __init__(self, subject, relationship, object):
        self.subject = subject
        self.relationship = relationship
        self.object = object

    # Allow a tuple to compare equal to a Triple
    def __eq__(self, other):
        if not isinstance(other, Triple):
            other = Triple(*other)

        return (other.subject == self.subject and
                other.relationship == self.relationship and
                other.object == self.object)

    def serialize(self):
        return "{subject} {relationship} {object} .\n".format(
            subject=serialize_rdf_term(self.subject),
            relationship=serialize_rdf_term(self.relationship),
            object=serialize_rdf_term(self.object))
