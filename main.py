

from src import main_logic


def main():
    #Temporary
    from ui import battle_screen as bs
    from src.unit_class import Unit
    from utils import access_json as aj
    from utils import ui_helpers as uh

    units_data = aj.load_json_data("units_default.json")
    deck1 = [Unit(0, 0, units_data), None, Unit(2, 0, units_data)]
    deck2 = [Unit(0, 2, units_data), None, None]

    battle_ui = bs.convert_battle_ui(deck1, deck2)
    uh.display(battle_ui)

    # main_logic.main_menu()


if __name__ == "__main__":
    main()