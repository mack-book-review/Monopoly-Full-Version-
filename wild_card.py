

class WildCard():
    def __init__(self,description,amount, **kwargs):

        self.is_community_card = False
        self.is_chance_card = False

        #Accounts for most community cards, which are either expenditures or revenues
        self.description = description
        self.amount = amount

        #Accounts for most community cards, which are either expenditures or revenues
        self.is_expenditure = kwargs["is_expenditure"]
        self.is_revenue = kwargs["is_revenue"]

        #Mainly for special community cards
        self.is_collect_from_every_player = kwargs["is_collect_from_every_player"]
        self.is_advance_to_go = kwargs["is_advance_to_go"]
        self.is_property_dependent = kwargs["is_property_dependent"]
        self.per_house_fee = kwargs["per_house_fee"]
        self.per_hotel_fee = kwargs["per_hotel_fee"]

