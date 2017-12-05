
import random

#Constructs card object with attributes: front and back images, revealed
class Card:

    def __init__(self, screen, coordinates, size, background, over, front_image_file, clicked):

        self.front=str(front_image_file)
        self.back='Back.png'

        self.revealed=False
        self.screen = screen
        self.coordinates = coordinates
        self.over = over
        self.background = background
        self.clicked = clicked

    def getCoordinates(self):
        return self.coordinates

    def getSize(self):
        return self.size():

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


def createCardList(num_cards):

    picture_list1=['Penguin.png','Snowflake.png','Tree.png','GingerbreadMan.png','NorthPole.png','Star.png','Sleigh.png','Reindeer.png','Owl.png','Stocking.png','Snowman.png','Bells.png','Penguin.png','Snowflake.png','Tree.png','GingerbreadMan.png','NorthPole.png','Star.png','Sleigh.png','Reindeer.png','Owl.png','Stocking.png','Snowman.png','Bells.png']
    picture_list2=random.sample(picture_list1,num_cards)
    #List2 (length=24) contains 2 of each of 12 pictures in a random order

    cardlist=[]
    for i in range(num_cards):
        cardlist.append(Card(picture_list2[i]))
        #Adds card to list with corresponding png in list2

    return cardlist
