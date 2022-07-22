from player import Player
import random

class PlayerManager():

    def __init__(self):
        self.available_players = [
            Player("Michael Anderson", 1),
            Player("AI Bill", 2,True)
        ]

        self.players = []
        self.current_player_index = 0

    def initialize_players(self, starting_money):
        self.players.clear()
        for player in self.available_players:
            player.location = 0
            player.in_jail = False
            player.jail_wait_turns = 0
            player.owned_properties = []
            player.money = starting_money
            player.is_first_turn = True
            self.players.append(player)

        self.current_player_index = random.randint(0, len(self.players) - 1)

    def get_next_player(self):
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0

    def check_player_elimination(self,player):
        if player.money < 0:
            print("Player {} is out of money and has been eliminated".format(player.name))
            self.players.remove(player)
