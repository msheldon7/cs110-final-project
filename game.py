
#If game is finished - will see if all cards have been revealed
def isFinished(cardList):

    for card in cardList:

        if card.revealed==False:
            return False

    return True
