
#Will compare front image file names to see if they are the same
def isMatching(card1, card2):

        if(card1.front==card2.front):
            return True

        else:
            return False


#If game is finished - will see if all cards have been revealed
def isFinished(cardList):

    for card in cardList:

        if card.revealed==False:
            return False

    return True
