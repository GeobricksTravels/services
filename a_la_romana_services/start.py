from flask import Flask
from flask.ext.cors import CORS
from a_la_romana_services.rest.dao_rest import dao_rest


# Initialize the Flask app
app = Flask(__name__)

# Initialize CORS filters
cors = CORS(app, resources={r'/*': {'origins': '*', 'headers': ['Content-Type']}})

# Register Blueprint
app.register_blueprint(dao_rest, url_prefix='/rest')

# Start Flask server
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
