

def get_pages_data(data):
    pages = []
    for idx, unit in enumerate(data):
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
        page = {
            "name": unit["name"],
            "idx": idx,
            "traits": [perTrait]
        }
        pages.append(page)
    return pages