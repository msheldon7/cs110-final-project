
import Card
import Grid
import evaluate

import pygame


pygame.init()
pygame.display.set_caption('Winter Matching Game')
#clock=pygame.time.clock()

x=800
y=600

display_window=pygame.display.set_mode((x,y))

game_finish=False

answer=24
cardlist=Card.createCardList(answer)
table=Grid.Grid(answer,cardlist)

click_counter=0

#Main game Loop
while not game_finish:

    #Add code to correspond card1 with first click, card2 with second click
    card1=

    card2=

    if evaluate.isMatching(card1,card2):
        card1.revealed=True
        card2.revealed=True
    click_counter+=2
    

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            game_finish=True

    game_finish=game.isFinished(cardlist)

    pygame.display.update()

    #clock.tick(30)

pygame.quit()
