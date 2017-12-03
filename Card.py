
import random

#Constructs card object with attributes: front and back images, revealed
class Card:

    def __init__(self, front_image_file):

        self.front=str(front_image_file)
        self.back='Back.png'
        
        self.revealed=False


    def __str__(self):

        return str(self.front)


def createCardList(num_cards):

    picture_list1=['Penguin.png','Snowflake.png','Tree.png','GingerbreadMan.png','NorthPole.png','Star.png','Sleigh.png','Reindeer.png','Owl.png','Stocking.png','Snowman.png','Bells.png','Santa.png','Present.png','Mistletoe.png','Elf.png','Candycane.png','GingerbreadGirl.png','Ornament.png','Wreath.png','Penguin.png','Snowflake.png','Tree.png','GingerbreadMan.png','NorthPole.png','Star.png','Sleigh.png','Reindeer.png','Owl.png','Stocking.png','Snowman.png','Bells.png','Santa.png','Present.png','Mistletoe.png','Elf.png','Candycane.png','GingerbreadGirl.png','Ornament.png','Wreath.png']
    picture_list2=random.sample(picture_list1,num_cards)
    #List2 (length=40) contains 2 of each of 20 pictures in a random order 

    cardlist=[]
    for i in range(num_cards):
        cardlist.append(Card(picture_list2[i]))
        #Adds card to list with corresponding png in list2

    return cardlist
