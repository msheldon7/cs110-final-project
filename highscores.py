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

    display_width = 970
    display_length = 650

    gameDisplay = pygame.display.set_mode((display_width, display_length))
    gameDisplay.fill(white)

    font1 = pygame.font.SysFont("Times New Roman", 50)
    title = font1.render("HIGHSCORES", True, black)
    gameDisplay.blit(title, (205, 10))

    font2 = pygame.font.SysFont("Arial", 30)
    name = font2.render("Name:", True, black)
    gameDisplay.blit(name, (60, 120))
    gameDisplay.blit(name, (460, 120))
    score = font2.render("Score:", True, black)
    gameDisplay.blit(score, (280, 120))
    gameDisplay.blit(score, (680, 120))

    back = Button.Button(gameDisplay, white, green, red, (260, 540), (255, 50), "Menu")
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if findButton(back):
                running = False

            else:
                running = True
