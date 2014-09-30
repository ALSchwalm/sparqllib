import abc

class Statement:
    @abc.abstractmethod
    def serialize(self):
        ''' Should return a valid SPARQL string representation of the statement.
        '''
        pass
