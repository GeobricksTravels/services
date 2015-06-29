from flask import Flask
from flask.ext.cors import CORS
from a_la_romana_services.rest.dao_rest import dao_rest
from a_la_romana_services.config.settings import test_config


print 'init flask...'
app = Flask(__name__)                                   # pragma: no cover

@app.route("/")
def hello():
    return str(test_config)

print 'init cors...'
cors = CORS(app,                                        # pragma: no cover
            resources={                                 # pragma: no cover
                r'/*': {                                # pragma: no cover
                    'origins': '*',                     # pragma: no cover
                    'headers': ['Content-Type']         # pragma: no cover
                }                                       # pragma: no cover
            })                                          # pragma: no cover
print 'register blueprint...'
app.register_blueprint(dao_rest, url_prefix='/dao')     # pragma: no cover
print 'app run'
if __name__ == '__main__':                              # pragma: no cover
    app.run(debug=True, threaded=True)                  # pragma: no cover
