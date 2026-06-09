

from pprint import pprint


def get_pages_data(data):
    pages = []
    for idx, unit in enumerate(data):
        page = {
            "name": unit["name"],
            "idx": idx,
            "traits": []
        }
        for trait in unit["traits"]:
            perTrait = {
                "trait": trait["trait"],
                "abilities": trait["abilities"],
                "stats": {
                    "HP": trait["stats"]["health"],
                    "DEF": trait["stats"]["defence"],
                    "ATK": trait["stats"]["attack"]
                }
            }
            page["traits"].append(perTrait)
        pages.append(page)
    pprint(pages)
    return pages