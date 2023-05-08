#!/usr/bin/python3


import flask 
import json
import algebra1

app = flask.Flask(__name__)

@app.route("/porcent")
def porcent():
    body_text = flask.request.data 
    body_dict = json.loads(body_text)
    valor_n1 = body_dict["n1"]
    valor_n2 = body_dict["n2"]
    operacio = algebra1.Algebra1(valor_n1, valor_n2. "%")  
    res = json.loads(str(operacio))
    return flask.jsonify(res)




def main():
    app.run()


if __name__ == "__main__":
    main()
    