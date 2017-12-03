
#Constructs grid object of certain dimensions depending on number of cards
class Grid:

    def __init__(self, num_cards):

        self.cards=num_cards


        if num_cards==20:
            self.x=5
            self.y=4
        elif num_cards==40:
            self.x=8
            self.y=5
        elif num_cards==60:
            self.x=6
            self.y=10

        grid_list=[]
        for i in range(self.y):
            grid_list.append([])
            #accessed wiht grid_list[r][c]
            #length of grid_list {self.y} is the number of rows in grid
            #length of grid_list internal lists {self.x} is num of columns


class GridSquare:

    def __init__(self, xcoor, ycoor, occupy_state):

        self.x=xcoor
        self.y=ycoor
        self.occupied=occupy_state#Boolean value - will be used when placing cards
