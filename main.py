from game_manager import GameManager
from wrappers import *

game_manager = GameManager()
# Press the green button in the gutter to run the script.
@repeat_play
def main():
    game_manager.play_game()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == "__main__":
    main()



