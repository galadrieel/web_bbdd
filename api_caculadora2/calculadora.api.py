#!/usr/bin/python3


import flask
import json
import algebra

app = flask.Flask(__name__)

@app.route("/suma/<n1>/<n2>")
def suma(n1, n2):
    valor_v1 = float(n1)
    valor_v2 = float(n2)
    operacio = algebra.Algebra(valor_v1, valor_v2)
    res = json.loads(str(operacio)) #res = "resultat" : valor_v1 + valor_v2}
    return flask.jsonify(res)


@app.route("/resta")
def resta():
    body_text = flask.request.data 
    body_dict = json.loads(body_text)
    valor_n1 = body_dict["n1"]
    valor_n2 = body_dict["n2"]
    operacio = algebra.Algebra(valor_n1, valor_n2, "-")
    res = json.loads(str(operacio))
    return flask.jsonify(res)

#return (str(body_dict["n1"]) + " " + str(body_dict["n2"])); remplaza a return flask.jsonify(res)




def main():
    app.run()


if __name__ == "__main__":
    main()
    