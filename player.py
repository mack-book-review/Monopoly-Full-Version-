
class Player():


    def __init__(self,name,id,is_computer = False):
        self.is_computer = is_computer
        self.name = name
        self.id = id
        self.money = 500
        self.location = 0
        self.is_first_turn = True

        self.owned_properties = []
        self.prop_info = {
            "brown": 0,
            "lightblue": 0,
            "magenta": 0,
            "orange": 0,
            "red": 0,
            "yellow": 0,
            "green": 0,
            "darkblue": 0
        }

        self.in_jail = False
        self.jail_wait_turns = 0
        self.exit_jail_cards = 0

    def purchase_hotel(self,property):
        property_set = self.get_property_set(property.get_group_color())

        min_index = 0
        min_hotels = property_set[0].number_hotels

        for i in range(len(property_set) - 1, 0, -1):
            number_hotels = property_set[i].number_hotels
            if number_hotels <= min_hotels:
                min_hotels = number_hotels
                min_index = i

        to_build_property = property_set[min_index]
        if self.money >= to_build_property.get_cost_of_hotel():
            self.pay_money(to_build_property.get_cost_of_hotel())
            to_build_property.purchase_hotel()
        else:
            print("Sorry, you don't have enough money to build a hotel on this property")

    def purchase_house(self,property):
        property_set = self.get_property_set(property.get_group_color())

        min_houses_index = 0
        min_houses = property_set[0].number_houses

        for i in range(len(property_set)-1,0,-1):
            number_houses = property_set[i].number_houses
            if number_houses <= min_houses:
                min_houses = number_houses
                min_index = i

        if min_houses == 4:
            print("You can't build any more houses.  You are out of room for houses.")
        else:
            to_build_property = property_set[min_houses]
            if self.money >= to_build_property.get_cost_of_house():
                self.pay_money(to_build_property.get_cost_of_house())
                to_build_property.purchase_house()
            else:
                print("Sorry, you don't have enough money to build a house on this property")


    def get_property_set(self,group_color):
        return [property for property in self.owned_properties if property.get_group_color() == group_color]

    def has_consolidated_property(self):
        return len([prop for prop in self.owned_properties if prop.is_consolidated]) > 0

    def purchase_property(self,property):
        property.is_owned = True
        self.money -= property.cost
        self.owned_properties.append(property)
        self.prop_info[property.get_group_color()] += 1

        #check if the user has purchased entire color group.  If so, set 'is_consolidated' to True on each property
        #belonging to the group
        if self.prop_info["brown"] == 2:
            prop_group = [property for property in self.owned_properties if property.group_color == "brown"]
            for prop in prop_group:
                prop.is_consolidated = True
        elif self.prop_info["darkblue"] == 2:
            prop_group = [property for property in self.owned_properties if property.group_color == "darkblue"]
            for prop in prop_group:
                prop.is_consolidated = True
        else:
            for color_group, prop_number in self.prop_info.items():
                if prop_number == 3:
                    prop_group = [property for property in self.owned_properties if property.group_color == color_group]
                    for prop in prop_group:
                        prop.is_consolidated = True

    def has_property(self,property):
        return property in self.owned_properties

    def receive_money(self,amount):
        self.money += amount

    def pay_money(self,amount):
        self.money -= amount
    

    def can_make_improvements(self):
        return self.has_consolidated_property()