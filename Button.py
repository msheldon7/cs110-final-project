
import pygame
import sys

pygame.init()

class Button:
    def __init__(self, screen, background, boxColor, hoverOverColor, coordinates, size, text):
        self.textObject = pygame.font.SysFont("Time New Roman", 50)
        self.text = text
        self.textDraw = self.textObject.render(self.text, True, (0,0,0))
        self.screen = screen
        self.background = background
        self.boxColor = boxColor
        self.hoverOverColor = hoverOverColor
        self.coordinates = coordinates
        self.size = size
        self.textCords = (coordinates[0]+3, coordinates[1]-5)
        self.drawButton()

    def drawButton(self):
        self.screen.lock()
        pygame.draw.rect(self.screen, self.boxColor, pygame.Rect(self.coordinates, self.size))
        self.screen.unlock()
        self.screen.blit(self.textDraw, self.coordinates)
        pygame.display.update()

    def drawButtonActive(self):
        self.screen.lock()
        pygame.draw.rect(self.screen, self.hoverOverColor, pygame.Rect(self.coordinates, self.size))
        self.screen.unlock()
        self.screen.blit(self.textDraw, self.coordinates)
        pygame.display.update()

    def drawButtonCover(self):
        self.screen.lock()
        pygame.draw.rect(self.screen, self.background, pygame.Rect((self.coordinates, self.size)))
        self.screen.unlock()
        pygame.display.update()

    def drawText(self):
        self.screen.blit(self.textDraw,self.textCords)
        pygame.display.update()

    def getCoordinates(self):
        return self.coordinates

    def getsize(self):
        return self.size

    def text(self):
        self.text = text
        self.textDraw = self.textObject.render(self.text, True, (0,0,0))

    def getText(self):
        return self.text
