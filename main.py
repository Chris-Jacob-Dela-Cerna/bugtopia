

import sys
from src import main_logic
from ui import splashes as spl


def main():
    main_logic.main_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        spl.show_goodbye()