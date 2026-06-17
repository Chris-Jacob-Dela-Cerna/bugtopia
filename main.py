

from src import main_logic


def main():
    # main_logic.main_menu()
    deck_1 = ["T3-Ant", "T2-Grasshopper", "T3-Centipede"]
    deck_2 = ["T2-Ant", "T2-Dragonfly", "T1-Fly"]
    main_logic.battle(deck_1, deck_2)

if __name__ == "__main__":
    main()