from flask import Flask, jsonify, request
import numpy

app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    return jsonify({"name": "Jaydeep Sambangi"})


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return jsonify({"message": "Hello, there, {}".format(name)})


@app.route("/distance", methods=["POST"])
def distance():
    points = request.get_json()
    aa = numpy.array(points.get("a"))
    bb = numpy.array(points.get("b"))
    first = numpy.linalg.norm(aa-bb)
    computed = numpy.array(first).tolist()
    dictComputed = {
            "distance": computed,
            "a":points.get("a"),
            "b":points.get("b")
    }
    return jsonify(dictComputed)


if __name__ == "__main__":
    app.run(host = "0.0.0.0")
