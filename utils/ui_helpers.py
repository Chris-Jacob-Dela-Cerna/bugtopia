

def display(ui):
    print("\n".join(ui))


def fit(text="", max_length=0, first="", last=""):
    space = (max_length - len(str(text))) * " "
    return f"{first}{text}{space}{last}"