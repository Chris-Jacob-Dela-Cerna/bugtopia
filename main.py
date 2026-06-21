

from src import main_logic
from ui import splashes as spl


def main():
    try:
        main_logic.main_menu()
    except KeyboardInterrupt:
        spl.show_goodbye()


if __name__ == "__main__":
    main()