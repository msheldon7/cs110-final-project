
import random

#Constructs card object with attributes: front and back images, revealed
class Card:

    def __init__(self, screen, coordinates, front_image_file):

        self.front=str(front_image_file)
        self.back='Back.png'

        self.revealed=False
        
        self.size=(160,160)
        self.screen = screen
        self.coordinates = coordinates
        self.background = False
        self.clicked = False

    def getCoordinates(self):
        return self.coordinates

    def getSize(self):
        return self.size()

    def getClicked(self, clicked):
        return self.clicked

    def getFront_image_file(self):
        return self.front

    def setBackground(self, background):
        self.background = background

    def setOver(self, over):
        self.over = over

    def setFront_image_file(self, front_image_file):
        self.front = front_image_file

    def drawButton(self):
        self.screen.blit(self.background, self.coordinates)

    def drawButtonActive(self):
        self.screen.blit(self.over, self.coordinates)

    def drawCardImage(self):
        self.screen.blit(self.front_image_file, self.coordinates)
        pygame.display.update()

    def __str__(self):

        return str(self.front)


def createCardList(num_cards, gameDisplay):

    picture_list1=['Penguin.png','Snowflake.png','Tree.png','GingerbreadMan.png','NorthPole.png','Star.png','Sleigh.png','Reindeer.png','Owl.png','Stocking.png','Snowman.png','Bells.png','Penguin.png','Snowflake.png','Tree.png','GingerbreadMan.png','NorthPole.png','Star.png','Sleigh.png','Reindeer.png','Owl.png','Stocking.png','Snowman.png','Bells.png']
    picture_list2=random.sample(picture_list1,num_cards)
    #List2 (length=24) contains 2 of each of 12 pictures in a random order

    cardlist=[]
    for i in range(num_cards):

        if i<6:
            loc=( (i*160)+2, 2)
        elif i<12:
            loc=( ((i-6)*160)+4, 164)
        elif i<18:
            loc=( ((i-12)*160)+6, 326)
        else:
            loc=( ((i-18)*160)+8, 488)
            
        cardlist.append(Card(gameDisplay, loc, picture_list2[i]))
        #Adds card to list with corresponding png in list2

    return cardlist
