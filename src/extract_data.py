

import json
import os


def get_json_data(file_name):
    abs = os.path.abspath(__file__)
    dir = os.path.dirname(abs)
    dir2 = os.path.dirname(dir)
    path = os.path.join(dir2, "data", file_name)

    with open(path, "r") as file:
        data = json.load(file)

    return data