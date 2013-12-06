from flask import Flask, g, request, redirect, url_for, render_template
from rdflib import Graph
from webid_profile import ns
from webid_profile.core import uri_for

app = Flask(__name__)

@app.before_request
def before_request():
    graph = getattr(app, 'graph', None)
    if graph is None:
        app.graph = Graph()
        app.graph.namespace_manager = ns.rdflib_ns_manager
        with app.open_resource('db/profile.ttl') as f:
            app.graph.parse(f, format="turtle")
    g.graph = app.graph


@app.route('/')
def root():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    #if request.mimetype == "text/html":
    best = request.accept_mimetypes.best_match(
            ['text/html', 'text/turtle', 'application/rdf+xml'])
    if best == 'text/turtle':
        return g.graph.serialize(format="turtle")
    elif best == 'application/rdf+xml':
        return g.graph.serialize(format="xml")
    else :
        return render_template('profile.html',
                current_uri=uri_for('profile'),
                graph=g.graph, ns=ns)


if __name__ == '__main__':
    app.debug = True
    app.run()
