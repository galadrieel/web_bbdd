from flask import Flask   # python3 -m pip install flask

app = Flask(__name__)

@app.route("/hola")
def hello_world():
    return '{"missatge": "Hola mon"}'

@app.route("/adeu")
def adeu():
    return '{"missatge": "A10 mon cruel!"}'



if __name__ == "__main__":
    app.run()