def imageCheck(card1,card2,points):
    if card1.getCardImage() != card2.getCardImage():
        card1.setClicked(False)
        card2.setClicked(False)
        points = 0
    else:
        points = 1
    return [card1,card2,points]
