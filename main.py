

from src import main_logic


def main():
    #Temporary
    from ui import battle_screen as bs
    from src.unit_class import Unit
    from utils import access_json as aj
    from utils import ui_helpers as uh

    units_data = aj.load_json_data("units_default.json")
    warrior = Unit(units_data, 0, 0)
    warrior.poison()
    warrior.pierce()
    deck1 = [warrior, None, Unit(units_data, 2, 0)]
    deck2 = [Unit(units_data, 0, 2), None, None]

    battle_ui = bs.convert_battle_ui(deck1, deck2)
    uh.display(battle_ui)

    main_logic.main_menu()


if __name__ == "__main__":
    main()