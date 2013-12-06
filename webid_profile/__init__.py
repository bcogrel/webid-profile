from rdflib.namespace import RDF, DCTERMS, FOAF, RDFS, Namespace
from .core import NSManager

ns = NSManager({
      'dcterms': DCTERMS,
      'rdf': RDF,
      'rdfs': RDFS,
      'foaf': FOAF,
      'cert': Namespace("http://www.w3.org/ns/auth/cert#"),
      'xsd': Namespace("http://www.w3.org/2001/XMLSchema#"),
      'wot': Namespace("http://xmlns.com/wot/0.1/")
    })
