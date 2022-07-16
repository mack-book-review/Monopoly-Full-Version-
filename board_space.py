
class BoardSpace():

    def __init__(self):
        self.is_property = False
        self.is_tax = False
        self.is_utility = False
        self.is_community_chest = False
        self.is_goto_jail = False
        self.is_visiting_jail = False
        self.is_chance = False
        self.is_free_parking = False
        self.is_go = False

    def get_message(self):
        return ""