import abc
import re

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
        if not isinstance(query, str):
            query = query.serialize()

        #TODO handle braces inside literals correctly
        formatted_query = ""
        indent_level = 0

        for letter in query:

            # newline and reindent on open brace
            if letter == "{":
                indent_level += 1
                formatted_query += "{\n" + self.indent_str*indent_level

            # newline and reindent on close brace
            elif letter == "}":
                indent_level -= 1
                formatted_query += "\n" + self.indent_str*indent_level + "}"

            # reindent after any newline
            elif len(formatted_query) and formatted_query[-1] == '\n':
                formatted_query += self.indent_str*indent_level + letter

            # otherwise just add the letter
            else:
                formatted_query += letter

        # trim whitespace
        formatted_query = re.sub(r'(.)\s+\n', '\g<1>\n', formatted_query, flags=re.MULTILINE)

        # remove duplicate newlines
        formatted_query = re.sub(r'(\n+)', '\n', formatted_query, flags=re.MULTILINE)
        return formatted_query
