import random, time
from property import Property
from player import Player

from board_manager import BoardManager

board_manager = BoardManager()

available_players = [
    Player("Michael Anderson",1),
    Player("Computer", 2)
]

players = []

current_player_index = 0
is_game_over = False



def initialize_players(starting_money):
    global current_player_index
    players.clear()
    for player in available_players:
        player.location = 0
        player.in_jail = False
        player.jail_wait_turns = 0
        player.owned_properties = []
        player.money = starting_money
        players.append(player)

    current_player_index = random.randint(0,len(players)-1)

def check_player_elimination(player):
    if player.money < 0:
        print("Player {} is out of money and has been eliminated".format(player.name))
        players.remove(player)


def make_improvements(player):
    print("Here are the properties that you own")
    print("=================================================")
    print("Property Name\tCost\tHouses\tHotels")
    for i in len(player.owned_properties):
        print("{}) {}".format(i,player.owned_properties[i]))
    choice = input("Would you like build on one of these properties (y/n)? ")
    if choice in ["yes","y","okay","sure","yup"]:
        choice = input("Which property would you like to improve? ")
        selected_prop = player.owned_properties[choice]
        #Continue asking
        if not selected_prop.is_consolidated:
            print("You cannot build improvements on this property until you've bought all of the properties in the color group")
        else:
            print("Okay, choose from the options below to make an improvement: ")
            print("1) Build a house")
            print("2) Build a hotel")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                player.purchase_house(selected_prop)
            elif choice == 2:
                player.purchase_hotel(selected_prop)
    else:
        print("Okay, let's continue with your current turn")

def run_player_turn(current_player):
    global current_player_index, is_game_over
    roll_again = False
   
    if current_player.in_jail:
        print("You are still in jail.")
        if current_player.exit_jail_cards > 0:
            choice = input("You have a get out of jail free card.  Would you like to use it (y/n)? ").lower()
            if choice in ["y","yes","yeah","yup"]:
                current_player.exit_jail_cards -= 1
                current_player.in_jail = False
                print("You used one of your get out of jail free cards. Congratulations, you're out of the slammer")
                run_player_turn()
                return
        else:
            current_player.jail_wait_turns += 1
            if current_player.jail_wait_turns > 2:
                print("However, you've done your time.  You're free to leave jail now")
                run_player_turn()
                return
            print("You've waited {} turns while in jail".format(current_player.jail_wait_turns))
    else:

        if current_player.can_make_improvements():
            choice = input("Do you wish to make improvements (y/n)?").lower()
            if choice in ["yes","y","yeah","yup","sure","okay"]:
                make_improvements(current_player)

        die1 = random.randint(2, 6)
        die2 = random.randint(2, 6)
        current_location_index = current_player.location
        new_location_index = (current_location_index + die1 + die2) % len(board_manager.board)

        #check if passed go
        if current_location_index + die1 + die2 > len(board_manager.board):
            #player has passed go
            current_player.receive_money(200)
            print("You passed go and collected $200.  You now have ${}".format(current_player.money))
        elif current_location_index == 0 and new_location_index > 0:
            #player is already on go but hasn't passed it yet
            current_player.receive_money(200)
            print("You passed go and collected $200.  You now have ${}".format(current_player.money))

        time.sleep(1)


        current_player.location = new_location_index
        new_location = board_manager.board[new_location_index]

        if new_location.is_property:
            print(new_location.get_message())
            if new_location.is_owned:
                if current_player.has_property(new_location.name):
                    print("You already own this property.".format(new_location.name))
                else:
                    for player in players:
                        if player.id == new_location.owner_id:
                            property_owner = player
                    rent_amount = new_location.get_rent()
                    property_owner.receive_money(rent_amount)
                    current_player.pay_money(rent_amount)
                    print("This property is owned by {}.  You paid ${} to the owner".format(
                        new_location.name,property_owner.name,rent_amount
                    ))
                    check_player_elimination(current_player)
            else:
                print("This property ({}) is not owned by anyone.".format(new_location.get_name()))
                choice = input("Do you wish to buy this property (y/n)?")
                if choice.lower() in ["yes","y","yeah","yup"]:
                    if current_player.money >= new_location.cost:
                        current_player.pay_money(new_location.cost)
                        current_player.owned_properties.append(new_location)
                        new_location.owner_id = current_player.id
                        print("You just purchased {} for ${}.  You now have ${} left".format(
                            new_location.name,
                            new_location.cost,
                            current_player.money
                        ))
                    else:
                        print("You do not have enough money to afford this property")
                else:
                    print("You decided not to purchase the property")


        elif new_location.is_tax:
            print(new_location.get_message())
            current_player.pay_money(new_location.get_fee_amount())
            print("Player {} (i.e. {}) currently has ${}".format(current_player.id,
                                                                 current_player.name,
                                                                current_player.money))
            check_player_elimination(current_player)
        elif new_location.is_utility:
            print(new_location.get_message())
            current_player.pay_money(new_location.get_fee_amount())
            print("Player {} (i.e. {}) currently has ${}".format(current_player.id,
                                                                 current_player.name,
                                                                 current_player.money))
            check_player_elimination(current_player)
        elif new_location.is_go:
            print(new_location.get_message())
        elif new_location.is_community_chest:
            pass
        elif new_location.is_chance:
            pass
        elif new_location.is_free_parking:
            print(new_location.get_message())
        elif new_location.is_visiting_jail:
            print(new_location.get_message())
        elif new_location.is_goto_jail:
            print(new_location.get_message())

        if die1 == die2:
            roll_again = True

        if len(players) <= 1:
            is_game_over = True
            return

        if roll_again:
            run_player_turn(players[current_player_index])



def run_computerAI_turn(current_player):
    global current_player_index, is_game_over
    roll_again = False

    current_location_index = current_player_index

    if current_player.in_jail:
        print("{} is still in jail.".format(current_player.name))
        if current_player.exit_jail_cards > 0:
            current_player.exit_jail_cards -= 1
            current_player.in_jail = False
            print("{} used one of their get out of jail free cards. They're now out of the slammer".format(current_player.name))
            run_computerAI_turn()
            return
        else:
            current_player.jail_wait_turns += 1
            if current_player.jail_wait_turns > 2:
                print("However, they've done their time.  They're now free to leave jail")
                run_computerAI_turn()
                return
            print("{} has waited {} turns while in jail".format(current_player.name,current_player.jail_wait_turns))
    else:

        # Check if computer has the available funds to make improvements
        # Get a random number to decide whether or not improvements will be made
            # Probability can be proportional to the amount of funds available and assets
            # Refactor player class to include functions that assess the total value of all combined properties, improvements, and money
            # Refactor Player class so that it derives common attributes and functionality from some base class in common with another derived class, ComputerAI
            # The computerAI class could have variables for adjusting willing to take risk and spend aggressively
            # ComputerAI chooses a property randomly or according to some inherent characteristic, such as a preference for luxury properties
            #use another version of the make_improvements function (current_player)

        die1 = random.randint(2, 6)
        die2 = random.randint(2, 6)

        new_location_index = (current_location_index + die1 + die2) % len(board_manager.board)

        #check if passed go
        if current_location_index + die1 + die2 > len(board_manager.board):
            #player has passed go
            current_player.receive_money(200)
            print("{} passed go and collected $200.  {} now has ${}".format(current_player.name,current_player.name,current_player.money))
        elif current_location_index == 0 and new_location_index > 0:
            #player is already on go but hasn't passed it yet
            current_player.receive_money(200)
            print("{} passed go and collected $200.  {} now have ${}".format(current_player.name,current_player.name,current_player.money))

        time.sleep(1)

        current_player.location = new_location_index
        new_location = board_manager.board[new_location_index]

        if new_location.is_property:
            print(new_location.get_message())
            if new_location.is_owned:
                if current_player.has_property(new_location.name):
                    print("{} already own this property.".format(current_player.name,new_location.name))
                else:
                    for player in players:
                        if player.id == new_location.owner_id:
                            property_owner = player
                    rent_amount = new_location.get_rent()
                    property_owner.receive_money(rent_amount)
                    current_player.pay_money(rent_amount)
                    print("This property is owned by {}.  {} paid ${} to the owner".format(
                        new_location.name,current_player.name,property_owner.name,rent_amount
                    ))
                    check_player_elimination(current_player)
            else:
                print("This property is not owned by anyone.".format(new_location.name))
                choice = random.random()
                if choice < 0.5:

                    if current_player.money >= new_location.cost:
                        current_player.pay_money(new_location.cost)
                        current_player.owned_properties.append(new_location)
                        new_location.owner_id = current_player.id
                        print("You just purchased {} for ${}.  You now have ${} left".format(
                            new_location.name,
                            new_location.cost,
                            current_player.money
                        ))
                    else:
                        print("{} does not have enough money to afford this property".format(current_player.name))
                else:
                    print("{} decided not to purchase the property".format(current_player.name))


        elif new_location.is_tax:
            print(new_location.get_message())
            current_player.pay_money(new_location.get_fee_amount())
            print("Player {} (i.e. {}) currently has ${}".format(current_player.id,
                                                                 current_player.name,
                                                                current_player.money))
            check_player_elimination(current_player)
        elif new_location.is_utility:
            print(new_location.get_message())
            current_player.pay_money(new_location.get_fee_amount())
            print("Player {} (i.e. {}) currently has ${}".format(current_player.id,
                                                                 current_player.name,
                                                                 current_player.money))
            check_player_elimination(current_player)
        elif new_location.is_go:
            print(new_location.get_message())
        elif new_location.is_community_chest:
            pass
        elif new_location.is_chance:
            pass
        elif new_location.is_free_parking:
            print(new_location.get_message())
        elif new_location.is_visiting_jail:
            print(new_location.get_message())
        elif new_location.is_goto_jail:
            print(new_location.get_message())

        if die1 == die2:
            roll_again = True

        if len(players) <= 1:
            is_game_over = True
            return

        if roll_again:
            run_player_turn(current_player_index)

def get_next_player():
    global current_player_index
    current_player_index += 1
    if current_player_index >= len(players):
        current_player_index = 0

def play_game():
    global is_game_over
    initialize_players(600)
    print("================= Let's Play Monopoly! ====================")

    while not is_game_over:
        current_player = players[current_player_index]
        print("It is {} (i.e. Player {})'s turn. ".format(current_player.name,current_player.id))
        time.sleep(1)
        current_player = players[current_player_index]
        if current_player.is_computer:
            run_computerAI_turn(current_player)
        else:
            run_player_turn(current_player)
        get_next_player()


    winner = players[0]
    print("The winner is {} with a total of ${}".format(winner.name,winner.money))



# Press the green button in the gutter to run the script.
def main():
    global is_game_over
    user_choice = "y"
    while user_choice == "y":
        play_game()
        print("===================================================")
        user_choice = input("Do you want to play again (y/n)? ").lower()
        valid = False
        while not valid:
            if user_choice in ["y","yes","yeah","yup","n","no","nope","naw"]:
                valid = True 
            else:
                print("Invalid choice.  Please type 'y' to continue or 'n' to stop")
    
        if user_choice in ["y","yes","yeah","yup"]:
            is_game_over = False
            initialize_players(600)
            board_manager.reset_board()
        elif user_choice in ["n","no","nope","naw"]:
            break 
    
    print("Thanks for playing Monopoly!")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == "__main__":
    main()



