
#Will compare front image file names to see if they are the same
def isMatching(card1, card2):
    '''
    This function tests whether the two cards that were clicked are matching or not, if they are it will return True, otherwise it will return False
    param list: card1, card2
    returns: True or False
    '''
    if(card1.front==card2.front):
        return True

    else:
        return False


#If game is finished - will see if all cards have been revealed
def isFinished(cardList):
    '''
    This function checks to see if the game has been completed by testing if all of the cards have been revealed.
    param list: cardList
    returns: True or False
    '''
    for card in cardList:

        if card.revealed==False:
            return False

    return True
