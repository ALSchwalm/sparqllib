'''
This modules contains various utility functions for use by sparqllib

'''

from sparqllib.querycomponent import QueryComponent
from sparqllib.querycomponent.triple import Triple

def convert_components(components):
    ''' Construct a list of QueryComponents from 'components'

    Args:
        components: A list of QueryComponents or tuples
    '''
    converted_components = []

    for component in components:
        if not isinstance(component, QueryComponent):
            converted_components.append(Triple(*component))
        else:
            converted_components.append(component)
    return converted_components
