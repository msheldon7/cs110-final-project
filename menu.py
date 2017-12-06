
import pygame
import highscores
import sys
import Button
import findButton
import Game

def menu():
    white=(255,255,255)
    red=(255,0,0)
    green=(0,255,0)
    screen = "menu"
    while screen == "menu":
        title = pygame.image.load("title.png")
        gameDisplay = pygame.display.set_mode((970,650))
        gameDisplay.fill(white)
        pygame.display.set_caption("Winter Card Matcher")
        gameDisplay.blit(title,(150,0))
        running = True
        play = Button.Button(gameDisplay, white, green, red, (200, 200), (150, 50), "START")

        highscore = Button.Button(gameDisplay, white, green, red, (200, 300), (250, 50), "HIGHSCORES")

        quitGame = Button.Button(gameDisplay, white, green, red, (200, 400), (350, 50), "QUIT")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if findButton.buttonDetect(quitGame):
                    running = False
                    pygame.quit()
                    quit()

                elif findButton.buttonDetect(play):
                    running = False
                    Game.game(24)

                elif findButton.buttonDetect(highscore):
                    running = False
                    highscore.highscores()

                else:
                    running = True

menu()
