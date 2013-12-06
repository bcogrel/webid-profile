"""
"""

from rdflib import URIRef, Graph
from rdflib.namespace import NamespaceManager
from flask import url_for, g


def uri_for(url, **kwargs):
    """ Tricks that creates an URIRef from the URL """
    kwargs['_external'] = True
    return URIRef(url_for(url, **kwargs))



class ContentError(Exception):
    pass


class NamedGraphNotFoundError(ContentError):
    pass


class AlreadyExistingResourceError(ContentError):
    pass


class AlreadyRegisteredNSError(Exception):
    pass


class NSManager:
    def __init__(self, ns_dict):
        """ TODO: check ns_dict """
        self._ns_dict = ns_dict
        self._rdflib_ns_manager = None

    def __getitem__(self, key):
        return self._ns_dict[key]

    def __getattr__(self, key):
        try:
            return self._ns_dict[key]
        except KeyError:
            raise AttributeError()

    def add_namespace(self, prefix, namespace):
        """ TODO: check prefix and namespace """
        if self._ns_dict.has_key(prefix):
            raise AlreadyRegisteredNSError(prefix)
        self._ns_dict[prefix] = namespace

    @property
    def ns_dict(self):
        return self._ns_dict

    @property
    def rdflib_ns_manager(self):
        """ For using prefixes in RDFlib graphs """
        if self._rdflib_ns_manager is None:
             self._rdflib_ns_manager = NamespaceManager(Graph())
             for namesp in self._ns_dict:
                self._rdflib_ns_manager.bind(namesp, self._ns_dict[namesp])

        return self._rdflib_ns_manager
