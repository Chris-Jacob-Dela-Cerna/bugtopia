

def fit(max_length, text_length):
    return (max_length - len(str(text_length))) * " "


def display(ui):
    print("\n".join(ui))