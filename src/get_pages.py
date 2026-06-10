

def get_pages_data(data):
    pages = []
    for idx, unit in enumerate(data):
        page = {
            "name": unit["name"],
            "idx": idx,
            "traits": []
        }
        for trait in unit["traits"]:
            page["traits"].append(trait)
        pages.append(page)
    return pages