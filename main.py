

from src import main_logic
from src import unit_class as uc
from utils import access_json as aj


def main():
    slot = "T3-Giant"
    units_data = aj.load_json_data("units_default.json")
    unit_idx, trait_idx = uc.get_unit(slot, units_data)
    main_logic.main_menu()


if __name__ == "__main__":
    main()