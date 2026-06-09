

import json
import os


def get_default_units():
    abs = os.path.abspath(__file__)
    dir = os.path.dirname(abs)
    dir2 = os.path.dirname(dir)
    path = os.path.join(dir2, "data", "units_default.json")

    with open(path, "r") as file:
        data = json.load(file)

    return data


def get_page_data(data):
    print(data[0])

    return {
        "header": {
            "name": "Marck",
            "number": "1",
        }
    }