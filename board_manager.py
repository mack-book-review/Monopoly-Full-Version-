from property_configuration import PropertyConfiguration
from property import Property
from fee import Tax,Utility
from placeholder import Go,CommunityChest,Chance,VisitingJail,GoToJail,FreeParking
from community_card import CommunityCard,ChanceCard

class BoardManager():

    PROPERTY_NAMES = [
        "Mediterranean Avenue",
        "Baltic Avenue",
        "Oriental Avenue",
        "Vermont Avenue",
        "Connecticut Avenue",
        "St. Charles Place",
        "States Avenue",
        "Virginia Avenue",
        "St. James Place",
        "Tennessee Avenue",
        "New York Avenue",
        "Kentucky Avenue",
        "Indiana Avenue",
        "Illinois Avenue",
        "Atlantic Avenue",
        "Ventnor Avenue",
        "Marvin Gardens",
        "Pacific Avenue",
        "North Carolina Avenue",
        "Pennsylvania Avenue",
        "Park Place",
        "Boardwalk"]


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
            self.get_property_space("Mediterranean Avenue"),
            CommunityChest(),
            self.get_property_space("Baltic Avenue"),
            Tax("Income Tax", 200),
            self.get_property_space("Reading Railroad"),
            self.get_property_space("Oriental Avenue"),
            Chance(),
            self.get_property_space("Vermont Avenue"),
            self.get_property_space("Connecticut Avenue"),
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
            if name == "Mediterranean Avenue":
                # prop config -> PropertyConfiguration(name,group_color,cost,base_rent,mortgage_value,...)
                prop_config = PropertyConfiguration(name,"brown",60,2,50,50,30,10,30,90,160,250)
            elif name == "Baltic Avenue":
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == "Oriental Avenue":
                prop_config = PropertyConfiguration(name,"lightblue",60,4,50,50,30,20,60,180,320,450)
            elif name == "Vermont Avenue":
                prop_config = PropertyConfiguration(name,"lightblue",60,4,50,50,30,20,60,180,320,450)
            elif name == "Connecticut Avenue":
                prop_config = PropertyConfiguration(name,"lightblue",60,4,50,50,30,20,60,180,320,450)
            elif name == "St. Charles Place":
                prop_config = PropertyConfiguration(name,"orange",60,4,50,50,30,20,60,180,320,450)
            elif name == "States Avenue":
                prop_config = PropertyConfiguration(name,"orange",60,4,50,50,30,20,60,180,320,450)
            elif name == "Virginia Avenue":
                prop_config = PropertyConfiguration(name,"orange",60,4,50,50,30,20,60,180,320,450)
            elif name == "St. James Place":
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == "Tennessee Avenue":
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == "New York Avenue":
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == "Kentucky Avenue":
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == "Indiana Avenue":
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == "Illinois Avenue":
                prop_config = PropertyConfiguration(name,"brown",60,4,50,50,30,20,60,180,320,450)
            elif name == "Atlantic Avenue":
                prop_config = PropertyConfiguration(name,"yellow",60,4,50,50,30,20,60,180,320,450)
            elif name == "Ventnor Avenue":
                prop_config = PropertyConfiguration(name,"yellow",60,4,50,50,30,20,60,180,320,450)
            elif name == "Marvins Garden":
                prop_config = PropertyConfiguration(name,"yellow",60,4,50,50,30,20,60,180,320,450)
            elif name == "Pacific Avenue":
                prop_config = PropertyConfiguration(name,"green",60,4,50,50,30,20,60,180,320,450)
            elif name == "North Caroliona Avenue":
                prop_config = PropertyConfiguration(name,"green",60,4,50,50,30,20,60,180,320,450)
            elif name == "Pennsylvania Avenue":
                prop_config = PropertyConfiguration(name,"green",60,4,50,50,30,20,60,180,320,450)
            elif name == "Park Place":
                prop_config = PropertyConfiguration(name,"darkblue",60,4,50,50,30,20,60,180,320,450)
            elif name == "Boardwalk":
                prop_config = PropertyConfiguration(name,"darkblue",60,4,50,50,30,20,60,180,320,450)

            property = Property(prop_config)
            self.property_info[name] = property

    def reset_board(self):
        for space in self.board:
            if space.is_property:
                space.is_owned = False
                space.owner_id = -1
                space.number_houses = 0
                space.number_hotels = 0

