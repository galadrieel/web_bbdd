from flask import Flask   # python3 -m pip install flask

app = Flask(__name__)

@app.route("/suma/<n1>/<n2>")
def suma(n1, n2):
    return {"resultat" : int(n1) + int(n2) }


@app.route("/resta/<n1>/<n2>")
def resta(n1, n2):
    return {"resultat" : int(n1) - int(n2) }

@app.route("/multiplicacio/<n1>/<n2>")
def multiplicacio(n1, n2):
    return {"resultat" : int(n1) * int(n2) }

@app.route("/divisio/<n1>/<n2>")
def divisio(n1, n2):
    if int(n2) == 0:
        return "" , 400
    
    return {"resultat" : int(n1) / int(n2) }


if __name__ == "__main__":
    app.run()





