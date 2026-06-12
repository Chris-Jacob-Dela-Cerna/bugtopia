

import json
import os


def get_data_path(file_name):
    abs = os.path.abspath(__file__)
    dir = os.path.dirname(abs)
    dir2 = os.path.dirname(dir)
    path = os.path.join(dir2, "data", file_name)

    return path


def load_json_data(file_name):
    path = get_data_path(file_name)
    with open(path, "r") as file:
        file_data = json.load(file)
    return file_data


def dump_json_data(file_name, file_data):
    path = get_data_path(file_name)
    with open(path, "w") as file:
        json.dump(file_data, file, indent=4)