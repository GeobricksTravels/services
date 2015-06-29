from flask import Flask
from flask.ext.cors import CORS
from a_la_romana_services.rest.dao_rest import dao_rest


app = Flask(__name__)                                   # pragma: no cover
cors = CORS(app,                                        # pragma: no cover
            resources={                                 # pragma: no cover
                r'/*': {                                # pragma: no cover
                    'origins': '*',                     # pragma: no cover
                    'headers': ['Content-Type']         # pragma: no cover
                }                                       # pragma: no cover
            })                                          # pragma: no cover
app.register_blueprint(dao_rest, url_prefix='/dao')     # pragma: no cover

@app.route('/', methods=['GET'])
def say_hello():
    return 'hello?'

if __name__ == '__main__':                              # pragma: no cover
    app.run(debug=True, threaded=True)                  # pragma: no cover
