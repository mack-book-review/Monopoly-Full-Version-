from player import Player
from constants import *
import random

class PlayerManager():

    def __init__(self):
        self.available_players = []
        self.get_available_players()
        self.players = []
        self.current_player_index = 0

    def get_available_players(self):
        choice = input("Do you want to enter players manually (y/n)?")
        if choice in VALID_AFFIRMATIVES:
            num_players = int(input("How many people are going to play? "))
            for i in range(num_players):
                player_name = input("What is the name of Player {}?".format(i+1))
                player_type = int(input("Is this player (1) a human or (2) an AI? "))
                new_player = Player(player_name,i+1,player_type-1)
                self.available_players.append(new_player)
        else:
            print("Getting default players....")
            self.available_players = [
                Player("User", 1),
                Player("AI Opponent", 2, True)
            ]

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
