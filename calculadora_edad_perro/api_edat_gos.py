#!usr/bin/python3

import json
import flask
import gos
app = flask.Flask(__name__)

@app.route("/equivalencia", methods=['GET'])

    

def calcula_equivalencia():
    body_text = flask.request.get_data()
    body_dict = json.loads(body_text)
    edat_gos = body_dict["edat"]
    un_gos = gos.Gos(float(edat_gos))
    un_gos.calcula_equivalencia()
    dict_gos = json.loads(str(un_gos))
    return flask.jsonify(dict_gos)

def main():
    app.run()
    
if __name__ == "__main__":
    main()
