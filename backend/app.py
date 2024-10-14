import os
from flask_cors import CORS
from flask import Flask , jsonify
from graph.graph import get_neo4j_data

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/api/graph-data', methods=['GET'])
    def get_graph_data():
        graph_data = get_neo4j_data()
        return jsonify(graph_data)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)