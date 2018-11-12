from flask import jsonify
import requests


def points():
    points = {
             "a":[2, 2],
             "b":[5, 6]
    }
    r = requests.post("http://vcm-7315.vm.duke.edu:5000/distance", json=points)
    distance = r.json()
    print(distance)

def other():
    print(requests.get("http://vcm-7315.vm.duke.edu:5000/name").json())
    print(requests.get("http://vcm-7315.vm.duke.edu:5000/hello/Jaydeep").json())

    
if __name__ == "__main__":
    points()
    other()
