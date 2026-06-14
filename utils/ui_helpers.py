

def display(ui):
    print("\n".join(ui))


def fit(max_length, text_length):
    return (max_length - len(str(text_length))) * " "


def fit2(text="", max_length=0, first="", last=""):
    space = (max_length - len(str(text))) * " "
    return f"{first}{text}{space}{last}"