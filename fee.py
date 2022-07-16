from board_space import BoardSpace

class Fee(BoardSpace):
    def __init__(self, name, amount):
        super().__init__()
        self.name = name
        self.amount = amount

    def get_fee_amount(self):
        return self.amount

    def get_name(self):
        return self.name

    def get_message(self):
        return "You must pay a {} of ${}".format(self.name,self.amount)

class Tax(Fee):
    def __init__(self,name,amount):
        super().__init__(name,amount)
        self.is_tax = True


class Utility(Fee):
    def __init__(self,name,amount):
        super().__init__(name,amount)
        self.is_utility = True
