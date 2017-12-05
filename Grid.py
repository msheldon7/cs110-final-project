
#Constructs grid object of certain dimensions depending on number of cards
class Grid:

    def __init__(self, num_cards, card_list):

        self.cards=num_cards

        self.x=6
        self.y=4

        grid_list=[]
        for i in range(self.y):
            grid_list.append([])
            #accessed wiht grid_list[r][c]
            #length of grid_list {self.y} is the number of rows in grid
            #length of grid_list's internal lists {self.x} is num of columns

        i=0
        #Adds cards in card_list to 2D grid_list
        for r in range(self.y):
            for c in range(self.x):
                grid_list[r][c]=card_list[i]
                i+=1

            


class GridSquare:

    def __init__(self, xcoor, ycoor, occupy_state):

        self.x=xcoor
        self.y=ycoor
