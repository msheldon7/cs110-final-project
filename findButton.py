import pygame

def buttonDetect(button):
    pressed = False
    x, y = pygame.mouse.get_pos()
    buttonXOne = button.getRectCords()[0]
    buttonXTwo = buttonXOne + button.getRectSize()[0]
    buttonYOne = button.getRectCords()[1]
    buttonYTwo = buttonYOne + button.getRectSize()[1]

    if x>buttonXOne and x<buttonXTwo and y>buttonYOne and y<buttonYTwo:
        button.drawButtonActive()
        if pygame.mouse.get_pressed()[0]:
            pressed = True
    else:
         button.drawButton()

    return pressed
