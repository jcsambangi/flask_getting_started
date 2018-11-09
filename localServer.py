from flask import Flask, jsonify, request
from scipy.spatial import distance

app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    return jsonify({"name": "Jaydeep Sambangi"})


@app.route("/hello/<name>", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, there, {}".format(name)})


@app.route("/distance", methods=["POST"])
def distance():
    points = request.get_json()
    a = points.get("a")
    b = points.get("b")
    computed = distance.euclidean(a, b)
    dictComputed = {
            "distance": computed,
            "a":a,
            "b":b
    }
    return jsonify(dictComputed)


if __name__ == "__main__":
    app.run(host = "127.0.0.1")
