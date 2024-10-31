class Phone:
    def __init__(self,color=None,cost=None):
        self.color = color
        self.cost = cost


    def set_color(self,color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost

    def make_call(self):
        print("Making phone call")

    def play_game(self):
        print("Playing game")

