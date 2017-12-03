
import Card
import Grid
import evaluate
import game

import pygame


pygame.init()
pygame.display.set_caption('Matching Game')
#clock=pygame.time.clock()

x=800
y=600

display_window=pygame.display.set_mode((x,y))

game_finish=False

answer=40
table=Grid.Grid(answer)
cardlist=Card.createCardList(answer)
print(cardlist)


#Main game Loop
while not game_finish:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            game_finish=True

    game_finish=game.isFinished(cardlist)

    pygame.display.update()

    #clock.tick(30)

pygame.quit()
