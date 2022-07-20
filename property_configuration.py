
class PropertyConfiguration():

    def __init__(self,
                 name,
                 group_color,
                 cost,
                 base_rent,
                 cost_of_house,
                 cost_of_hotel,
                 mortgage_value,
                 rent_1house,
                 rent_2house,
                 rent_3house,
                 rent_4house,
                 rent_1hotel):

        #basic information
        self.name = name
        self.group_color = group_color
        self.cost = cost

        #base rent
        self.base_rent = base_rent

        #adjusted rent for improvements
        self.rent_1house = rent_1house
        self.rent_2house = rent_2house
        self.rent_3house = rent_3house
        self.rent_4house = rent_4house
        self.rent_1hotel = rent_1hotel

        #mortgage value
        self.mortgage_value = mortgage_value

        #cost of improvements
        self.cost_of_house = cost_of_house
        self.cose_of_hotel = cost_of_hotel

