from wild_card import WildCard

class CommunityCard(WildCard):
    def __init__(self,description,amount, **kwargs):
        super().__init__(description,amount,kwargs)
        self.is_community_card = True

class ChanceCard(WildCard):
    def __init__(self,description,amount, **kwargs):
        super().__init__(description,amount,kwargs)
        self.is_chance_card = True

