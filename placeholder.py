from board_space import BoardSpace

class CommunityChest(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_community_chest = True
    
    def get_message(self,player_name):
        return "{} landed on a Community Chest".format(player_name)


class Chance(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_chance = True
        
    def get_message(self,player_name):
        return "{} landed on a Chance".format(player_name)

class Go(BoardSpace):

    def __init__(self):
        super().__init__()
        self.is_go = True

    def get_message(self,player_name):
        return "{} landed on Go".format(player_name)

class VisitingJail(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_visiting_jail = True

    def get_message(self,player_name):
        return "{} is at the jailhouse just visiting".format(player_name)

class GoToJail(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_goto_jail = True

    def get_message(self,player_name):
        return "You are out of luck, {}! Go to Jail!".format(player_name)

class FreeParking(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_free_parking = True

    def get_message(self,player_name):
        return "{} landed on the free parking area".format(player_name)
