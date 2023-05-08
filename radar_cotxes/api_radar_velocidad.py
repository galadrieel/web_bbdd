#!usr/bin/python3

import flask
import json

app = flask.Flask(__name__)

@app.route("/multa/<permitida>/<real>", methods=['GET'])
def multa(permitida, real):
    resultat = ""
    valor_permitida = int(permitida)
    valor_real = int(real)
    if valor_real <= valor_permitida:
        resultat = "correcto"
    elif valor_real <= valor_permitida * 1.1:
        resultat = "Margen de seguridad"
    else:
        resultat= "multa"
    return flask.jsonify({"resultat": resultat})



 


def main():
    app.run()
    
if __name__ == "__main__":
    main()
    