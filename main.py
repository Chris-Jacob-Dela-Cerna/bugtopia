

from src import main_logic


def main():
    # main_logic.main_menu()
    deck1 = ["T1-Ant", "T2-Ant", "T3-Ant"]
    deck2 = ["T1-Beetle", "T2-Beetle", "T1-Dragonfly"]
    from src.battle_logic import battle_logic
    battle_logic(deck1, deck2)

if __name__ == "__main__":
    main()