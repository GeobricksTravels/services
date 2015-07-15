from flask import Flask                                 # pragma: no cover
from flask.ext.cors import CORS                         # pragma: no cover
from spartimm_services.rest.dao_rest import dao_rest    # pragma: no cover


app = Flask(__name__)                                   # pragma: no cover

cors = CORS(app,                                        # pragma: no cover
            resources={                                 # pragma: no cover
                r'/*': {                                # pragma: no cover
                    'origins': '*',                     # pragma: no cover
                    'headers': ['Content-Type']         # pragma: no cover
                }                                       # pragma: no cover
            })                                          # pragma: no cover
app.register_blueprint(dao_rest, url_prefix='/dao')     # pragma: no cover

if __name__ == '__main__':                              # pragma: no cover
    app.run(debug=True, threaded=True)                  # pragma: no cover
