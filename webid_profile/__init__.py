from rdflib.namespace import RDF, DCTERMS, FOAF, RDFS, SKOS, OWL, Namespace
from .core import NSManager

ns = NSManager({
      'dcterms': DCTERMS,
      'rdf': RDF,
      'rdfs': RDFS,
      'foaf': FOAF,
      'skos': SKOS,
      'owl': OWL,
      'bio': Namespace("http://purl.org/vocab/bio/0.1/"),
      'cert': Namespace("http://www.w3.org/ns/auth/cert#"),
      'xsd': Namespace("http://www.w3.org/2001/XMLSchema#"),
      'wot': Namespace("http://xmlns.com/wot/0.1/")
    })
