from board_space import BoardSpace
from  property_configuration import PropertyConfiguration

class Property(BoardSpace):

    def __init__(self,property_configuration):
        super().__init__()

        # designate this boardspace as a property
        self.is_property = True

        # these variables can change in the course of gameplay
        self.is_consolidated = False
        self.is_owned = False
        self.owner_id = -1
        self.number_houses = 0
        self.number_hotels = 0

        # property configuration defines essential characteristics of a given property
        self.property_configuration = property_configuration

    def sell_to_player(self,player):
        self.is_owned = True
        self.owner_id = player.id

    def has_improvements(self):
        return self.number_hotels > 0 or self.number_houses > 0

    def get_name(self):
        return self.property_configuration.name

    def get_cost(self):
        return self.property_configuration.cost

    def get_base_rent(self):
        return self.property_configuration.base_rent

    def get_group_color(self):
        return self.property_configuration.group_color

    def get_mortgage_value(self):
        return self.property_configuration.mortgage_value

    def get_cost_of_hotel(self):
        return self.property_configuration.cost_of_hotel

    def get_cost_of_house(self):
        return self.property_configuration.cost_of_house

    def get_rent_for_number_of_houses(self,number_of_houses):
        if number_of_houses == 1:
            return self.property_configuration.rent_1house
        elif number_of_houses == 2:
            return self.property_configuration.rent_2house
        elif number_of_houses == 3:
            return self.property_configuration.rent_3house
        elif number_of_houses == 4:
            return self.property_configuration.rent_4house

    def get_rent_for_hotel(self):
        return self.property_configuration.rent_1hotel


    def get_rent(self):
        #calculate rent based on umber of houses and hotels
        adjusted_rent = self.get_base_rent()
        if self.is_consolidated and not self.has_improvements():
            adjusted_rent *= 2
            return adjusted_rent
        elif not self.is_consolidated and not self.has_improvements():
            return adjusted_rent
        else:
            if self.number_houses > 0:
                adjusted_rent = self.get_rent_for_number_of_houses(self.number_houses)

            if self.number_hotels > 0:
                adjusted_rent = self.get_rent_for_hotel()

            return adjusted_rent


    def purchase_house(self):
        self.number_houses += 1

    def purchase_hotel(self):
        self.number_houses -= 4
        self.number_hotels += 1

    def get_message(self):
        return "You landed on {}".format(self.get_name())

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(self.get_name(),self.get_cost(),self.number_houses,self.number_hotels)