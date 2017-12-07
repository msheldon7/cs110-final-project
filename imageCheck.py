def imageCheck(card1,card2,points):
    '''
    This function checks  if the cards are matching or not and returns the outcome.
    param list: card1, card2, points
    returns: array of card1, card2, and points
    '''
    if card1.getFront_image_file() != card2.getFront_image_file():
        card1.setClicked(False)
        card2.setClicked(False)
        points = 0
    else:
        points = 1
    return [card1,card2,points]
