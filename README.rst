WebID profile
=============

Overview
--------

Basic WebID_ profile page with content-negotiation support.

You just have write your profile in Turtle in *db/profile.ttl*. For example, see *db/profile.ttl.example*.

You can add a picture in the *static/* directory.

For a quick overview, you may visit `my page <https://benjamin.bcgl.fr/profile>`_.


Basic features
~~~~~~~~~~~~~~

- Information: WebID, WebID-TLS, short biography, PGP key, OpenID, photo, email SHA1 hashes.
- Content-negotiation: HTML5 with RDFa, Turtle and RDF/XML.
- Vocabularies: foaf_, cert_, wot_ and bio_.



Dependencies
------------

- Python 2.7
- Flask
- Rdflib 3


License
-------

MIT


Installation
------------
::

    git clone https://github.com/bcogrel/webid-profile.git
    cd webid-profile

    # Setup a virtual environment
    virtualenv2 env
    source env/bin/activate

    # Install dependencies
    pip install -r requirements.txt

    # Test it
    python webid_profile/app.py



.. _WebID: https://dvcs.w3.org/hg/WebID/raw-file/tip/spec/identity-respec.html
.. _foaf: http://xmlns.com/foaf/0.1/
.. _bio: http://purl.org/vocab/bio/0.1/
.. _cert: http://www.w3.org/ns/auth/cert#
.. _wot: http://xmlns.com/wot/0.1/
