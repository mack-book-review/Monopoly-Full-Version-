from board_space import BoardSpace

class CommunityChest(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_community_chest = True
    
    def get_message(self):
        return "You landed on a Community Chest"


class Chance(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_chance = True
        
    def get_message(self):
        return "You landed on a Chance"

class Go(BoardSpace):

    def __init__(self):
        super().__init__()
        self.is_go = True

    def get_message(self):
        return "You landed on Go"

class VisitingJail(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_visiting_jail = True

    def get_message(self):
        return "You are at the jailhouse just visiting"

class GoToJail(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_goto_jail = True

    def get_message(self):
        return "GO to Jail!"

class FreeParking(BoardSpace):
    def __init__(self):
        super().__init__()
        self.is_free_parking = True

    def get_message(self):
        return "You are on the free parking area"



