
import pygame
import Card
import random
import Button
import findButton
import sys
import evaluate
import time
import json

def game(player):
    pygame.init()

    back = pygame.image.load("Back.png")

    wintercards = [pygame.image.load("Penguin.png"), pygame.image.load('Snowflake.png'), pygame.image.load('Tree.png'), pygame.image.load('GingerbreadMan.png'), pygame.image.load('NorthPole.png'), pygame.image.load('Star.png'), pygame.image.load('Sleigh.png'), pygame.image.load('Reindeer.png'), pygame.image.load('Owl.png'), pygame.image.load('Stocking.png'), pygame.image.load('Snowman.png'), pygame.image.load('Bells.png'), pygame.image.load('Santa.png'), pygame.image.load('Present.png'), pygame.image.load('Mistletoe.png'), pygame.image.load('Elf.png'), pygame.image.load('Candycane.png'), pygame.image.load('GingerbreadGirl.png'), pygame.image.load('Ornament.png'), pygame.image.load('Wreath.png')]

    display_width = 970
    display_length = 650

    font1 = pygame.font.SysFont("Times New Roman", 20)

    gameDisplay = pygame.display.set_mode((display_width, display_width))
    clock = pygame.time.Clock()

    back = Button.Button(gameDisplay, white, red, green, (50, 535), (250, 50), "Menu")

    totalPointsText = (player + "Score:")

    gameDisplay.fill(blue)
    gameDisplay.blit(title, (245, 5))

    messageOne = font1.render(totalPointsText,1,white)
    gameDisplay.blit(messageOne, (5,25))

    messageTwo = font1.render("Match all the pairs to win",10,white)
    gameDisplay.blit(messageTwo, (330,535))

    messageThree = font1.render("12 points to win",30, white)
    messageFour = font1.render("11 points to win",30, white)
    messageFive = font1.render("10 points to win",30, white)
    messageSix = font1.render("9 points to win",30, white)
    messageSeven = font1.render("8 points to win",30, white)
    messageEight = font1.render("7 points to win",30, white)
    messageNine= font1.render("6 points to win",30, white)
    messageTen = font1.render("5 points to win",30, white)
    messageEleven = font1.render("4 points to win",30, white)
    messageTwelve = font1.render("3 points to win",30, white)
    messageThirteen = font1.render("2 points to win",30, white)
    messageFourteen = font1.render("1 points to win",30, white)
    messageFifteen = font1.render("You won!",30, white)

    cardsRandom = []
    cards = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11]
    for i in range(24):
        randomCard = cards[random.randint(0, len(cards)-1)]
        cardsRandom.append(randomCard)
        cards.remove(randomCard)


    cardList2 = Card.createCardList(24, gameDisplay)#Card list with pictures all in randomized order

    clickcount = 0
    cardlist = []
    running = True
    playerPoints = 0
    scored = 0
    timer = 0
    timerFont = pygame.font.SysFont("Times New Roman", 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        seconds = clock.tick()
        if playerPoints <12:
            timer += seconds
        timerText = timerFont.render("Timer: " + format(timer/1000.0, '.3f'), True, black)
        gameDisplay.blit(timerText, (560,10))

        if findButton(back):
            running = False

        for card in cardList2:
            if not card.getClicked():
                if findButton(card):
                    card.drawCardImage()
                    card.setClicked(True)
                    cardlist.append(card)
                    clickcount +=1

        if clickcount == 2:
            points = 0

            pygame.time.wait(1000)
            cardlist[0],cardlist[1], points = imageCheck.imageCheck(cardlist[0],cardlist[1],points)

            playerPoints += points
            score = font1.render(str(playerOnePoints),1,white)
            gameDisplay.blit(score, (83,50))

            clickcount = 0
            cardlist.clear()
            pygame.time.wait(50)

            if playerOnePoints == 0:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageThree,(560, 535))
            elif playerOnePoints == 1:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageFour,(560,535))
            elif playerOnePoints == 2:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageFive,(560,535))
            elif playerOnePoints == 3:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageSix,(560,535))
            elif playerOnePoints == 4:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageSeven,(560,535))
            elif playerOnePoints == 5:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageEight,(560,535))
            elif playerOnePoints == 6:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageNine,(560,535))
            elif playerOnePoints == 7:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageTen,(560,535))
            elif playerOnePoints == 8:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageEleven,(560,535))
            elif playerOnePoints == 9:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageTwelve,(560,535))
            elif playerOnePoints == 10:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageThirteen,(560,535))
            elif playerOnePoints == 11:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageFourteen,(560,535))
            else:
                gameDisplay.blit(back,(560,534))
                gameDisplay.blit(messageFifteen,(560,535))

        if(playerPoints == 12 and scored == 0):
            timerEnd = timer*100 + random.randint(1, 45)
            highscores = json.load(open("highscoresList.txt", "r"))
            highscores[str(timerEnd)] = str(player)
            json.dump(highscores,open("highscoresList.txt", "w"))
            scored += 1
