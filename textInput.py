import pygame
import Button

def textInput(screen, base):
    '''
    This function gets the input for the user's name to be added to the high scores list.
    param list: screen, base
    returns: base
    '''
    person = ""
    inputString = []
    time = 0
    enter = True

    while enter:
        person = ""
        preLength = len(inputString)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                time = 90
                if event.key == pygame.K_0:
                    inputString.append("0")
                elif event.key == pygame.K_1:
                    inputString.append("1")
                elif event.key == pygame.K_2:
                    inputString.append("2")
                elif event.key == pygame.K_3:
                    inputString.append("3")
                elif event.key == pygame.K_4:
                    inputString.append("4")
                elif event.key == pygame.K_5:
                    inputString.append("5")
                elif event.key == pygame.K_6:
                    inputString.append("6")
                elif event.key == pygame.K_7:
                    inputString.append("7")
                elif event.key == pygame.K_8:
                    inputString.append("8")
                elif event.key == pygame.K_9:
                    inputString.append("9")
                elif event.key == pygame.K_q:
                    inputString.append("q")
                elif event.key == pygame.K_w:
                    inputString.append("w")
                elif event.key == pygame.K_e:
                    inputString.append("e")
                elif event.key == pygame.K_r:
                    inputString.append("r")
                elif event.key == pygame.K_t:
                    inputString.append("t")
                elif event.key == pygame.K_y:
                    inputString.append("y")
                elif event.key == pygame.K_u:
                    inputString.append("u")
                elif event.key == pygame.K_i:
                    inputString.append("i")
                elif event.key == pygame.K_o:
                    inputString.append("o")
                elif event.key == pygame.K_p:
                    inputString.append("p")
                elif event.key == pygame.K_a:
                    inputString.append("a")
                elif event.key == pygame.K_s:
                    inputString.append("s")
                elif event.key == pygame.K_d:
                    inputString.append("d")
                elif event.key == pygame.K_f:
                    inputString.append("f")
                elif event.key == pygame.K_g:
                    inputString.append("g")
                elif event.key == pygame.K_h:
                    inputString.append("h")
                elif event.key == pygame.K_j:
                    inputString.append("j")
                elif event.key == pygame.K_k:
                    inputString.append("k")
                elif event.key == pygame.K_l:
                    inputString.append("l")
                elif event.key == pygame.K_z:
                    inputString.append("z")
                elif event.key == pygame.K_x:
                    inputString.append("x")
                elif event.key == pygame.K_c:
                    inputString.append("c")
                elif event.key == pygame.K_v:
                    inputString.append("v")
                elif event.key == pygame.K_b:
                    inputString.append("b")
                elif event.key == pygame.K_n:
                    inputString.append("n")
                elif event.key == pygame.K_m:
                    inputString.append("m")
                elif event.key == pygame.K_RETURN:
                    enter = False
                elif event.key == pygame.K_BACKSPACE:
                    if len(inputString)>0:
                        base.drawButtonCover()
                        del inputString[-1]
                else:
                    time = 0
            pygame.event.clear()
        if preLength != len(inputString):
            #This is to to help limit the length of the username
            if len(inputString) > 8:
                num = 7
                while num<50:
                    try:
                        del inputString[num]
                        num += 1
                    except:
                        num = 50
            for element in inputString:
                time += element
            base.setText(person)
        base.drawButton()
        pygame.time.wait(time)

    return base
