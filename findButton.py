import pygame

def buttonDetect(button):
    '''
    This function checks which button on the menu has been pressed.
    param list: button
    returns: pressed
    '''
    pressed = False
    x, y = pygame.mouse.get_pos()
    buttonXOne = button.getCoordinates()[0]
    buttonXTwo = buttonXOne + button.getsize()[0]
    buttonYOne = button.getCoordinates()[1]
    buttonYTwo = buttonYOne + button.getsize()[1]

    if x>buttonXOne and x<buttonXTwo and y>buttonYOne and y<buttonYTwo:
        button.drawButtonActive()
        if pygame.mouse.get_pressed()[0]:
            pressed = True
    else:
         button.drawButton()

    return pressed
