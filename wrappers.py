from constants import *

def repeat_play(func):
    def inner():
        user_choice = "y"
        while user_choice == "y":
            func()
            print("===================================================")
            user_choice = input("Do you want to play again (y/n)? ").lower()
            valid = False
            while not valid:
                if user_choice in VALID_CHOICES:
                    valid = True
                else:
                    print("Invalid choice.  Please type 'y' to continue or 'n' to stop")

            if user_choice in VALID_AFFIRMATIVES:
                is_game_over = False

            elif user_choice in VALID_NEGATIVES:
                break

        print("Thanks for playing Monopoly!")

    return inner
