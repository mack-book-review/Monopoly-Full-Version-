from property_configuration import PropertyConfiguration
from property import Property
from fee import Tax,Utility
from placeholder import Go,CommunityChest,Chance,VisitingJail,GoToJail,FreeParking
from community_card import CommunityCard,ChanceCard
from constants import * 

class BoardManager():

    PROPERTY_NAMES = [
        MEDITERRANEAN_AV,
        BALTIC_AV,
        ORIENTAL_AV,
        VERMONT_AV,
        CONNECTICUT_AV,
        ST_CHARLES_PLACE,
        STATES_AV,
        VIRGINIA_AV,
        ST_JAMES_PLACE,
        TENNESSEE_AV,
        NEW_YORK_AV,
        KENTUCKY_AV,
        INDIANA_AV,
        ILLINOIS_AV,
        ATLANTIC_AV,
        VENTNOR_AV,
        MARVIN_GARDENS,
        PACIFIC_AV,
        NORTH_CAROLINA_AV,
        PENNSYLVANIA_AV,
        PARK_PLACE,
        BOARDWALK
        ]


    def __init__(self):
        self.board = []
        self.community_cards = []
        self.chance_cards = []
        self.property_info = {}
        self.configure_properties()
        self.configure_board()

    def get_board(self):
        return self.board

    def configure_board(self):
        self.board = [
            Go(),
            self.get_property_space(MEDITERRANEAN_AV),
            CommunityChest(),
            self.get_property_space(BALTIC_AV),
            Tax("Income Tax", 200),
            self.get_property_space(ORIENTAL_AV),
            Chance(),
            self.get_property_space(VERMONT_AV),
            self.get_property_space(CONNECTICUT_AV),
            VisitingJail(),
            FreeParking(),
            GoToJail(),
        ]



    def get_property_space(self,name):
        property_config = self.property_info[name]
        return Property(property_config)

    def configure_community_cards(self):
        self.community_cards.append(CommunityCard("Pay Hospital $100", 100, {}))


    def configure_chance_cards(self):
        pass

    def configure_properties(self):
        for name in BoardManager.PROPERTY_NAMES:
            prop_config = None
            if name == MEDITERRANEAN_AV:
                # prop config -> PropertyConfiguration(name,group_color,cost,base_rent,mortgage_value,...)
                prop_config = PropertyConfiguration(name,"brown",60,2,50,50,30,10,30,90,160,250)
            elif name == BALTIC_AV:
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == ORIENTAL_AV:
                prop_config = PropertyConfiguration(name,"lightblue",60,4,50,50,30,20,60,180,320,450)
            elif name == VERMONT_AV:
                prop_config = PropertyConfiguration(name,"lightblue",60,4,50,50,30,20,60,180,320,450)
            elif name == CONNECTICUT_AV:
                prop_config = PropertyConfiguration(name,"lightblue",60,4,50,50,30,20,60,180,320,450)
            elif name == ST_CHARLES_PLACE:
                prop_config = PropertyConfiguration(name,"orange",60,4,50,50,30,20,60,180,320,450)
            elif name == STATES_AV:
                prop_config = PropertyConfiguration(name,"orange",60,4,50,50,30,20,60,180,320,450)
            elif name == VIRGINIA_AV:
                prop_config = PropertyConfiguration(name,"orange",60,4,50,50,30,20,60,180,320,450)
            elif name ==  ST_JAMES_PLACE:
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == TENNESSEE_AV:
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == NEW_YORK_AV:
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == KENTUCKY_AV:
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == INDIANA_AV:
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == ILLINOIS_AV:
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == ATLANTIC_AV:
                prop_config = PropertyConfiguration(name,"yellow",60,4,50,50,30,20,60,180,320,450)
            elif name == VENTNOR_AV:
                prop_config = PropertyConfiguration(name,"yellow",60,4,50,50,30,20,60,180,320,450)
            elif name == MARVIN_GARDENS:
                prop_config = PropertyConfiguration(name,"yellow",60,4,50,50,30,20,60,180,320,450)
            elif name == PACIFIC_AV:
                prop_config = PropertyConfiguration(name,"green",60,4,50,50,30,20,60,180,320,450)
            elif name == NORTH_CAROLINA_AV:
                prop_config = PropertyConfiguration(name,"green",60,4,50,50,30,20,60,180,320,450)
            elif name == PENNSYLVANIA_AV:
                prop_config = PropertyConfiguration(name,"green",60,4,50,50,30,20,60,180,320,450)
            elif name == PARK_PLACE:
                prop_config = PropertyConfiguration(name,"darkblue",60,4,50,50,30,20,60,180,320,450)
            elif name == BOARDWALK:
                prop_config = PropertyConfiguration(name,"darkblue",60,4,50,50,30,20,60,180,320,450)


           
            self.property_info[name] = prop_config

    def reset_board(self):
        for space in self.board:
            if space.is_property:
                space.is_owned = False
                space.owner_id = -1
                space.number_houses = 0
                space.number_hotels = 0

