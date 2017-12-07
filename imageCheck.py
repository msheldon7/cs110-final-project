def imageCheck(card1,card2,points):
    if card1.getFront_image_file() != card2.getFront_image_file():
        card1.setClicked(False)
        card2.setClicked(False)
        points = 0
    else:
        points = 1
    return [card1,card2,points]
