import abc

class Formatter:
    @abc.abstractmethod
    def format(self, query):
        ''' Should return a human-readable version of the query string
        '''
        pass

class BasicFormatter(Formatter):
    ''' Provides a basic default formatting for query strings

    This formatter provides only indentation levels and newlines at
    open braces.
    '''
    def __init__(self):
        self.indent_str = "  "

    def format(self, query):
        #TODO handle braces inside literals correctly
        formatted_query = ""
        indent_level = 0

        for letter in query:
            if letter == "{":
                indent_level += 1
                formatted_query += "{\n" + self.indent_str*indent_level
            elif letter == "}":
                indent_level -= 1
                formatted_query += "\n" + self.indent_str*indent_level + "}"
            else:
                formatted_query += letter
        return formatted_query
