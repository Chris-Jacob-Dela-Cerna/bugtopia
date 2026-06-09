

import json
import os
from pprint import pprint


def get_default_units():
    abs = os.path.abspath(__file__)
    dir = os.path.dirname(abs)
    dir2 = os.path.dirname(dir)
    path = os.path.join(dir2, "data", "units_default.json")

    with open(path, "r") as file:
        data = json.load(file)

    return data


def get_pages_data(data):
    pages = []
    for idx, unit in enumerate(data):
        page = {}
        page["name"] = unit["name"]
        page["idx"] = idx

        page["traits"] = []
        for trait in unit["traits"]:
            perTrait = {}
            perTrait["trait"] = trait["trait"]
            perTrait["abilities"] = trait["abilities"]

            perStat = {
                "HP": trait["stats"]["health"],
                "DEF": trait["stats"]["defence"],
                "ATK": trait["stats"]["attack"]
            }
            perTrait["stats"] = perStat

            page["traits"].append(perTrait)

        pages.append(page)
        
    [
        {
            "name": "Archer",
            "idx": 1,
            "traits": [
                {
                "trait": "Normal",
                "stats": {
                    "HP": 100,
                    "DEF": 10,
                    "ATK": 35
                    }
                },
            ]
        }
    ]