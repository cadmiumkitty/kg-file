from pydoc import describe
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, SKOS, DCTERMS

# Simple test to validate parsing of relative paths and remote contextx

g = Graph()
g.parse('https://raw.githubusercontent.com/cadmiumkitty/kg-file/main/kg.jsonld', format='json-ld')
g.serialize(destination = 'kg.ttl', format='turtle')
