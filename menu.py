import pygame
import highscores
import sys
import Button
import findButton

def menu():
    '''
    This function sets up the display for the main menu and has some logic determining whether or not the menu should remain on screen.
    param list: none
    returns: None
    '''
    screen = "menu"
    while screen == "menu":
        title = pygame.image.load("")
        gameDisplay = pygame.display.set_mode((800,600))
        gameDisplay.fill("white")
        pygame.display.set_caption("Winter Card Matcher")
        gameDisplay.blit(title,(245,5))
        running = True
        play = Button.Button(gameDisplay, white, green, red, (200, 100), (150, 50), "START")

        highscore = Button.Button(gameDisplay, white, green, red, (200, 200), (250, 50), "HIGHSCORES")

        quitGame = Button.Button(gameDisplay, white, green, red, (200, 300), (350, 50), "QUIT")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if findButton(quitGame):
                    running = False
                    pygame.quit()
                    quit()

                elif findButton(play):
                    running = False
                    mode.mode(amountOfCards)

                elif findButton(highscore):
                    running = False
                    highscore.highscores()

                else:
                    running = True
menu()
