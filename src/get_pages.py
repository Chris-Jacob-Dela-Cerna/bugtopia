

def get_pages_data(data):
    pages = []
    for idx, bug in enumerate(data):
        page = {
            "name": bug["name"],
            "idx": idx,
            "species": []
        }
        for species in bug["species"]:
            page["species"].append(species)
        pages.append(page)
    return pages