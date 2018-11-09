from flask import jsonify
import requests


def points():
    points = {
             "a":[2, 2],
             "b":[5, 6]
    }
    r = requests.post("http://127.0.0.1:5000/distance", json=points)
    distance = r.json()
    print(distance)


if __name__ == "__main__":
    points()
