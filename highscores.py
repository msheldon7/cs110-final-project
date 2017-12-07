import pygame
import findButton
import textInput
import sys
import Button


def highscores():
    '''
    This function sets up the highscores screen and displays the list on screen.
    param list: none
    returns: None
    '''
    black = (0,0,0)
    white = (255,255,255)
    green = (0, 255, 0)
    red = (255, 0, 0)

    display_width = 970
    display_length = 650

    gameDisplay = pygame.display.set_mode((display_width, display_length))
    gameDisplay.fill(red)

    font1 = pygame.font.SysFont("Times New Roman", 50)
    title = font1.render("HIGHSCORES", True, black)
    gameDisplay.blit(title, (320, 10))

    font2 = pygame.font.SysFont("Arial", 30)
    name = font2.render("Name:", True, black)
    gameDisplay.blit(name, (60, 120))
    gameDisplay.blit(name, (460, 120))
    score = font2.render("Time:", True, black)
    gameDisplay.blit(score, (280, 120))
    gameDisplay.blit(score, (680, 120))

    back = Button.Button(gameDisplay, white, green, white, (340, 590), (255, 50), "        MENU")
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if findButton.buttonDetect(back):
                running = False

            else:
                running = True
