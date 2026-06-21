

from utils.ui_helpers import fit


def prompt(message):
    input(
        f"{"\n" * 35}"
        "\n               ╭──────────────────────────────╮"
        f"\n{fit(message, 28, "               │ ", " |")}"
        "\n               ╰──────────────────────────────╯"
        "\n                 "
    )